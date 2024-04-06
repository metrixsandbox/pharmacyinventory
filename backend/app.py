# app.py
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://postgres:{os.environ.get('DATABASE_PASSWORD')}@192.168.1.17:5432/inventory'
db = SQLAlchemy(app)

# Define your models here using SQLAlchemy

@app.route('/')
def index():
    return jsonify({'message': 'Welcome to Medication Inventory API'})

# Add more routes and functionality as needed


# Add more routes and functionality as needed

if __name__ == '__main__':
    app.run(debug=True)
