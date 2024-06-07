with app.app_context():
    members_between_ages = db.session.query(Member).filter(
        Member.age.between(25, 30)
    ).all()
    for member in members_between_ages:
        print(f"Name: {member.name}, Age: {member.age}, Trainer ID: {member.trainer_id}")
