from app.database_methods import task_list, add_notes
from app import app
from flask import render_template, redirect, url_for, flash, session
from app.forms import LoginForm, TaskForm
from app import login_manager
from app.models import User, Note
from flask_login import login_required, login_user, logout_user


@app.route('/home')
@login_required
def index():
    if 'id' in session:
        task_id = session['id']
        tasks = [x[1] for x in task_list(note_id=task_id)]
        return render_template('home.html', tasks=tasks)


@app.route('/', methods=['GET', 'POST'])
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            if user.password == form.password.data:
                login_user(user)
                session['id'] = str(user.id)
                return redirect(url_for('index'))
            else:
                flash('Wrong Password or Login')
        else:
            flash('User does not exist')
    return render_template('login.html', form=form)


@app.route('/add_task', methods=['GET', 'POST'])
@login_required
def add_task():
    form = TaskForm()
    if form.validate_on_submit():
        task = form.task.data
        if 'id' in session:
            id_note = session['id']
            add_notes(note_id=id_note, task_text=task)
    return render_template('add_task.html', form=form)


@app.route('/detailed_task')
@login_required
def detailed_task():
    if 'id' in session:
        id = session['id']
        note = Note.query.filter_by(note_id=id).all()
        return render_template('detailed_task.html', note=note)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Log out!')
    return redirect(url_for('login'))


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))



