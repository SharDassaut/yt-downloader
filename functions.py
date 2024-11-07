import subprocess

def urlCheck(url):
    if(url.startswith("http://youtu.be/") or url.startswith("https://youtu.be/")):
        return True
    return False

def download(link):
        if urlCheck(link):
            cmd = f"yt-dlp {link} -f 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4'"
            subprocess.run(cmd, shell=True)
            return 0
        else:
            return 1

download("https://youtu.be/BvulBSnAyg0?si=YQdeCYV76xVoBUhh")