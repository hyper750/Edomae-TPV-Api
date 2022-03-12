from parser import (
    parse_contact_message_object, parse_contact_message_query,
    parse_contact_message_update
)

from flask_jwt_extended import jwt_required
from flask_restful import Resource
from logic.model_filter.paginate import paginate_queryset
from models import ContactMessage
from serialization import ContactMessageSchema
from sqlalchemy import desc


class ContactMessageResource(Resource):
    method_decorators = (jwt_required(),)

    def get(self, id: int):
        contact_message = ContactMessage.query.get(id)

        if not contact_message:
            return '', 404

        return ContactMessageSchema().dump(contact_message)

    def delete(self, id: int):
        contact_message = ContactMessage.query.get(id)

        if contact_message:
            contact_message.delete()

        return '', 204

    def put(self, id: int):
        contact_message = ContactMessage.query.get(id)

        if not contact_message:
            return '', 404

        for key, value in parse_contact_message_update().items():
            setattr(contact_message, key, value)

        contact_message.save()

        return ContactMessageSchema().dump(contact_message)


class ContactMessagesResource(Resource):

    def post(self):
        contact_message = ContactMessage(
            **parse_contact_message_object()
        )

        contact_message.save()
        return ContactMessageSchema().dump(contact_message), 201

    @jwt_required()
    def get(self):
        params = parse_contact_message_query()
        page_size = params.get('page_size')
        page_num = params.get('page_num')
        contact_messages = ContactMessage.query.order_by(
            desc(ContactMessage.creation_date)
        )

        contact_messages = paginate_queryset(
            contact_messages,
            page_size,
            page_num
        )

        return ContactMessageSchema(many=True).dump(contact_messages)
