from flask_jwt_extended import jwt_required
from flask_restful import Resource
from models import PaymentMethod, PaymentMethodSchema


class PaymentMethodResource(Resource):
    method_decorators = (jwt_required(),)

    def get(self, id: int):
        payment_method = PaymentMethod.query.get(id)

        if not payment_method:
            return '', 404

        return PaymentMethodSchema().dump(payment_method)

    def put(self, id: int):
        pass

    def delete(self, id: int):
        payment_method = PaymentMethod.query.get(id)
        if payment_method:
            payment_method.delete()
        return '', 204


class PaymentMethodsResource(Resource):
    method_decorators = (jwt_required(),)

    def get(self):
        pass

    def post(self):
        pass
