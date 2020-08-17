<h1 align="center">gotify-dunst</h1>

## Intro
This is a simple script for receiving [Gotify](https://github.com/gotify/server) messages on a Linux Desktop via [dunst](https://dunst-project.org/).

## Features

* receive messages via WebSocket
* display it via dust (notify-send)
* multiple priorities adopted from Gotify
* automatic fetch of your application Images

## Installation

1. Clone this repo
<code>git clone https://github.com/ztpnk/gotify-dunst && cd gotify-dunst</code>
2. Install python requirements
<code>./.env/bin/pip install -r requirements.txt</code>
3. Change the domain and token in main.py
4. Test if it runs
<code>./.env/bin/python main.py</code>
5. Customize the gotify-dunst.service and copy it to /etc/systemd/system
6. Start and enable the Systemd Unit
<code>sudo systemd start gotify-dunst && sudo systemd enable gotify-dunst</code>
