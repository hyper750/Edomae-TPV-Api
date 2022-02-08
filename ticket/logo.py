import base64

from settings import TICKET_COMMAND_LOGO


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
