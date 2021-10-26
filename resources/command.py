from flask_jwt_extended import get_jwt_identity, jwt_required
from flask_restful import Resource
from logic.command import parse_object_command, parse_query_command
from models import Command, CommandSchema


class CommandResource(Resource):
    method_decorator = (jwt_required(),)

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
    method_decorator = (jwt_required(),)

    def get(self):
        commands = Command.query.filter_by(
            **parse_query_command()
        )
        return CommandSchema(many=True).dump(commands)

    def post(self):
        command = Command(
            user=get_jwt_identity(),
            **parse_object_command()
        )
        command.save()
        return CommandSchema().dump(command)
