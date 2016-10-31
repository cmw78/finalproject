from sqlalchemy import sql, orm
from app import db

class SchoolMember(db.Model):
	__tablename__ = 'schoolmember'
	id = db.Column('id', db.String(256), primary_key = True)
	name = db.Column('name', db.String(256))

class Student(db.Model):
	__tablename__= 'student'
	id = db.Column('id', db.String(256), db.ForeignKey('drinker.id'), primary_key = True)
	name = db.Column('name', db.String(256))

class Professor(db.Model):
	__tablename__= 'professor'
	id = db.Column('id', db.String(256), db.ForeignKey('drinker.id'), primary_key = True)
	name = db.Column('name', db.String(256))

class Course(db.Model):
	__tablename__ = 'course'
	id = db.Column('id', db.String(256), primary_key = True)
	name = db.Column('name', db.String(256))

class Bookbag(db.Model):
	__tablename__ = 'bookbag'
	course = db.Column('course', db.String(256), db.ForeignKey('course.id'), primary_key = True)
	student = db.Column('student', db.String(256), db.ForeignKey('student.id'), primary_key = True)

class Taken(db.Model):
	__tablename__ = 'taken'
	course = db.Column('course', db.String(256), db.ForeignKey('course.id'), primary_key = True)
	student = db.Column('student', db.String(256), db.ForeignKey('student.id'), primary_key = True)
	rating = db.Column('rating', db.Integer())
	semester = db.Column('semester', db.String(256), primary_key = True)

class Taking(db.Model):
	__tablename__ = 'taking'
	course = db.Column('course', db.String(256), db.ForeignKey('course.id'), primary_key = True)
	student = db.Column('student', db.String(256), db.ForeignKey('student.id'), primary_key = True)
	semester = db.Column('semester', db.String(256), primary_key = True)


class IsFriendsWith(db.Model):
	__tablename__= 'isfriendswith'
	id1 = db.Column('id1', db.String(256), db.ForeignKey('drinker.id'), primary_key = True)
	id2 = db.Column('id2', db.String(256), db.ForeignKey('drinker.id'), primary_key = True)

class Teaches(db.Model):
	__tablename__ = 'teaches'
	courseid = db.Column('courseid',db.String(256), db.ForeignKey('course.id'), primary_key = True)
	profid = db.Column('profid', db.String(256), db.ForeignKey('professor.id'),primary_key = True  )
	semester = db.Column('semester', db.String(256), primary_key = True)



