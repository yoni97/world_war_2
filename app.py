from flask import Flask
from db import db
from routes.mission_route import mission_bp
from psycopg2

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1234@localhost:5432/wwi_missions'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
######## first create ########

with app.app_context():
    db.create_all()
@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'
app.register_blueprint(mission_bp, url_prefix='/mission')

if __name__ == '__main__':
    app.run()
