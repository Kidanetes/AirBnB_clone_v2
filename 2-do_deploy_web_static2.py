#!/usr/bin/python3
"""using fabric to compress all files in
webstatic directory"""


from fabric.api import *
from os.path import exists

env.hosts = ['52.86.189.212', '52.201.146.212']


def do_deploy(archive_path):
    """deploy our compressed web_static to the
    my servers"""
    if not exists(archive_path):
        return False
    try:
        put(archive_path, "/tmp/")
        archive_name = archive_path.split("/")[-1].split(".")[0]
        unarchive_name = archive_path.split("/")[-1]
        run(f"mkdir -p /data/web_static/releases/{archive_name}")
        run(f"tar -xzf  /tmp/{unarchive_name} -C \
              /data/web_static/releases/{archive_name}/")
        run(f"rm /tmp/{unarchive_name}")
        run(f"mv -r /data/web_static/releases/{archive_name}/web_static/* \
             /data/web_static/releases/{archive_name}")
        run(f"rm -rf /data/web_static/releases/{archive_name}/web_static")
        run("rm -rf /data/web_static/current")
        run(f"ln -s /data/web_static/releases/{archive_name} \
             /data/web_static/current")
        return True
    except Exception:
        return False
