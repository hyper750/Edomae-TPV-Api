from models import Language, Meal, MealCategory, PaymentMethod


def get_translation_recommendations_keys(**filters) -> set:
    keys = set()

    # Add Meal keys
    for meal in Meal.query.filter_by(**filters):
        keys.add(meal.name)
        keys.add(meal.description)
    
    # Add Meal category and payment methods keys
    models = [
        MealCategory,
        PaymentMethod
    ]
    for model in models:
        for item in model.query.filter_by(**filters):
            keys.add(item.name)

    return keys
