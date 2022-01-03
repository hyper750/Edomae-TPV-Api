from settings import TICKET_COMMAND_TEMPLATE


def generate_ticket(id: int) -> str:
    template_content = ''

    with open(TICKET_COMMAND_TEMPLATE, "r") as f:
        template_content = f.read()

    return template_content
