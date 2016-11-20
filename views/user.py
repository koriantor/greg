from flask import Blueprint, render_template, g

from models import user

# The prefix is defined on registration in templates/__init__.py.
profile_blueprint = Blueprint('profile', __name__, url_prefix="/profile/<user_url_slug>")

@profile_blueprint.url_value_preprocessor
def get_profile_owner(endpoint, values):
    url_slug = values.pop('user_url_slug')
    # query is api for SQLalchemy
    #query = user.query.filter_by(url_slug=values.pop('user_url_slug'))
    #g.profile_owner = query.first_or_404()

@profile_blueprint.route('/')
def profile():
    # TODO: Read profile
    return render_template('user/profile.html')

@profile_blueprint.route('/participating')
def participating():
    # TODO: Read current profile
    return render_template('user/participating.html')

@profile_blueprint.route('/myevents')
def myevents():
    # TODO: Read current profile
    return render_template('user/myevents.html')
