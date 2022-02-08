from typing import List

import arrow
from models import Command, CommandMeal, Meal, User
from settings import IVA, TICKET_COMMAND_DELIVERY_TEMPLATE_NAME, TIMEZONE
from utils.math import calculate_percentage

from .abstract_ticket import AbstractTicket
from .logo import get_edomae_logo


class CommandDelivery(AbstractTicket):

    def can_generate_ticket(self, id: int) -> bool:
        command: Command = Command.query.get(id)
        return command.is_home_delivery

    def get_template_name(self) -> str:
        return TICKET_COMMAND_DELIVERY_TEMPLATE_NAME

    def get_content(self, id: int) -> dict:
        command: Command = Command.query.get(id)
        command_meals: List[CommandMeal] = CommandMeal.query.filter_by(
            command=id
        )
        user: User = User.query.get(command.user)

        total_command_price = round(
            sum(
                command_meal.total_price
                for command_meal in command_meals
            ),
            2
        )
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
            'COMMAND_ADDRESS': command.delivery_address,
            'COMMAND_DETAILS': command.delivery_details,
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

        return data
