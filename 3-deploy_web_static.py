#!/usr/bin/python3
"""create a compressed file of the web_static directory and
deploy them to the servers"""


from datetime import datetime
from fabric.api import *
from os.path import exists


env.hosts = ['54.152.218.147', '54.87.157.200']
x = []

def deploy():
    """
    deploy the webstatic directory to the servers
    """
    x.append(do_pack())
    if x[0] is None:
        return False
    return do_deploy(x[0])


def do_pack():
    """create a compressed file"""
    x = datetime.now()
    x = x.isoformat()
    x = x.split('.')[0].replace('-', '').replace('T', '').replace(':', '')
    try:
        local("mkdir -p  versions")
        path = f"versions/web_static_{x}.tgz"
        local(f"tar -cvzf {path} web_static")
        return path
    except Exception:
        return None


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
        run(f"mv  /data/web_static/releases/{archive_name}/web_static/* \
             /data/web_static/releases/{archive_name}")
        run(f"rm -rf /data/web_static/releases/{archive_name}/web_static")
        run("rm -rf /data/web_static/current")
        run(f"ln -s /data/web_static/releases/{archive_name}/ \
             /data/web_static/current")
        return True
    except Exception:
        return False
