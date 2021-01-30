from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello_world():
    return 'Hello, World!'

@app.route('/inicio', methods=['GET'])
def send_page():
    # devolver un html
    return render_template("index.html")

@app.errorhandler(404)
def page_not_found(error):
    # return 'This page does not exist', 404
    return render_template("404errorPage.html")


if __name__ == '__main__':
    app.run(port = 3000, debug = True)
