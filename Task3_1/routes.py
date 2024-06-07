from flask import request, jsonify
from app import app, db
from models import Member, member_schema, members_schema

@app.route('/members', methods=['POST'])
def add_member():
    name = request.json['name']
    age = request.json['age']
    membership_type = request.json['membership_type']
    trainer_id = request.json['trainer_id']

    new_member = Member(name=name, age=age, membership_type=membership_type, trainer_id=trainer_id)

    db.session.add(new_member)
    db.session.commit()

    return member_schema.jsonify(new_member)

@app.route('/members/<int:id>', methods=['GET'])
def get_member(id):
    member = Member.query.get_or_404(id)
    return member_schema.jsonify(member)

@app.route('/members/<int:id>', methods=['PUT'])
def update_member(id):
    member = Member.query.get_or_404(id)

    member.name = request.json['name']
    member.age = request.json['age']
    member.membership_type = request.json['membership_type']
    member.trainer_id = request.json['trainer_id']

    db.session.commit()

    return member_schema.jsonify(member)

@app.route('/members/<int:id>', methods=['DELETE'])
def delete_member(id):
    member = Member.query.get_or_404(id)
    db.session.delete(member)
    db.session.commit()
    return jsonify({'message': 'Member deleted successfully'})

@app.route('/members', methods=['GET'])
def get_all_members():
    members = Member.query.all()
    return members_schema.jsonify(members)

from models import WorkoutSession, workout_session_schema, workout_sessions_schema

@app.route('/workouts', methods=['POST'])
def add_workout():
    member_id = request.json['member_id']
    session_date = request.json['session_date']
    activity = request.json['activity']
    duration = request.json['duration']

    new_workout = WorkoutSession(member_id=member_id, session_date=session_date, activity=activity, duration=duration)

    db.session.add(new_workout)
    db.session.commit()

    return workout_session_schema.jsonify(new_workout)

@app.route('/workouts/<int:id>', methods=['PUT'])
def update_workout(id):
    workout = WorkoutSession.query.get_or_404(id)

    workout.member_id = request.json['member_id']
    workout.session_date = request.json['session_date']
    workout.activity = request.json['activity']
    workout.duration = request.json['duration']

    db.session.commit()

    return workout_session_schema.jsonify(workout)

@app.route('/workouts/<int:id>', methods=['DELETE'])
def delete_workout(id):
    workout = WorkoutSession.query.get_or_404(id)
    db.session.delete(workout)
    db.session.commit()
    return jsonify({'message': 'Workout session deleted successfully'})

@app.route('/workouts/member/<int:member_id>', methods=['GET'])
def get_workouts_by_member(member_id):
    workouts = WorkoutSession.query.filter_by(member_id=member_id).all()
    return workout_sessions_schema.jsonify(workouts)

