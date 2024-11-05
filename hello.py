from flask import *
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def hello_world():
    if request.method == "POST":
        link = request.form.get('url')
        cmd = f"yt-dlp {link}"
        os.system(cmd)  
        return render_template('main.html')
    else:
        return render_template('main.html')