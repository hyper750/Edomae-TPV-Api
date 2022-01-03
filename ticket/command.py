from jinja2 import Environment, FileSystemLoader
from settings import TEMPLATE_DIR, TICKET_COMMAND_TEMPLATE_NAME


def generate_ticket(id: int) -> str:
    file_loader = FileSystemLoader(TEMPLATE_DIR)
    env = Environment(loader=file_loader)
    template_content = env.get_template(TICKET_COMMAND_TEMPLATE_NAME)

    data = {}

    return template_content.render(**data)
