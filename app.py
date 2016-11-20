from flask import Flask, render_template, send_from_directory, render_template_string
from views.user import profile_blueprint
from views.item import item_blueprint
from views.home import home_blueprint
from views.event import event_blueprint

app = Flask(__name__)

# ============
#    ROUTES
# ============
app.register_blueprint(profile_blueprint, url_prefix='/profile/<user_url_slug>')
app.register_blueprint(item_blueprint, url_prefix="/item")
app.register_blueprint(home_blueprint, url_prefix="/<user_url_slug>")
app.register_blueprint(event_blueprint, url_prefix="/<user_url_slug>")

# @app.route('/')
# def hello_world():
#     obj = "foo"
#     return render_template('layout.html', obj=obj)

@app.route('/js/<path:path>')
def sendJS(path):
    return send_from_directory('static/js', path)

@app.route('/css/<path:path>')
def sendCSS(path):
    return send_from_directory('static/css', path)

@app.route('/img/<path:path>')
def sendImgs(path):
    return send_from_directory('static/imgs', path)

@app.route('/templates/<path:path>')
def sendTemplate(path):
    return send_from_directory('templates', path)

# ==========
#    main
# ==========
if __name__ == '__main__':
    app.run(debug=True)
