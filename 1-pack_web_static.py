#!/usr/bin/python3
""" This module contains the function do_pack that generates a .tgz archive
    from the contents of the web_static folder (fabric script) """
import warnings

warnings.filterwarnings(action='ignore', category=DeprecationWarning)
from fabric.api import local
from datetime import datetime

def do_pack():
    """ Fabric script that generates a .tgz archive from the contents of the
        web_static folder """
    # Create versions directory if it doesn't exist
    local("mkdir -p versions")

    # Generate timestamp
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    filename = "versions/web_static_{}.tgz".format(date)

    # Create .tgz archive from web_static folder
    result = local("tar -cvzf {} web_static".format(filename))

    # Check if the tar operation was successful
    if result.return_code == 0:
        return filename
    else:
        return None
