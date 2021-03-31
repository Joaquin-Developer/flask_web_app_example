
from flask import Flask, render_template, request, json, send_from_directory

app = Flask(__name__)

# @app.route('/', methods=['GET'])
# def hello_world():
#     return 'Hello, World!'

@app.route('/', methods=['GET'])
def send_page():
    # devolver un html
    return render_template("index.html")

@app.errorhandler(404)
def page_not_found(error):
    # return 'This page does not exist', 404
    return render_template("404errorPage.html")

@app.route('/public/<path:path>')
def send_css(path):
    return send_from_directory('public', path)

if __name__ == '__main__':
    app.run(port = 3000, debug = True)
