from flask_jwt_extended import get_jwt_identity, jwt_required
from flask_restful import Resource
from logic.command import parse_object_command, parse_query_command
from logic.model_filter.date_filter import filter_by_date_range
from logic.model_filter.paginate import paginate_queryset
from models import Command, CommandSchema
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
        commands = Command.query.all()

        # Filter by raw fields
        commands = commands.filter_by(
            **params
        )

        # Filter by creation date
        # commands = filter_by_date_range(commands, )
        # if start_date:
        #     commands = commands.filter(Command.creation_date > start_date)
        # if end_date:
        #     commands = commands.filter(Command.creation_date < end_date)

        # Paginate queryset
        commands = paginate_queryset(commands, page_size, page_num)

        # Order by creation date desc, most recent on the top
        commands = commands.order_by(desc(Command.creation_date))

        return CommandSchema(many=True).dump(commands)

    def post(self):
        command = Command(
            user=get_jwt_identity(),
            **parse_object_command()
        )
        command.save()
        return CommandSchema().dump(command)
