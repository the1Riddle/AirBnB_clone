#!/usr/bin/python3
"""
    a script that clean all archives based on the number of
    arguements passed
"""

from operator import length_hint
from fabric.api import run, local, cd, env
import os


def do_clean(number=0):
    """Cleans all .tgz files"""
    number = int(number)
    if number == 0:
        number = 2
    else:
        number += 1

    local('cd versions ; ls -t | tail -n +{} | xargs rm -rf'.format(number))
    path = '/data/web_static/releases'
    run('cd {} ; ls -t | tail -n +{} | xargs rm -rf'.format(path, number))
