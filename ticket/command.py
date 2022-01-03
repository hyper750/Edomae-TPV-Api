from jinja2 import Environment, FileSystemLoader
from settings import TICKET_COMMAND_TEMPLATE


def generate_ticket(id: int) -> str:
    file_loader = FileSystemLoader()
    env = Environment(loader=file_loader)
    template_content = env.get_template(TICKET_COMMAND_TEMPLATE)

    data = {}

    return template_content.render(**data)
