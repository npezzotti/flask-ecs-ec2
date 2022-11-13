from flask import Blueprint, redirect, render_template, request, url_for

from app import db
from .models import Post

bp = Blueprint(
    'posts',
    __name__,
    url_prefix='/posts',
    template_folder='templates'
)

@bp.route('/', methods=['GET'])
def get_posts():
    posts = Post.query.all()
    return render_template('posts/post_list.html', posts=posts)

@bp.route('/<int:id>/', methods=['GET'])
def get_post(id):
    post = Post.query.get_or_404(id)
    return render_template('posts/post_detail.html', post=post)

@bp.route('/create/', methods=['POST'])
def create_post():
    post = Post(
        title=request.form['title'],
        content=request.form['content']
    )

    db.session.save(post)
    db.session.commit()
    return redirect

@bp.route('/update/<int:id>/', methods=['POST'])
def update_post(id):
    post = Post.query.get_or_404(id)
    post.title = request.form['title']
    post.content = request.form['content']

@bp.route('/delete/<int:id>/', methods=['GET'])
def delete_post(id):
    post = Post.query.get_or_404(id)
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for('posts.get_posts'))
