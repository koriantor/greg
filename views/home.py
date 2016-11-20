from flask import Blueprint, render_template, g

# The prefix is defined on registration in templates/__init__.py.
home_blueprint = Blueprint('home', __name__, url_prefix="/<user_url_slug>")

@home_blueprint.url_value_preprocessor
def get_profile_owner(endpoint, values):
    x = values.pop('user_url_slug')
    pass
    # query is api for SQLalchemy
    #query = user.query.filter_by(url_slug=values.pop('user_url_slug'))
    #g.profile_owner = query.first_or_404()

@home_blueprint.route('/')
def profile():
    return render_template('home/index.html')

@home_blueprint.route('/about')
def participating():
    return render_template('home/about.html')

@home_blueprint.route('/login')
def myevents():
    return render_template('home/login.html')
