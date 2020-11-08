<h1 align="center">gotify-dunst</h1>

## Intro

This is a simple script for receiving [Gotify](https://github.com/gotify/server) messages on a Linux Desktop via [dunst](https://dunst-project.org/).

## Features

* receive messages via WebSocket
* display it via dust (notify-send)
* multiple priorities adopted from Gotify
* automatic fetch of your application Images

## Installation

### Debian (Ubuntu, Mint, etc.)

```bash
sudo apt install git make libnotify-bin python3-websocket
git clone https://github.com/ztpnk/gotify-dunst
cd gotify-dunst
sudo make install
```

### Arch (Manjaro)

```bash
yay -S gotify-dunst-git
```

## Usage

1. Run `systemctl --user enable --now gotify-dunst.service` (**no sudo**)
2. Open `~/.config/gotify-dunst/gotify-dunst.conf` in your favorite text editor. Modify the domain to your instance of Gotify and modify the token to a client token you get from the Gotify web app.
3. Run `systemctl --user restart gotify-dunst.service`.
4. (optionally) You can check the status of the service with `systemctl --user status gotify-dunst.service`.
