from flask_jwt_extended import jwt_required
from flask_restful import Resource

class TicketCommandResource(Resource):
    method_decorators = (jwt_required(),)

    def get(self, id: int):

        return {
            'html': '<html></html>'
        }
