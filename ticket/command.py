import base64
from typing import List

import arrow
from jinja2 import Environment, FileSystemLoader
from models import Command, CommandMeal, Meal, Table, User
from settings import (
    IVA, TEMPLATE_DIR, TICKET_COMMAND_LOGO,
    TICKET_COMMAND_TEMPLATE_NAME, TIMEZONE
)
from utils.math import calculate_percentage


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
