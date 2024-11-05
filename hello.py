from flask import *

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def hello_world():
    if request.method == "POST":
        data = request.form.get('url')
        print(data)
        return render_template('main.html')
    else:
        return render_template('main.html')