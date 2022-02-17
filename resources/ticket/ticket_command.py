from parser import parse_query_ticket_command

import arrow
from flask import make_response
from flask_jwt_extended import jwt_required
from flask_restful import Resource
from models import Command

from ticket.command import generate_serie_ticket, generate_ticket


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
        response = []

        params = parse_query_ticket_command()

        start_date = arrow.get(params.get('creation_date__gte')).floor('day')
        end_date = arrow.get(params.get('creation_date__lte')).ceil('day')

        for start, end in arrow.Arrow.interval('day', start_date, end_date):
            commands = Command.query.filter(
                Command.creation_date >= start.datetime,
                Command.creation_date <= end.datetime
            )
            command_ids = [command.id for command in commands]
            if command_ids:
                response.append(dict(
                    html=generate_serie_ticket(start, command_ids)
                ))

        return response
