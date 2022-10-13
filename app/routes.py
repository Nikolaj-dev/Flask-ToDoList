from app.database_methods import task_list, add_notes, get_one_task
from app import app
from flask import render_template, redirect, url_for, flash, session
from app.forms import LoginForm, AddTaskForm
from app import login_manager
from app.models import User
from flask_login import login_required, login_user, logout_user


@app.route('/home')
@login_required
def index():
    if 'id' in session:
        task_id = session['id']
        tasks = task_list(note_id=task_id)
        return render_template('home.html', tasks=tasks, title='Homepage')


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
    return render_template('login.html', form=form, title='Log in')


@app.route('/add_task', methods=['GET', 'POST'])
@login_required
def add_task():
    form = AddTaskForm()
    if form.validate_on_submit():
        task = form.task.data
        if 'id' in session:
            id_note = session['id']
            add_notes(note_id=id_note, note_text=task)
    return render_template('add_task.html', form=form, title='Add a task')


@app.route('/detailed_task/<int:task_id>')
@login_required
def detailed_task(task_id):
    note = get_one_task(task_id)
    return render_template('detailed_task.html', note=note, title="Tasks's detailed view")


@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Log out!')
    return redirect(url_for('login'))


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
