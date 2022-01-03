from jinja2 import Environment, FileSystemLoader
from settings import TEMPLATE_DIR, TICKET_COMMAND_TEMPLATE_NAME, TICKET_COMMAND_LOGO
import base64


def get_edomae_logo() -> str:
    content = ''
    with open(TICKET_COMMAND_LOGO, "r") as f:
        content = base64.b64encode(f.read())
    return content


def generate_ticket(id: int) -> str:
    file_loader = FileSystemLoader(TEMPLATE_DIR)
    env = Environment(loader=file_loader)
    template_content = env.get_template(TICKET_COMMAND_TEMPLATE_NAME)

    data = {
        'EDOMAE_LOGO_BASE64': get_edomae_logo()
    }

    return template_content.render(**data)
