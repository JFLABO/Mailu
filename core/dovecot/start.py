#!/usr/bin/python

import jinja2
import os
import socket
import glob

# Actual startup script
os.environ["FRONT_ADDRESS"] = socket.gethostbyname("front")
if os.environ["WEBMAIL"] != "none":
    try:
	os.environ["WEBMAIL_ADDRESS"] = socket.gethostbyname("webmail")
    except:
        print("Error resolving webmail host, WEBMAIL_ADDRESS isn't set")

def convert(src, dst):
    print("Converting file ", src, " to ", dst)
    with open(dst, "w") as dst_file, open(src, "r") as src_file:
        template = src_file.read()
        config = jinja2.Template(template).render(**os.environ)
        dst_file.write(config)

confroot = "/conf"
for dirpath, dirs, files in os.walk(confroot):
    for f in files:
        filefullpath = os.path.join(dirpath, f)
        filerelpath = os.path.relpath(filefullpath, confroot)
        convert(filefullpath, os.path.join("/etc/dovecot", filerelpath))

# Run postfix
os.system("chown -R mail:mail /mail /var/lib/dovecot")
os.execv("/usr/sbin/dovecot", ["dovecot", "-c", "/etc/dovecot/dovecot.conf", "-F"])
