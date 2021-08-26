ifeq ($(PREFIX),)
    PREFIX := /usr
endif

install:
	# systemd file
	install -d $(DESTDIR)$(PREFIX)/lib/systemd/user/
	install gotify-dunst.service $(DESTDIR)$(PREFIX)/lib/systemd/user/

	# files in /usr/lib
	install -d $(DESTDIR)$(PREFIX)/lib/gotify-dunst/
	install main.py $(DESTDIR)$(PREFIX)/lib/gotify-dunst/
	install gotify-dunst.conf $(DESTDIR)$(PREFIX)/lib/gotify-dunst/

	# files in /usr/share
	install gotify-dunst.desktop $(DESTDIR)$(PREFIX)/share/applications
	install gotify-16.png $(DESTDIR)$(PREFIX)/share/icons/hicolor/16x16/apps/gotify.png
	install gotify-32.png $(DESTDIR)$(PREFIX)/share/icons/hicolor/32x32/apps/gotify.png
	install gotify-96.png $(DESTDIR)$(PREFIX)/share/icons/hicolor/96x96/apps/gotify.png
	install gotify-128.png $(DESTDIR)$(PREFIX)/share/icons/hicolor/128x128/apps/gotify.png