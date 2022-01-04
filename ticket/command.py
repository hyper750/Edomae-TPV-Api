from jinja2 import Environment, FileSystemLoader
from settings import TEMPLATE_DIR, TICKET_COMMAND_TEMPLATE_NAME, TICKET_COMMAND_LOGO
import base64


def get_edomae_logo() -> str:
    content = ''
    with open(TICKET_COMMAND_LOGO, "rb") as f:
        content = base64.b64encode(f.read()).decode()
    return content


def generate_ticket(id: int) -> str:
    file_loader = FileSystemLoader(TEMPLATE_DIR)
    env = Environment(loader=file_loader)
    template_content = env.get_template(TICKET_COMMAND_TEMPLATE_NAME)

    data = {
        'EDOMAE_LOGO_BASE64': get_edomae_logo(),
        'COMMAND_ID': 46,
        'TABLE_NUMBER': 2,
        'COMMAND_MEALS': [
            {
                'number': 23,
                'name': 'Gyozas de pollo',
                'price': 6.52,
                'total_price': 6.52
            },
            {
                'number': 23,
                'name': 'Gyozas de langostino',
                'price': 6.59,
                'total_price': 6.59
            }
        ],
        'COMMAND_TOTAL_PRICE': 13,
        'COMMAND_TOTAL_PRICE_WITHOUT_IVA': 10.27,
        'COMMAND_IVA': 21,
        'COMMAND_IVA_PRICE': 2.1567,
        'CURRENT_DATE': 'Lunes 3 Enero 2021 21:16:12',
        'EMPLOYEE_NAME': 'Cristian Lopez Alonso'
    }

    return template_content.render(**data)
