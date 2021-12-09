from flask_jwt_extended import jwt_required
from flask_restful import Resource
from parser import (
    parse_object_local,
    parse_query_local
)
from models import Local
from serialization import LocalSchema


class LocalResource(Resource):
    method_decorators = (jwt_required(),)

    def get(self, id: int):
        local = Local.query.get(id)

        if not local:
            return '', 404

        return LocalSchema().dump(local)

    def delete(self, id: int):
        local = Local.query.get(id)
        if local:
            local.delete()
        return '', 204

    def put(self, id: int):
        local = Local.query.get(id)

        if not local:
            return '', 404

        params = parse_query_local()
        for key, value in params.items():
            setattr(local, key, value)

        local.save()

        return LocalSchema().dump(local)


class LocalsResource(Resource):
    method_decorators = (jwt_required(),)

    def post(self):
        local = Local(
            **parse_object_local()
        )

        local.save()

        return LocalSchema().dump(local), 201

    def get(self):
        locals = Local.query.filter_by(
            **parse_query_local()
        ).order_by(Local.name)
        return LocalSchema(many=True).dump(locals)
