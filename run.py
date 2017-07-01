import os
from os.path import join, dirname

from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

from config import app_config

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

config_name = os.getenv('FLASK_CONFIG')
print(config_name)

db = SQLAlchemy()

app = Flask(__name__)
app.config.from_object(app_config[config_name])
db.init_app(app)

@app.route('/index', methods=['GET'])
def show_index():
    return jsonify({ 'message': 'You have succesfully created the basic setup' })

if __name__ == '__main__':
    app.run()
    

