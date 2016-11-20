from flask import Blueprint, render_template, g

from models import item

# The prefix is defined on registration in templates/__init__.py.
item_blueprint = Blueprint('item', __name__, url_prefix="/item/<itemID>")

@item_blueprint.url_value_preprocessor
def get_profile_owner(endpoint, values):
    g.itemID = itemID
    pass
    # query is api for SQLalchemy
    #query = user.query.filter_by(url_slug=values.pop('user_url_slug'))
    #g.profile_owner = query.first_or_404()

@item_blueprint.route('/<item>')
def profile():
    return render_template('item/item.html')
