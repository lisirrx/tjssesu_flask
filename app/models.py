from app import db


class Student(db.Model):
    __tablename__ = 'student'
    id = db.Column(db.Unicode(10), primary_key = True, unique = True)
    name = db.Column(db.Unicode(1000))
    gender = db.Column(db.Unicode(1000))

    phone_number = db.Column(db.Unicode(1000))
    class_number = db.Column(db.Unicode(1000))
    native_place = db.Column(db.Unicode(1000))
    email = db.Column(db.Unicode(1000))
    
    department1 = db.Column(db.Unicode(1000))
    department2 = db.Column(db.Unicode(1000))
    
    skill = db.Column(db.UnicodeText)
    former_job = db.Column(db.UnicodeText)
    former_experience = db.Column(db.UnicodeText)
    reason = db.Column(db.UnicodeText)

    expection = db.Column(db.UnicodeText)
    
    obey_swap = db.Column(db.Boolean)
    turn_major = db.Column(db.Boolean)
    def __repr__(self):
        return '<name %r>' % self.name

