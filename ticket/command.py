from jinja2 import Environment, FileSystemLoader
from settings import TEMPLATE_DIR, TICKET_COMMAND_TEMPLATE_NAME, TICKET_COMMAND_LOGO
import base64
from models import Command, CommandMeal, Table, Meal


def get_edomae_logo() -> str:
    content = ''
    with open(TICKET_COMMAND_LOGO, "rb") as f:
        content = base64.b64encode(f.read()).decode()
    return content


def generate_ticket(id: int) -> str:
    file_loader = FileSystemLoader(TEMPLATE_DIR)
    env = Environment(loader=file_loader)
    template_content = env.get_template(TICKET_COMMAND_TEMPLATE_NAME)
    
    command = Command.query.get(id)
    command_meals = CommandMeal.query.filter_by(command=id)
    table = Table.query.get(command.table)

    data = {
        'EDOMAE_LOGO_BASE64': get_edomae_logo(),
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
        'COMMAND_TOTAL_PRICE': 13,
        'COMMAND_TOTAL_PRICE_WITHOUT_IVA': 10.27,
        'COMMAND_IVA': 21,
        'COMMAND_IVA_PRICE': 2.1567,
        'CURRENT_DATE': 'Lunes 3 Enero 2021 21:16:12',
        'EMPLOYEE_NAME': 'Cristian Lopez Alonso'
    }

    return template_content.render(**data)
