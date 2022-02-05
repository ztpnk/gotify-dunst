import websocket
from urllib.request import urlopen, Request
import json
import subprocess
import os.path
import configparser

try:
    import setproctitle
    setproctitle.setproctitle("gotify-dunst")
except:
    pass

home = os.path.expanduser('~')
configpath = home+'/.config/gotify-dunst/gotify-dunst.conf'

if not os.path.isfile(configpath):
    from shutil import copyfile
    from os import makedirs
    makedirs(home+'/.config/gotify-dunst/',exist_ok=True)
    copyfile('gotify-dunst.conf',configpath)

config = configparser.ConfigParser()
config.read(configpath)

domain = config.get('server','domain',fallback=None)

if domain in [ "push.example.com", None]:
    print("Confiuration error. Make sure you have properly modified the configuration")
    exit()

token = config.get('server','token')

ssl = "true" == config.get('server','ssl', fallback='false').lower()

path = "{}/.cache/gotify-dunst".format(home)
if not os.path.isdir(path):
    os.mkdir(path)

def get_picture(appid):
    imgPath = "{}/{}.jpg".format(path, appid)
    if os.path.isfile(path):
        return imgPath
    else:
        if ssl:
            protocol = 'https'
        else:
            protocol = 'http'

        req = Request("{}://{}/application?token={}".format(protocol, domain, token))
        req.add_header("User-Agent", "Mozilla/5.0")
        r = json.loads(urlopen(req).read())
        for i in r:
            if i['id'] == appid:
                with open(imgPath, "wb") as f:
                    req = Request("{}://{}/{}?token={}".format(protocol, domain, i['image'], token))
                    req.add_header("User-Agent", "Mozilla/5.0")
                    f.write(urlopen(req).read())
        return imgPath

def send_notification(message):
    m = json.loads(message)
    if m['priority'] <= 3:
        subprocess.Popen(['notify-send', m['title'], m['message'], "-u", "low", "-i", get_picture(m['appid']), "-a", "Gotify", "-h", "string:desktop-entry:gotify-dunst"])
    if 4 <= m['priority'] <= 7:
        subprocess.Popen(['notify-send', m['title'], m['message'], "-u", "normal", "-i", get_picture(m['appid']), "-a", "Gotify", "-h", "string:desktop-entry:gotify-dunst"])
    if m['priority'] > 7:
        subprocess.Popen(['notify-send', m['title'], m['message'], "-u", "critical", "-i", get_picture(m['appid']), "-a", "Gotify", "-h", "string:desktop-entry:gotify-dunst"])

def on_message(ws, message):
    print(message)
    send_notification(message)

def on_error(ws, error):
    print(error)

def on_close(ws):
    print("### closed ###")

if __name__ == "__main__":
    websocket.enableTrace(True)
    if ssl:
        protocol = 'wss'
    else:
        protocol = 'ws'

    ws = websocket.WebSocketApp("{}://{}/stream?token={}".format(protocol, domain, token),
                              on_message = on_message,
                              on_error = on_error,
                              on_close = on_close)
    ws.run_forever()
