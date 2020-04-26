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

from cmd import Cmd
from pyfiglet import Figlet

if platform.system() == "Windows":
    import msvcrt
    
try:
    from termcolor import colored
    
    
    
except ImportError:
    colored = None

class silver(Cmd):
    f = Figlet(font='slant')
    print(f.renderText('Silver - A Python shell prompt'))
    intro = colored("\n                                                                \n                   🏇 Hi-Yo, Silver! Away!                      \n                                                                ", "grey", "on_white") + "\n"
    def updatePrompt():
        if platform.system() == "Windows":
            prompt = colored(str("~") + str(os.getcwd()) + str("> "), "green")
        else:
            prompt = colored(str("~") + str(os.getcwd()) + str("> "), "green", attrs=['bold'])
        
        
    def do_exit(self, inp):
        '''exit the application. Shorthand: x q.'''
        print("Bye")
        return True
 
    def default(self, inp):
        if inp == 'x' or inp == 'q':
            return self.do_exit(inp)
 
        print("Default: {}".format(inp))
 

if __name__ == '__main__':  
     silver().cmdloop()
'''
print(os.name)
print(os.getcwd())

os.chdir("/home/bernd/dropbox/websites/python-course.eu/cities")
print(os.getcwd())

print(os.listdir()) 
string = "Test"
color = "green"
print(colored(string, color))
'''