from flask import Flask, render_template, redirect, url_for, session, request
from flask_sqlalchemy import SQLAlchemy
import models
import forms
from forms import SignupForm, LoginForm, FriendForm, ClassForm, Taken2Form, SearchClass, DeleteForm, EditFormFactory

app = Flask(__name__)
app.secret_key = 's3cr3t'
app.config.from_object('config')
db = SQLAlchemy(app, session_options={'autocommit': False})

@app.route('/edit-info')
def edit_student():
    studentid = session['netid']
    student = db.session.query(models.Student)\
        .filter(models.Student.id==studentid)
    bookbag = db.session.query(models.Bookbag)\
        .filter(models.Bookbag.studentid ==studentid).all()
    taking = db.session.query(models.Taking)\
        .filter(models.Taking.studentid ==studentid).all()
    taken = db.session.query(models.Taken)\
        .filter(models.Taken.studentid ==studentid).all()
    form = forms.EditFormFactory.form(studentid,bookbag,taking,taken)
    print "LOOK"
    if form.validate_on_submit():
        try:
            form.errors.pop('database', None)
            models.Student.info(studentid, form.get_bookbag(), form.get_taking(), form.get_taken())
            return redirect(url_for('student', id=studentid))
        except BaseException as e:
            form.errors['database'] = str(e)
            return render_template('edit-drinker.html',student=student, form=form)
    else:
        return render_template('edit-drinker.html', student=student,form=form)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home')
def home():
    if 'netid' in session:
        id = session['netid']
        return render_template('home.html', id=id)

@app.route('/courses', methods=["GET", "POST"])
def all_courses():
    form3 = SearchClass()
    courses = db.session.query(models.Course).all()
    if request.method == "POST":
        if form3.validate()==False:
            return render_template('all-courses.html', courses=courses, form3=form3)
        else:
            search = form3.subject.data.upper()
            st = "%"+search+"%"
            sub = db.session.query(models.Course)\
                .filter(models.Course.id.like(st)).all()
            return render_template('subject.html', sub=sub)
    else:
        return render_template('all-courses.html', courses=courses, form3=form3)
@app.route('/students',methods=["GET", "POST"])
def all_students():
    form3 = SearchClass()
    students = db.session.query(models.Student).all()
    if request.method == "POST":
        if form3.validate()==False:
            return render_templates('all-students.html', students=students, form3=form3)
        else:
            search = form3.subject.data
            st = "%"+search+"%"
            sub = db.session.query(models.Student)\
                .filter(models.Student.name.like(st)).all()
            return render_template('search-student.html', sub=sub)
    return render_template('all-students.html', students=students, form3 = form3)

@app.route('/course/<id>', methods=["GET", "POST"])
def course(id):
    form = ClassForm()
    form2= Taken2Form()
    form3 = SearchClass()
    courses = db.session.query(models.Course).all()
    course = db.session.query(models.Course)\
        .filter(models.Course.id== id).one()
    if request.method == "POST":
        if form.validate()==False:
            return render_template('course.html', course=course, form=form, form2=form2)
        else:
            curid = session['netid']
            if form.bookbag.data == True:
                models.Bookbag.bookbag(id,curid)
            if form.taking.data ==True:
                models.Taking.taking(id,curid)
        if form2.validate()==False:
            return render_template('course.html', course=course, form=form, form2=form2)
        else:
            if form2.taken.data == True:
                models.Taken.taken(id, curid, form2.rating.data,form2.semester.data)
            return render_template('all-courses.html', courses=courses, form3=form3)

    return render_template('course.html', course=course, form=form,form2=form2)


@app.route('/myinfo/<id>')
def my_info(id):
    return render_template('my-info.html', id=id)
@app.route('/student/<id>',methods=["GET", "POST"])
def student(id):
    form = FriendForm()
    form3 = SearchClass()
    students = db.session.query(models.Student).all()

    student = db.session.query(models.Student)\
            .filter(models.Student.id== id).one()
    if request.method =="POST":
        if form.validate()==False:
            print "FALSE"
            return render_template('student.html', student=student, form=form)
        else:
            print "HELLO"
            if form.follow.data == True:
                print "YAY"
                curid= session['netid']
                models.Student.addFriend(curid,id)
            print str(form.follow.data)
            return render_template('all-students.html', students=students,form3=form3)
    print "YOYO"
    print str(form.follow.data)
    return render_template('student.html', student=student,form=form)
