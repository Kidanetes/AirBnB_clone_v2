#!/usr/bin/python3
"""using fabric to compress all files in
webstatic directory"""


from fabric.api import *
from os.path import exists

env.hosts = ['3.85.136.6', '18.209.152.171']


def do_deploy(archive_path):
    """deploy our compressed web_static to the
    my servers"""
    if not exists(archive_path):
        return False
    try:
        put(archive_path, "/tmp/")
        archive_name = archive_path.split("/")[-1].split(".")[0]
        unarchive_name = archive_path.split("/")[-1]
        run(f"sudo mkdir -p /data/web_static/releases/{archive_name}")
        run(f"sudo tar -xzf  /tmp/{unarchive_name} -C \
              /data/web_static/releases/{archive_name}/")
        run(f"sudo rm /tmp/{unarchive_name}")
        run(f"sudo mv  /data/web_static/releases/{archive_name}/web_static/* \
             /data/web_static/releases/{archive_name}")
        run(f"sudo rm -rf /data/web_static/releases/{archive_name}/web_static")
        run("sudo rm -rf /data/web_static/current")
        run(f"sudo ln -s /data/web_static/releases/{archive_name}/ \
             /data/web_static/current")
        return True
    except Exception:
        return False
