from sqlalchemy import func

with app.app_context():
    member_count_by_trainer = db.session.query(
        Member.trainer_id, func.count(Member.id)
    ).group_by(Member.trainer_id).all()
    print(member_count_by_trainer)
