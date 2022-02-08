from typing import List

import arrow
from db.sqlalchemy.sqlalchemy import DB
from jinja2 import Environment, FileSystemLoader
from models import CommandMeal, Meal, MealCategory
from settings import (
    IVA, SOCIETY_CIF, SOCIETY_NAME, SOCIETY_QUARTERS,
    TEMPLATE_DIR, TICKET_SERIE_TEMPLATE_NAME
)
from sqlalchemy import func
from utils.math import calculate_percentage

from .abstract_ticket import AbstractTicket
from .table_ticket import TableTicket
from .logo import get_edomae_logo


def generate_ticket(id: int) -> str:
    TICKETS_AVAILABLE: List[AbstractTicket] = [
        TableTicket()
    ]

    for ticket_available in TICKETS_AVAILABLE:
        if ticket_available.can_generate_ticket(id):
            return ticket_available.get_ticket(id)


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
            last_category = meal_category

        # When changing meals save the last categories
        # Or is the last item
        if meal_category.id != last_category.id:
            # Push previos categories data
            meal_by_categories.append({
                'name': last_category.name,
                'total_price': 0,
                'meals': list(meals.values()),
            })
            last_category = meal_category
            meals = dict()

        # Append new meal on that category
        if meal.id not in meals:
            meals[meal.id] = dict(
                name=meal.name,
                quantity=command_meal.number,
                price=round(command_meal.price, 2),
                total_price=command_meal.total_price
            )
        else:
            # Update price and quantity
            meals[meal.id]['quantity'] += command_meal.number
            meals[meal.id]['total_price'] = round(
                meals[meal.id]['total_price'] + command_meal.total_price, 2)

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
        category['total_price'] = round(total_category_price, 2)

    data = {
        'SOCIETY_NAME': SOCIETY_NAME,
        'SOCIETY_CIF': SOCIETY_CIF,
        'SOCIETY_QUARTERS': SOCIETY_QUARTERS,
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
