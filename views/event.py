from flask import Blueprint, render_template, g

from models import event

# The prefix is defined on registration in templates/__init__.py.
event_blueprint = Blueprint('event', __name__, url_prefix="/<user_url_slug>")

@event_blueprint.url_value_preprocessor
def get_profile_owner(endpoint, values):
    x = values.pop('user_url_slug')
    pass
    # query is api for SQLalchemy
    #query = user.query.filter_by(url_slug=values.pop('user_url_slug'))
    #g.profile_owner = query.first_or_404()

@event_blueprint.route('/')
def eventPage():
    return render_template('home/event.html')
