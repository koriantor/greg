from flask import Flask, render_template, send_from_directory, render_template_string
from views.profile import profile_blueprint
from views.item import item_blueprint
from views.event import event_blueprint

app = Flask(__name__)

# ============
#    ROUTES
# ============
app.register_blueprint(profile_blueprint, url_prefix='/profile/<profileID>')
app.register_blueprint(item_blueprint, url_prefix="/item/<itemID>")
app.register_blueprint(event_blueprint, url_prefix="/event/<eventID>")

@app.route('/')
def index():
    obj = "foo"
    return render_template('home/index.html')

@app.route('/login')
def login():
    return render_template('home/login.html')

@app.route('/about')
def about():
    return render_template('home/about.html')

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
