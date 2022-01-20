import arrow
from db.sqlalchemy.sqlalchemy import DB
from flask import make_response
from flask_jwt_extended import jwt_required
from flask_restful import Resource
from models import Command, CommandMeal

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

        start_date = arrow.Arrow(2021, 7, 1)
        end_date = arrow.Arrow(2022, 7, 1)

        for start, end in arrow.Arrow.interval('day', start_date, end_date):
            commands = Command.query.filter(
                Command.creation_date >= start.datetime,
                Command.creation_date <= end.datetime
            )
            command_ids = [command.id for command in commands]
            serie_total_price = DB.session.query(DB.session.func.sum(CommandMeal.total_price)).filter(
                CommandMeal.command.in_(command_ids)
            )
            response.append(dict(
                start_date=start.isoformat(),
                end_date=end.isoformat(),
                total_price=serie_total_price
            ))

        return response
