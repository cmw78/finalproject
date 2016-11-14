from sqlalchemy import sql, orm
from app import db

class Student(db.Model):
  __tablename__= 'student'
  id = db.Column('id', db.String(256), primary_key = True)
  name = db.Column('name', db.String(256))
  taken = orm.relationship('Taken')
  taking = orm.relationship('Taking')
  Bookbag = orm.relationship('Bookbag')
  IsFriendsWith = orm.relationship('IsFriendsWith')
  @staticmethod
  def edit(id,name):
    try:
      db.session.execute('INSERT INTO student VALUES(:id, :name)', dict(id=id, name=name))
      db.session.commit()
    except Exception as e:
      db.session.rollback()
      raise e
  @staticmethod
  def addFriend(yourid,friendid):
    try:
      db.session.execute('INSERT INTO isfriendswith VALUES(:yourid, :friendid)', dict(yourid=yourid, friendid=friendid))
      db.session.commit()
    except Exception as e:
      db.session.rollback()
      raise e
  @staticmethod
  def info(studentid, bookbagged,taking,taken):
    try:
      print "BOB"
      print studentid
      db.session.execute('DELETE FROM bookbag WHERE studentid = :studentid', dict(studentid=studentid))
      db.session.execute('DELETE FROM taking WHERE studentid = :studentid', dict(studentid=studentid))
      db.session.execute('DELETE FROM taken WHERE studentid = :studentid', dict(studentid=studentid))
      # for courseid in bookbagged:
      #   db.session.execute('INSERT INTO bookbag VALUES(:courseid, :studentid)', dict(studentid=studentid, courseid=courseid))
      # for courseid in taking:
      #   db.session.execute('INSERT INTO taking VALUES(:courseid, :studentid)', dict(studentid=studentid, courseid=courseid))
      # for courseid in taken:
      #   db.session.execute('INSERT INTO taken VALUES(:courseid, :studentid)', dict(studentid=studentid, courseid=courseid))
      db.session.commit()
    except Exception as e:
      db.session.rollback()
      raise e
class Professor(db.Model):
  __tablename__= 'professor'
  id = db.Column('id', db.String(256), primary_key = True)
  name = db.Column('name', db.String(256))
  teaches = orm.relationship('Teaches')

class Course(db.Model):
  __tablename__ = 'course'
  id = db.Column('id', db.String(256), primary_key = True)
  name = db.Column('name', db.String(256))

class Bookbag(db.Model):
  __tablename__ = 'bookbag'
  courseid = db.Column('courseid', db.String(256), db.ForeignKey('course.id'), primary_key = True)
  studentid = db.Column('studentid', db.String(256), db.ForeignKey('student.id'), primary_key = True)
  @staticmethod
  def bookbag(courseid, sid):
    try:
      db.session.execute('INSERT INTO bookbag VALUES(:courseid, :sid)', dict(courseid=courseid, sid=sid))
      db.session.commit()
    except Exception as e:
      db.session.rollback()
      raise e

class Taken(db.Model):
  __tablename__ = 'taken'
  courseid = db.Column('courseid', db.String(256), db.ForeignKey('course.id'), primary_key = True)
  studentid = db.Column('studentid', db.String(256), db.ForeignKey('student.id'), primary_key = True)
  rating = db.Column('rating', db.Integer())
  semester = db.Column('semester', db.String(256), primary_key = True)
  @staticmethod
  def taken(courseid, sid,rating, semester):
    try:
      db.session.execute('INSERT INTO taken VALUES(:courseid, :sid, :rating, :semester)', dict(courseid=courseid, sid=sid, rating=rating, semester=semester))
      db.session.commit()
    except Exception as e:
      db.session.rollback()
      raise e

class Taking(db.Model):
  __tablename__ = 'taking'
  courseid = db.Column('courseid', db.String(256), db.ForeignKey('course.id'), primary_key = True)
  studentid = db.Column('studentid', db.String(256), db.ForeignKey('student.id'), primary_key = True)
  @staticmethod
  def taking(courseid, sid):
    try:
      db.session.execute('INSERT INTO taking VALUES(:courseid, :sid)', dict(courseid=courseid, sid=sid))
      db.session.commit()
    except Exception as e:
      db.session.rollback()
      raise e


class IsFriendsWith(db.Model):
  __tablename__= 'isfriendswith'
  id1 = db.Column('id1', db.String(256), db.ForeignKey('student.id'), primary_key = True)
  id2 = db.Column('id2', db.String(256), primary_key = True)

class Teaches(db.Model):
  __tablename__ = 'teaches'
  courseid = db.Column('courseid',db.String(256), db.ForeignKey('course.id'), primary_key = True)
  profid = db.Column('profid', db.String(256), db.ForeignKey('professor.id'),primary_key = True )
  semester = db.Column('semester', db.String(256), primary_key = True)




