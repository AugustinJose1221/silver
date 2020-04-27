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

from Git import privateClone, Clone, push, add, commit
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
            if file=="":
                self.list = os.listdir()
            else:
                try:
                    self.list = os.listdir(str(file))
                except FileNotFoundError:
                    print(colored("No such file or directory, kemosabe!","red"))
                    return self.updatePrompt()
            self.contents = ""
            for i in self.list:
                if '.' in i:
                    
                    if i.split(".")[1].lower() in ["png", "jpeg", "jpg", "svg", "tiff", "bmp", "raw"]:
                        self.contents = self.contents + "  " + colored(str(i), "green", attrs=['bold'])
                        
                    elif i.split(".")[1].lower() in ["py", "c", "cpp", "html", "css", "js", "go", "java", "v", "xml"]:
                        self.contents = self.contents + "  " + colored(str(i), "blue", attrs=['bold'])
                        
                    elif i.split(".")[1].lower() in ["pdf", "ppt", "doc", "xlsx", "txt", "md", "epub", "tex"]:
                        self.contents = self.contents + "  " + colored(str(i), "grey", attrs=['bold'])
                        
                    elif i.split(".")[1].lower() in ["zip", "rar", "tar", "gz", "xz"]:
                        self.contents = self.contents + "  " + colored(str(i), "magenta", attrs=['bold'])
                        
                    else:
                        self.contents = self.contents + "  " + colored(str(i), "yellow", attrs=['bold'])
                        
                else:
                    self.contents = self.contents + "  " + str(i)
            print(self.contents)
            
        return self.updatePrompt()
    
    
    
    
    def do_dir(self, file):
        if file=="":
                self.list = os.listdir()
        else:
            try:
                self.list = os.listdir(str(file))
            except FileNotFoundError:
                print(colored("No such file or directory, kemosabe!","red"))
                return self.updatePrompt()
        self.contents = ""
        for i in self.list:
            if '.' in i:
                
                if i.split(".")[1].lower() in ["png", "jpeg", "jpg", "svg", "tiff", "bmp", "raw"]:
                    self.contents = self.contents + "  " + colored(str(i), "green", attrs=['bold'])
                    
                elif i.split(".")[1].lower() in ["py", "c", "cpp", "html", "css", "js", "go", "java", "v", "xml"]:
                    self.contents = self.contents + "  " + colored(str(i), "blue", attrs=['bold'])
                    
                elif i.split(".")[1].lower() in ["pdf", "ppt", "doc", "xlsx", "txt", "md", "epub", "tex"]:
                    self.contents = self.contents + "  " + colored(str(i), "grey", attrs=['bold'])
                    
                elif i.split(".")[1].lower() in ["zip", "rar", "tar", "gz", "xz"]:
                    self.contents = self.contents + "  " + colored(str(i), "magenta", attrs=['bold'])
                    
                else:
                    self.contents = self.contents + "  " + colored(str(i), "yellow", attrs=['bold'])
                    
            else:
                self.contents = self.contents + "  " + str(i)
        print(self.contents)
        
        return self.updatePrompt()
   
    
    def do_mkdir(self, file):
        if file=="":
            print(colored("Directory name required, kemosabe!","red"))
        else:
            try:
                os.mkdir(str(file))
            except FileExistsError:
                print(colored("Directory exists, kemosabe!","red"))
        return self.updatePrompt()
    
    def do_echo(self, stream):
        print(str(stream))
        return self.updatePrompt()  
    
    def do_git(self, args):
        if args.split(" ")[0]=="add":
            if len(args.split(" "))==1:
                print(colored("Argument missing, kemosabe!","red"))
                return self.updatePrompt()
            else:
                ret = add(args.split(" ")[1])
                if ret==True:
                    return self.updatePrompt() 
                else:
                    print(colored("Error, kemosabe!\n {}".format(str(ret)),"red"))
                    return self.updatePrompt() 
        
        
            
            
    
    def emptyline(self):
        pass
    
    
    def default(self, inp):
        if inp == 'x' or inp == 'q':
            return self.do_exit(inp)
 
        print(colored("Command {} not found, kemosabe!".format(inp),"red"))
        return self.updatePrompt()



#git
if __name__ == '__main__': 
     silver().cmdloop()
