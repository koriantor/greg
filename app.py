from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

# ============
#    ROUTES
# ============
@app.route('/')
def hello_world():
    return send_from_directory('templates', 'default.html')

@app.route('/<user>/')
def showUser():
    pass    # TODO: return user page

@app.route('/<user>/<event>')
def showEvent():
    pass    # TODO: return event page

@app.route('/login')
def showLogin():
    return "login" #TODO: return login page

@app.route('/about')
def showAbout():
    pass        #TODO: return about page

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