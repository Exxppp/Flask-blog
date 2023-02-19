from flask import render_template, flash, redirect, url_for
from flask_login import logout_user, login_required, login_user, current_user
from sqlalchemy import or_
from werkzeug.security import generate_password_hash, check_password_hash

from blog import app, db, login_manager
from forms import UserRegistrationForm, UserLoginForm, WriteBlogForm
from models import User, Blog


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route('/')
def index():
    blogs = db.session.query(Blog.title, Blog.body, Blog.timestamp, User.first_name, User.last_name, Blog.id) \
        .join(User).order_by(Blog.timestamp.desc()).all()
    return render_template('index.html', blogs=blogs)


@app.route('/about/')
def about():
    return render_template('about.html')


@app.route('/register/', methods=['GET', 'POST'])
def register():
    form = UserRegistrationForm()

    if form.validate_on_submit():

        if db.session.query(User).filter(or_(User.email == form.email.data, User.username == form.username.data)).all():
            flash('Username or Email address already exists')
        else:
            u = User(first_name=form.first_name.data, last_name=form.last_name.data,  # type: ignore
                     username=form.username.data, email=form.email.data,  # type: ignore
                     password=generate_password_hash(form.password.data))  # type: ignore
            db.session.add(u)
            db.session.commit()
            flash('Register is success')
            return redirect(url_for('login'))

    return render_template('register.html', form=form)


@app.route('/login/', methods=['GET', 'POST'])
def login():
    form = UserLoginForm()
    if form.validate_on_submit():
        user = db.session.query(User).filter(User.username == form.username.data).first()
        if check_password_hash(user.password, form.password.data):
            login_user(user, remember=True)
            return redirect(url_for('index'))
        else:
            flash('Username or password is invalid')

    return render_template('login.html', form=form)


@app.route('/logout/', methods=['GET', 'POST'])
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/blog/<int:blog_id>')
def blog(blog_id):
    blog_data = db.session.query(Blog, User).filter(Blog.id == blog_id).join(User).first()
    return render_template('blog.html', blog=blog_data)


@app.route('/write-blog/', methods=['GET', 'POST'])
@login_required
def write_blog():
    form = WriteBlogForm()
    if form.validate_on_submit():
        blog = Blog(title=form.title.data, body=form.body.data, user=current_user.id)
        db.session.add(blog)
        db.session.commit()
        flash('Your blog is successfully posted.')
        return redirect(url_for('index'))
    return render_template('write-blog.html', form=form)


@app.route('/my-blogs/')
@login_required
def my_blogs():
    blogs = db.session.query(Blog.title, Blog.body, Blog.timestamp, User.first_name, User.last_name, Blog.id) \
        .join(User).filter(User.id == current_user.id).order_by(Blog.timestamp.desc()).all()
    return render_template('my-blogs.html', blogs=blogs)


@app.route('/edit-blog/<int:blog_id>', methods=['GET', 'POST'])
def edit_blog(blog_id):
    blog = db.session.query(Blog).filter(Blog.id == blog_id, Blog.user == current_user.id).first()
    if not blog:
        flash("You don't have access")
        return redirect(url_for('my_blogs'))
    form = WriteBlogForm(title=blog.title, body=blog.body)
    if form.validate_on_submit():
        blog.title = form.title.data
        blog.body = form.body.data
        db.session.commit()
        flash('Your blog is successfully updated.')
        return redirect(url_for('index'))
    return render_template('edit-blog.html', blog=blog, form=form)


@app.route('/delete-blog/<int:blog_id>')
def delete_blog(blog_id):
    blog = db.session.query(Blog).filter(Blog.id == blog_id, Blog.user == current_user.id).first()
    if blog:
        db.session.delete(blog)
        db.session.commit()
    else:
        flash("You don't have access")
    return redirect(url_for('my_blogs'))
