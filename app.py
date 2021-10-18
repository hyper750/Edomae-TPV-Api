from flask import Flask
from flask_migrate import Migrate

from logic.user import JWT
from routes import API_ROUTES
from settings import DB, FLASK_CONFIG, MA

app = Flask('Commander')

# Configure app
app.config.update(FLASK_CONFIG)

# Initialize database
DB.init_app(app)

# Initialize database migrations
migrate = Migrate(app, DB)

# Initialize database serializer
MA.init_app(app)

# Initialize jwt
JWT.init_app(app)

# Initialize api routes
API_ROUTES.init_app(app)

if __name__ == '__main__':
    app.run()
