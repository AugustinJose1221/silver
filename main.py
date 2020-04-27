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
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")
    f = Figlet(font='slant')
    print(f.renderText('Silver - A Python shell prompt'))
    intro = colored("\n                                                                \n                   🏇 Hi-Yo, Silver! Away!                      \n                                                                ", "grey", "on_white") + "\n"
    if platform.system() == "Windows":
            prompt = colored(str("~") + str(os.getcwd()) + str("> "), "green")
    else:
        prompt = colored(str("~") + str(os.getcwd()) + str("> "), "green", attrs=['bold'])
    
    
    def updatePrompt(self):
        if platform.system() == "Windows":
            self.prompt = colored(str("~") + str(os.getcwd()) + str("> "), "green")
        else:
            self.prompt = colored(str("~") + str(os.getcwd()) + str("> "), "green", attrs=['bold'])
    
    def do_exit(self, inp):
        print(colored("\n                                                                \n                   🏇 Hi-Yo, Silver! Away!                      \n                                                                ", "grey", "on_white") + "\n")
        return True
    
    def do_cd(self, loc):
        if loc=="":
            self.dir = "/"
        else:
            self.dir = str(os.getcwd()) + "/" + str(loc) 
        try:
            os.chdir(self.dir)
        except FileNotFoundError:
            print(colored("No such file or directory, kemosabe!","red"))
   
        return self.updatePrompt()
    
    def do_ls(self, file):
        
        if platform.system() == "Windows":
            print(colored("Command ls not found, kemosabe!","red"))
            
        else:
            self.list = os.listdir()
            self.contents = ""
            for i in self.list:
                if '.' in i:
                    self.contents = self.contents + "  " + colored(str(i), "green", attrs=['bold'])
                else:
                    self.contents = self.contents + "  " + str(i)
            print(self.contents)
            
        return self.updatePrompt()
    
    def default(self, inp):
        if inp == 'x' or inp == 'q':
            return self.do_exit(inp)
 
        print(colored("Command {} not found, kemosabe!".format(inp),"red"))
        return self.updatePrompt()


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