from flask import *
import subprocess

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def hello_world():
    if request.method == "POST":
        link = request.form.get('url')
        cmd = f"yt-dlp {link} -q --list-formats |grep mp4 |tail -n 1| cut -c1-3"
        format = subprocess.check_output(cmd, shell=True, text="Text")
        cmd = f"yt-dlp {link} -f {format}"
        subprocess.run(cmd, shell=True)
        return render_template('main.html')
    else:
        return render_template('main.html')