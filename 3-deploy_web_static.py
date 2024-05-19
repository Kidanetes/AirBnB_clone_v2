#!/usr/bin/python3
"""create a compressed file of the web_static directory and
deploy them to the servers"""


from 1-pack_web_static import do_pack
from 2-do_deploy_web_static import do_deploy
from fabric.api import *


env.hosts = ['52.86.189.212', '52.201.146.212']


def deploy():
    """
    deploy the webstatic directory to the servers
    """
    x = do_pack()
    if x is None:
        return False
    return do_deploy(x)
