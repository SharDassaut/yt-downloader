import subprocess

def urlCheck(url):
    if(url.startswith("http://youtu.be/") or url.startswith("https://youtu.be/")):
        return True
    return False

def download(link):
        if urlCheck(link):
            cmd = f"yt-dlp {link} -q --list-formats |grep mp4 |tail -n 1| cut -c1-3"
            format = subprocess.check_output(cmd, shell=True, text="Text")
            cmd = f"yt-dlp {link} -f {format}"
            subprocess.run(cmd, shell=True)
            return 0
        else:
            return 1