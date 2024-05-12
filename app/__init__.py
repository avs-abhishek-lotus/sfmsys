from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from config import DevelopmentConfig  # Import the appropriate config

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)  # Or whichever config you're using

db = SQLAlchemy(app)
migrate = Migrate(app, db)
jwt = JWTManager(app)

from app import routes, models  # Import routes and models at the end to avoid circular dependencies

# Error handling
@app.errorhandler(Exception)
def handle_unexpected_error(error):
    response = jsonify({'message': 'An unexpected error occurred', 'details': str(error)})
    response.status_code = 500
    return response
