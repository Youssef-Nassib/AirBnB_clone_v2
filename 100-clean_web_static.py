#!/usr/bin/python3
# Fabfile to delete out-of-date archives.
import os
from fabric.api import env, local, run, lcd, cd

env.hosts = ["104.196.168.90", "35.196.46.172"]

def do_clean(number=0):
    """Delete out-of-date archives.

    Args:
        number (int): The number of archives to keep.
    """
    number = 1 if int(number) == 0 else int(number)

    # Local archives cleaning
    if os.path.exists("versions"):
        archives = sorted(
            [f for f in os.listdir("versions") if f.endswith(".tgz")],
            key=lambda x: os.path.getmtime(os.path.join("versions", x)),
            reverse=True
        )
        # Keep only the most recent 'number' archives
        archives_to_delete = archives[number:]
        with lcd("versions"):
            for archive in archives_to_delete:
                local("rm ./{}".format(archive))

    # Remote archives cleaning
    for host in env.hosts:
        with cd("/data/web_static/releases"):
            archives = run("ls -tr | grep 'web_static_'").split()
            # Keep only the most recent 'number' archives
            archives_to_delete = archives[:-number]
            for archive in archives_to_delete:
                run("rm -rf ./{}".format(archive))
