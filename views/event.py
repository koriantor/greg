from flask import Blueprint, render_template, g

#from models import event

# The prefix is defined on registration in templates/__init__.py.
event_blueprint = Blueprint('event', __name__, url_prefix="/<eventID>")

@event_blueprint.url_value_preprocessor
def get_profile_owner(endpoint, values):
    g.eventID = values.pop('eventID')
    pass
    # query is api for SQLalchemy
    #query = user.query.filter_by(url_slug=values.pop('user_url_slug'))
    #g.profile_owner = query.first_or_404()

@event_blueprint.route('/')
def eventPage():
    eventID = g.eventID
    return render_template('event/event.html', eventID=eventID)
