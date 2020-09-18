from flask import render_template, flash, redirect, url_for, request, Markup
from . import main
from .forms import RegisterForm, LoginForm, PostForm
from ..models import User, Post
from app import db
from flask_login import login_required, login_user, current_user, logout_user
import bleach

@main.route('/')
def index():
    posts = Post.query.order_by(Post.timestamp.desc()).filter_by(is_deleted=False).all()
    return render_template('index.html',posts = posts)

@main.route('/register',methods=['GET','POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        if User.query.limit(1).all():
            flash('不开放注册')
            return render_template('register.html',form = form)
        username = form.username.data
        password = form.password.data
        email = form.email.data
        introduce  = form.introduce.data
        user = User(username=username,password=password,email=email,introduce=introduce)
        db.session.add(user)
        db.session.commit()
        flash("注册成功")
        return redirect(url_for('.index'))
    return render_template('register.html',form = form)

@main.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username = form.username.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user)
            return redirect(url_for('.index'))
        else:
            flash('用户名或密码错误')
    return render_template('login.html',form = form)

@main.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect('login')

@main.route('/post', methods = ['GET', 'POST'])
@login_required
def post():
    form  = PostForm()
    if form.validate_on_submit():
        post = Post(title = form.title.data, body = form.content.data, author_id = current_user)
        db.session.add(post)
        db.session.commit()
        
        flash("发布成功","success")
        return redirect(url_for('.get_post',id=post.id))
    return render_template('submit_post.html',form = form)

@main.route('/post/<int:id>')
def get_post(id):
    post = Post.query.get_or_404(id)
    post.body = Markup(post.body)
    return render_template('post.html',post = post)
