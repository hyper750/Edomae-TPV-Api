from flask_restful import Api
from resources.ticket import (
    TicketCommandResource,
    TicketCommandsResource
)

TICKET_API = Api(prefix='/ticket')

# Print commands by query
TICKET_API.add_resource(TicketCommandsResource, '/command')

# Print command by id
TICKET_API.add_resource(TicketCommandResource, '/command/<int:id>')
