from flask import Flask
from flask_jwt import JWT
from flask_migrate import Migrate

from logic.user import authenticate_user, identity_user
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
jwt = JWT(app, authenticate_user, identity_user)

# TODO: Initialize api resources

if __name__ == '__main__':
    app.run()
