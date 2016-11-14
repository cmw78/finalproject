from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, IntegerField, SubmitField
from wtforms.validators import DataRequired

class SignupForm(FlaskForm):
  name = StringField('Name', validators=[DataRequired("Please enter your Name.")])
  netid = StringField('NetID', validators=[DataRequired("Please enter your NetID.")])
  submit = SubmitField('Sign up')

class LoginForm(FlaskForm):
  netid = StringField('Netid', validators=[DataRequired("Please enter your netid.")])
  submit = SubmitField("Sign in")

class FriendForm(FlaskForm):
	follow = BooleanField('Check To Follow')
	submit = SubmitField("Follow")

class ClassForm(FlaskForm):
	bookbag = BooleanField('Check To Bookbag')
	taking = BooleanField('Taking')
	submit = SubmitField("Submit")

class Taken2Form(FlaskForm):
  taken = BooleanField('Check to add to Taken')
  rating = IntegerField('Rating (-1, 0, or 1)')
  semester = StringField('Which semester did you take this course? (Please enter in form S16 for Spring 2016)')
  submit = SubmitField('Add to Taken')

class SearchClass(FlaskForm):
  subject = StringField('Search')
  submit = SubmitField('Search')

class DeleteForm(FlaskForm):
  remove = BooleanField('Remove course')
  submit = SubmitField('Submit')

class EditFormFactory:
  @staticmethod
  def form(sid, bookbag,taking,taken):
    class F(FlaskForm):
      @staticmethod
      def bookbag_field_name(index):
        return 'bookbag_{}'.format(index)
      def bookbag_fields(self):
        for i, b in enumerate(bookbag):
          yield b.courseid, getattr(self, F.bookbag_field_name(i))
      def get_bookbag(self):
        for b, field, in self.bookbag_fields():
          if field.data:
            yield b
      @staticmethod
      def taking_field_name(index):
        return 'taking_{}'.format(index)
      def taking_fields(self):
        for i, t in enumerate(taking):
          yield t.courseid, getattr(self, F.taking_field_name(i))
      def get_taking(self):
        for t, field, in self.taking_fields():
          if field.data:
            yield t
      @staticmethod
      def taken_field_name(index):
        return 'taken_{}'.format(index)
      def taken_fields(self):
        for i, t in enumerate(taken):
          yield t.courseid, getattr(self, F.taken_field_name(i))
      def get_taken(self):
        for t, field, in self.taken_fields():
          if field.data:
            yield t
    bookbagged = [b for b in bookbag]
    for i, b in enumerate(bookbag):
      field_name = F.bookbag_field_name(i)
      default = 'checked' if b.studentid == sid else None
      setattr(F, field_name, BooleanField(default=default))
    taking = [t for t in taking]
    for i, t in enumerate(taking):
      field_name = F.taking_field_name(i)
      default = 'checked' if t.studentid == sid else None
      setattr(F, field_name, BooleanField(default=default))
    taken = [t for t in taken]
    for i, t in enumerate(taken):
      field_name = F.taken_field_name(i)
      default = 'checked' if t.studentid == sid else None
      setattr(F, field_name, BooleanField(default=default))
    return F()



