from flask import Blueprint, render_template, abort
from simpledu.models import User

user = Blueprint('user', __name__, url_prefix='/user')

@user.route('/<username>')
def user_index(username):
    users = User.query.all()
    for user in users:
        if username == user.username:
            return render_template('user.html', users=users)
        else:
            abort(404)
    

@user.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404
