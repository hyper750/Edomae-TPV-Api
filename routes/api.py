from flask_restful import Api
from resources import Auth, MealResource, MealsResource

API_ROUTES = Api()

# Auth route
API_ROUTES.add_resource(Auth, '/auth')

# Meal routes
API_ROUTES.add_resource(MealResource, '/meal/<int:id>')
API_ROUTES.add_resource(MealsResource, '/meal/')
