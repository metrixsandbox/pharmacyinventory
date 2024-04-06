# app.py
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@localhost/your_database_name'
db = SQLAlchemy(app)

# Define your models here using SQLAlchemy

@app.route('/')
def index():
    return jsonify({'message': 'Welcome to Medication Inventory API'})

# Add more routes and functionality as needed


# Add more routes and functionality as needed

if __name__ == '__main__':
    app.run(debug=True)
