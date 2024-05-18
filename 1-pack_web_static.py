#!/usr/bin/env bash
"""using fabric to compress all files in
webstatic directory"""


from datetime import datetime
from fabric.api import *


def do_pack():
    """create a compressed file"""
    x = datetime.now()
    x = x.isoformat()
    x = x.split('.')[0].replace('-', '').replace('T', '').replace(':', '')
    try:
        local("mkdir -p  versions")
        path = f"versions/web_static_{x}.tgz"
        local(f"tar -cvf {path} web_static")
        return path
    except Exception:
        return None
