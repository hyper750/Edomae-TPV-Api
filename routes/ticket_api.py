from flask_restful import Api
from resources.ticket import TicketCommandResource

TICKET_API = Api(prefix='/ticket')

# Print command
TICKET_API.add_resource(TicketCommandResource, '/command/<int:id>')
