from flask import Flask, request
from Manager.AndroidManager import AndroidManager

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route("/string_to_IOS", methods=['POST'])
def convert_string_to_IOS():
    """Converts basic string to IOS"""
    if request.method == 'POST':
        post_string = request.get_json()
        am = AndroidManager(post_string["message"])
        print(am.convert_to_iOS())
        return {"message": am.convert_to_iOS()}
    return ""


@app.route("/file_to_IOS", methods=['POST'])
def convert_file_to_IOS():
    """Converts entire file to IOS"""


@app.route("/", methods=['GET', 'POST'])
def home_page():
    """Home page"""
    return "Home page"


if __name__ == "__main__":
    # app.debug = True
    app.run(host='0.0.0.0')
