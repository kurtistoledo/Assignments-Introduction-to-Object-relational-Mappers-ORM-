from flask import Flask
from models import db, Member

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///fitness_center.db'
db.init_app(app)

with app.app_context():
    distinct_trainers = db.session.query(Member.trainer_id).distinct().all()
    print(distinct_trainers)
