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