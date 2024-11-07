from flask import *
from functions import download,urlCheck


app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def hello_world():
    if request.method == "POST":
        link = request.form.get('url')
        return_value = download(link)
        if return_value == 0:
            return "Video descargado"
        else:
            return "Video no descargado"
    else:
        return render_template('main.html')

if __name__ == "__main__":
    app.run(debug=True)