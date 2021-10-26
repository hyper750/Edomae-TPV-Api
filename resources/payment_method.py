from flask_jwt_extended import jwt_required
from flask_restful import Resource


class PaymentMethodResource(Resource):
    method_decorators = (jwt_required(),)

    def get(self, id: int):
        pass

    def put(self, id: int):
        pass

    def delete(self, id: int):
        pass


class PaymentMethodsResource(Resource):
    method_decorators = (jwt_required(),)

    def get(self):
        pass

    def post(self):
        pass
