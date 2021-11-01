from .authentication_parser import parse_login
from .command import parse_object_command, parse_query_command
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
