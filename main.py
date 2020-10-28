import websocket
from urllib.request import urlopen
import json
import subprocess
import os.path

domain = "push.example.com"
token = "z2Uny92TZBzsukg"

home = os.path.expanduser('~')
path = "{}/.cache/gotify-dunst".format(home)
if not os.path.isdir(path):
    os.mkdir(path)

def get_picture(appid):
    imgPath = "{}/{}.jpg".format(path, appid)
    if os.path.isfile(path):
        return imgPath
    else:
        r = json.loads(urlopen("https://{}/application?token={}".format(domain, token)).read())
        for i in r:
            if i['id'] == appid:
                with open(imgPath, "wb") as f:
                    url = urlopen("https://{}/{}?token={}".format(domain, i['image'], token))
                    f.write(url.read())
        return imgPath

def send_notification(message):
    m = json.loads(message)
    if 1 <= m['priority'] <= 3:
        subprocess.Popen(['notify-send', m['title'], m['message'], "-u", "low", "-i", get_picture(m['appid'])])
    if 4 <= m['priority'] <= 7:
        subprocess.Popen(['notify-send', m['title'], m['message'], "-u", "normal", "-i", get_picture(m['appid'])])
    if m['priority'] > 7:
        subprocess.Popen(['notify-send', m['title'], m['message'], "-u", "critical", "-i", get_picture(m['appid'])])

def on_message(ws, message):
    print(message)
    send_notification(message)

def on_error(ws, error):
    print(error)

def on_close(ws):
    print("### closed ###")

if __name__ == "__main__":
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp("wss://{}/stream?token={}".format(domain, token),
                              on_message = on_message,
                              on_error = on_error,
                              on_close = on_close)
    ws.run_forever()
