from .authentication_parser import parse_login
from .command import parse_object_command, parse_query_command
from .command_meal import parse_object_command_meal, parse_query_command_meal
from .contact_message import (
    parse_contact_message_object,
    parse_contact_message_query,
    parse_contact_message_update
)
from .local import parse_object_local, parse_query_local
from .meal import parse_object_meal, parse_query_meal
from .meal_category import (
    parse_object_meal_category,
    parse_query_meal_category
)
from .payment_method import (
    parse_object_payment_method,
    parse_query_payment_method
)
from .table import parse_object_table, parse_query_table
from .ticket_command import parse_query_ticket_command
from .translation import parse_translation_object, parser_translation_query
