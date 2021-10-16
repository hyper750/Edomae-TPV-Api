from flask_restful import Api
from resources import Auth

API_ROUTES = Api()

# Auth route
API_ROUTES.add_resource(Auth, '/auth')
