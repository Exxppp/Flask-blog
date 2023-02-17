from flask import render_template

from blog import app


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about/')
def about():
    return render_template('about.html')


@app.route('/blogs/<int:blog_id>')
def blogs(blog_id):
    return render_template('blogs.html', blog_id=blog_id)


@app.route('/register/', methods=['GET', 'POST'])
def register():
    return render_template('register.html')


@app.route('/login/', methods=['GET', 'POST'])
def login():
    return render_template('login.html')


@app.route('/logout/', methods=['GET', 'POST'])
def logout():
    return


@app.route('/write-blog/', methods=['GET', 'POST'])
def write_blog():
    return render_template('write-blog.html')


@app.route('/my-blogs/')
def my_blogs():
    return render_template('write-blog.html')


@app.route('/edit-blog/', methods=['GET', 'POST'])
def edit_blog():
    return render_template('edit-blog.html')


@app.route('/delete-blog/<int:blog_id>')
def delete_blog(blog_id):
    return
