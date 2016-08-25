from . import db


class Student(db.Model):
    __tablename__ = 'student'
    id = db.Column(db.Unicode, primary_key = True, unique = True)
    name = db.Column(db.Unicode)
    email = db.Column(db.Unicode)
    department1 = db.Column(db.Unicode)
    department2 = db.Column(db.Unicode)
    skill = db.Column(db.UnicodeText)
    reason = db.Column(db.UnicodeText)

    def __repr__(self):
        return '<name %r>' % self.name

