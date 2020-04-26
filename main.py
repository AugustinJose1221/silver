#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 11:04:48 2020

@author: augustinjose
"""

import os
import platform
import subprocess
import sys
from pyfiglet import Figlet
if platform.system() == "Windows":
    import msvcrt
    

f = Figlet(font='slant')
print(f.renderText('Silver - A Python shell prompt'))
    
print(os.name)
print(os.getcwd())
'''
os.chdir("/home/bernd/dropbox/websites/python-course.eu/cities")
print(os.getcwd())
'''
print(os.listdir())