from flask import make_response
from flask_jwt_extended import jwt_required
from flask_restful import Resource
from models import Command

from ticket.command import generate_ticket


class TicketCommandResource(Resource):
    method_decorators = (jwt_required(),)

    def get(self, id: int):
        command = Command.query.get(id)

        if not command:
            return '', 404

        return make_response(generate_ticket(id))


class TicketCommandsResource(Resource):
    method_decorators = (jwt_required(),)

    def get(self):
        # TODO: Add start date and end date query params
        response = []

        for command in Command.query.all():
            response.append(
                generate_ticket(command.id)
            )

        return response
