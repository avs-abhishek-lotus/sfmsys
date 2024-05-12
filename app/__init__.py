from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from app import routes, models
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:your_password@localhost/InventoryManagement'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

app.config['JWT_SECRET_KEY'] = 'your_jwt_secret_key'  # Change this!
jwt = JWTManager(app)

@app.errorhandler(Exception)
def handle_unexpected_error(error):
    response = jsonify({'message': 'An unexpected error occurred', 'details': str(error)})
    response.status_code = 500
    return response

# Initialize it after db
migrate = Migrate(app, db)