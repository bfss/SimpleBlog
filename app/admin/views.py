from flask import render_template, flash, redirect, url_for
from . import admin
from ..models import User, Post
from app import db
from flask_login import login_required, login_user, current_user, logout_user
import bleach

@admin.route('/admin/post')
@login_required
def get_post():
    posts = Post.query.order_by(Post.timestamp.desc()).filter_by(is_deleted=False).all()
    return render_template('admin.html',posts = posts)

@admin.route('/admin/post/delete/<int:id>')
@login_required
def delete_post(id):
    """删除"""
    post = Post.query.get_or_404(id)
    post.is_deleted = True
    
    db.session.commit()
    posts = Post.query.order_by(Post.timestamp.desc()).filter_by(is_deleted=False).all()
    return render_template('admin.html',posts = posts)

