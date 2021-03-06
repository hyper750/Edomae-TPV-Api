from parser import parse_object_command, parse_query_command

import arrow
from flask_jwt_extended import get_jwt_identity, jwt_required
from flask_restful import Resource
from logic.model_filter.paginate import paginate_queryset
from models import Command
from serialization import CommandSchema
from sqlalchemy import desc


class CommandResource(Resource):
    method_decorators = (jwt_required(),)

    def get(self, id: int):
        command = Command.query.get(id)

        if not command:
            return '', 404

        return CommandSchema().dump(command)

    def put(self, id: int):
        command = Command.query.get(id)

        if not command:
            return '', 404

        for key, value in parse_object_command().items():
            setattr(command, key, value)

        command.save()

        return CommandSchema().dump(command)

    def delete(self, id: int):
        command = Command.query.get(id)

        if command:
            command.delete()

        return '', 204


class CommandsResource(Resource):
    method_decorators = (jwt_required(),)

    def get(self):
        params = parse_query_command()

        # Get filter date filters
        start_date = params.pop('creation_date__gte', None)
        end_date = params.pop('creation_date__lte', None)

        # Get paginate filters
        page_size = params.pop('page_size')
        page_num = params.pop('page_num')

        # Get queryset
        commands = Command.query.filter()

        # Filter by raw fields
        commands = commands.filter_by(
            **params
        )

        # Filter by creation date
        if start_date:
            commands = commands.filter(
                Command.creation_date >= arrow.get(
                    start_date
                ).floor('day').datetime
            )
        if end_date:
            commands = commands.filter(
                Command.creation_date <= arrow.get(
                    end_date
                ).ceil('day').datetime
            )

        # Order by creation date desc, most recent on the top
        commands = commands.order_by(desc(Command.creation_date))

        # Paginate queryset
        commands = paginate_queryset(commands, page_size, page_num)

        return CommandSchema(many=True).dump(commands)

    def post(self):
        command = Command(
            user=get_jwt_identity(),
            **parse_object_command()
        )
        command.save()
        return CommandSchema().dump(command), 201
