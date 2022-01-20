import base64
from typing import List

import arrow
from jinja2 import Environment, FileSystemLoader
from models import Command, CommandMeal, Meal, Table, User, MealCategory
from settings import (
    IVA, TEMPLATE_DIR, TICKET_COMMAND_LOGO,
    TICKET_COMMAND_TEMPLATE_NAME, TICKET_SERIE_TEMPLATE_NAME,
    TIMEZONE
)
from utils.math import calculate_percentage
from sqlalchemy import func
from db.sqlalchemy.sqlalchemy import DB


def get_edomae_logo() -> str:
    logo_extension = 'data:image/png'

    content = ''
    with open(TICKET_COMMAND_LOGO, "rb") as f:
        base_64_logo = base64.b64encode(f.read()).decode()
        content = f'base64, {base_64_logo}'

    return '{};{}'.format(
        logo_extension,
        content
    )


def generate_ticket(id: int) -> str:
    file_loader = FileSystemLoader(TEMPLATE_DIR)
    env = Environment(loader=file_loader)
    template_content = env.get_template(TICKET_COMMAND_TEMPLATE_NAME)

    command: Command = Command.query.get(id)
    command_meals: List[CommandMeal] = CommandMeal.query.filter_by(command=id)
    table: Table = Table.query.get(command.table)
    user: User = User.query.get(command.user)

    total_command_price = round(sum(
        command_meal.total_price
        for command_meal in command_meals
    ), 2)
    iva_price = round(
        calculate_percentage(total_command_price, IVA),
        2
    )
    price_without_iva = round(total_command_price - iva_price, 2)

    # 'Lunes 3 Enero 2021 21:16:12'
    # TODO: Command creation date
    current_date = arrow.now(tz=TIMEZONE).format(
        'dddd DD MMMM YYYY HH:mm:ss',
        locale='ES'
    )

    data = {
        'EDOMAE_LOGO': get_edomae_logo(),
        'COMMAND_ID': command.id,
        'TABLE_NUMBER': table.number,
        'COMMAND_MEALS': [
            {
                'quantity': command_meal.number,
                'name': Meal.query.get(command_meal.meal).name,
                'extra': command_meal.extra,
                'price': command_meal.price,
                'total_price': command_meal.total_price,
                'discount': command_meal.discount
            }
            for command_meal in command_meals
        ],
        'COMMAND_TOTAL_PRICE': total_command_price,
        'COMMAND_TOTAL_PRICE_WITHOUT_IVA': price_without_iva,
        'COMMAND_IVA': IVA,
        'COMMAND_IVA_PRICE': iva_price,
        'CURRENT_DATE': current_date,
        'EMPLOYEE_NAME': user.get_full_name()
    }

    return template_content.render(**data)


def generate_serie_ticket(serie_date: arrow.Arrow, command_ids: List[int]) -> str:
    # Total
    total_price = DB.session.query(func.sum(CommandMeal.total_price)).filter(
        CommandMeal.command.in_(command_ids)
    ).scalar()

    iva_price = round(
        calculate_percentage(total_price, IVA),
        2
    )
    price_without_iva = round(total_price - iva_price, 2)

    # Meals ordered by category order
    res = DB.session.query(
        CommandMeal,
        Meal,
        MealCategory
    ).filter(
        CommandMeal.meal == Meal.id
    ).filter(
        Meal.category == MealCategory.id
    ).filter(
        CommandMeal.command.in_(command_ids)
    ).order_by(
        MealCategory.order
    ).all()

    meal_by_categories = []
    meals = dict()
    last_category = None
    total_results = len(res)
    for i, (command_meal, meal, meal_category) in enumerate(res):
        # Fill first category
        if last_category is None:
            last_category = meal_category.id

        # When changing meals save the last categories
        # Or is the last item
        if meal_category.id != last_category:
            last_category = meal_category.id
            # Push previos categories data
            meal_by_categories.append({
                'name': meal_category.name,
                'total_price': 0,
                'meals': list(meals.values()),
            })
            meals = dict()

        # Append new meal on that category
        if meal.id not in meals:
            meals[meal.id] = dict(
                name=meal.name,
                quantity=command_meal.number,
                price=command_meal.price,
                total_price=command_meal.total_price
            )
        else:
            # Update price and quantity
            meals[meal.id]['quantity'] += command_meal.number
            meals[meal.id]['total_price'] += command_meal.total_price

        # Is last item
        if i + 1 >= total_results:
            meal_by_categories.append({
                'name': meal_category.name,
                'total_price': 0,
                'meals': list(meals.values()),
            })

    # Calculate total price for each category
    for category in meal_by_categories:
        total_category_price = sum(
            meal['total_price']
            for meal in category.get('meals', [])
        )
        category['total_price'] = total_category_price

    data = {
        'EDOMAE_LOGO': get_edomae_logo(),
        'SERIE_DATE': serie_date.date().isoformat(),
        'TOTAL_PRICE': round(total_price, 2),
        'TOTAL_PRICE_WITHOUT_IVA': price_without_iva,
        'IVA': IVA,
        'IVA_PRICE': iva_price,
        'MEAL_CATEGORIES': meal_by_categories
    }

    file_loader = FileSystemLoader(TEMPLATE_DIR)
    env = Environment(loader=file_loader)
    template_content = env.get_template(TICKET_SERIE_TEMPLATE_NAME)

    return template_content.render(**data)