# @app.route('/takeninfo/<id>', methods=["GET", "POST"])
# def taken_info(id, cid):
#     form = Taken2Form()
#     students = db.session.query(models.Student).all()
#     student = db.session.query(models.Student)\
#             .filter(models.Student.id== id).one()
#     if request.method == "POST":
#         if form.validate() == False:
#             return render_template('taken-page.html', id=id, form=form)
#         else:
#             curid = session['netid']
#             models.Taken.taken(id, curid, form.rating.data,form.semester.data)
#             return render_template('all-students.html', students=students, form=form)
#     return render_template('taken-page.html', id=id, form=form)
@app.route('/signup', methods=["GET", "POST"])
def signup():

    form = SignupForm()

    if request.method == "POST":
        if form.validate() == False:
            return render_template('signup.html', form=form)
        else:
            models.Student.edit(form.netid.data,form.name.data)
            session['netid'] = form.netid.data
            return render_template('home.html')

    elif request.method == "GET":
        return render_template('signup.html', form=form)
@app.route('/professors')
def all_professors():
    professors = db.session.query(models.Professor).all()
    return render_template('all-professors.html', professors=professors)

@app.route('/professor/<id>')
def professor(id):
    professor = db.session.query(models.Professor)\
        .filter(models.Professor.id== id).one()
    return render_template('professor.html', professor=professor)

@app.route('/friends')
def friends():
    id = session['netid']
    friends = db.session.query(models.IsFriendsWith)\
        .filter(models.IsFriendsWith.id1==id).all()
    return render_template('friends.html', friends=friends)


@app.route('/bookbag/<name>')
def bookbag(name):
    bookbag = db.session.query(models.Bookbag)\
        .filter(models.Bookbag.studentid==name).all()
    return render_template('bookbag.html', bookbag=bookbag)

@app.route('/taking/<name>')
def taking(name):
    taking = db.session.query(models.Taking)\
        .filter(models.Taking.studentid==name).all()
    return render_template('taking.html', taking=taking)

@app.route('/taken/<name>')
def taken(name):
    taken = db.session.query(models.Taken)\
        .filter(models.Taken.studentid==name).all()
    return render_template('taken.html', taken=taken)
@app.route('/teaches/<name>')
def teaches(name):
    teaches = db.session.query(models.Teaches)\
        .filter(models.Teaches.profid==name).all()
    return render_template('teaches.html', teaches=teaches)


@app.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()

    if request.method == "POST":
        if form.validate()== False:
            return render_template('login.html', form=form)
        else:
            id = form.netid.data 
            user = db.session.query(models.Student)\
                .filter(models.Student.id==id).first()
            if user is not None:
                session['netid'] = id
                return redirect(url_for('home'))

            else:
                return redirect(url_for('login'))


    elif request.method == 'GET':
        return render_template('login.html', form=form)
@app.route("/logout")
def logout():
  session.pop('email', None)
  return redirect(url_for('index'))

# @app.route('/edit-drinker/<name>', methods=['GET', 'POST'])
# def edit_drinker(name):
#     drinker = db.session.query(models.Drinker)\
#         .filter(models.Drinker.name == name).one()
#     beers = db.session.query(models.Beer).all()
#     bars = db.session.query(models.Bar).all()
#     form = forms.DrinkerEditFormFactory.form(drinker, beers, bars)
#     if form.validate_on_submit():
#         try:
#             form.errors.pop('database', None)
#             models.Drinker.edit(name, form.name.data, form.address.data,
#                                 form.get_beers_liked(), form.get_bars_frequented())
#             return redirect(url_for('drinker', name=form.name.data))
#         except BaseException as e:
#             form.errors['database'] = str(e)
#             return render_template('edit-drinker.html', drinker=drinker, form=form)
#     else:
#         return render_template('edit-drinker.html', drinker=drinker, form=form)

@app.template_filter('pluralize')
def pluralize(number, singular='', plural='s'):
    return singular if number in (0, 1) else plural

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
