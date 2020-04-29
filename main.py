#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 11:04:48 2020

@author: augustinjose
"""
"""

   _____ _ __                            ___ 
  / ___/(_) /   _____  _____            /   |
  \__ \/ / / | / / _ \/ ___/  ______   / /| |
 ___/ / / /| |/ /  __/ /     /_____/  / ___ |
/____/_/_/ |___/\___/_/              /_/  |_|
                                             
    ____        __  __                        __         ____
   / __ \__  __/ /_/ /_  ____  ____     _____/ /_  ___  / / /
  / /_/ / / / / __/ __ \/ __ \/ __ \   / ___/ __ \/ _ \/ / / 
 / ____/ /_/ / /_/ / / / /_/ / / / /  (__  ) / / /  __/ / /  
/_/    \__, /\__/_/ /_/\____/_/ /_/  /____/_/ /_/\___/_/_/   
      /____/                                                 
                                      __ 
    ____  _________  ____ ___  ____  / /_
   / __ \/ ___/ __ \/ __ `__ \/ __ \/ __/
  / /_/ / /  / /_/ / / / / / / /_/ / /_  
 / .___/_/   \____/_/ /_/ /_/ .___/\__/  
/_/                        /_/           


                                                                
                   🏇 Hi-Yo, Silver! Away!                      
                                                                



















"""

import os
import platform

from cmd import Cmd
from pyfiglet import Figlet


try:
    from termcolor import colored
    
    
except ImportError:
    colored = None

from Git import privateClone, clone, push, add, commit




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
    
    
    def usernamePrompt(self):
        if platform.system() == "Windows":
            self.username = input(colored("Username : ", "green"))
        else:
            self.username = input(colored("Username :", "green", attrs=['bold']))
        return self.username
            
    def passwordPrompt(self):
        if platform.system() == "Windows":
            self.password = input(colored("Password : ", "green"))
        else:
            self.password = input(colored("Password :", "green", attrs=['bold']))
        return self.password
    
    
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
        
        if args.split(" ")[0]=="commit":
            if len(args.split(" ")) <= 1:
                print(colored("Argument missing, kemosabe!","red"))
                return self.updatePrompt()
            else:
                ret = commit(args.split(" ")[2])
                if ret==True:
                    return self.updatePrompt()
                else:
                    print(colored("Error, kemosabe!\n {}".format(str(ret)),"red"))
                    return self.updatePrompt() 
        
        if args.split(" ")[0]=="push":
            if len(args.split(" ")) <= 2:    
                print(colored("Argument missing, kemosabe!","red"))
                return self.updatePrompt()
            else:
                self.username = self.usernamePrompt()
                self.password = self.passwordPrompt()
                self.changedPassword = self.changePassword(self.password)
                '''
                for i in self.password:
                    if i=='@':
                        self.changedPassword = self.changedPassword + "%40"
                    else:
                        self.changedPassword = self.changedPassword + str(i)
                '''
                self.repo = str(os.path.split(str(os.getcwd()))[len(os.path.split(str(os.getcwd())))-1])
                ret = push(self.username, self.changedPassword, self.repo)
                if ret==True:
                    return self.updatePrompt()
                else:
                    print(colored("Error, kemosabe!\n {}".format(str(ret)),"red"))
                    return self.updatePrompt() 
            
        if args.split(" ")[0]=="clone":
            if len(args.split(" ")) <= 1:
                print(colored("Argument missing, kemosabe!","red"))
                return self.updatePrompt()
            else:
                self.repo = str(args.split(" ")[1]).split("/")[len(str(args.split(" ")[1]).split("/"))-1].split(".")[0]
                ret = clone(str(args.split(" ")[1]), self.repo)
                if ret==True:
                    return self.updatePrompt()
                elif "code(128)" in str(ret).split():
                    self.username = self.usernamePrompt()
                    self.password = self.passwordPrompt()
                    self.changedPassword = self.changePassword(self.password)
                    '''
                    for i in self.password:
                        if i=='@':
                            self.changedPassword = self.changedPassword + "%40"
                        else:
                            self.changedPassword = self.changedPassword + str(i)
                    '''
                    ret = privateClone(str(args.split(" ")[1]), self.repo, self.username, self.changedPassword)
                    if ret==True:
                        return self.updatePrompt()
                    elif "code(128)" in str(ret).split():
                        print(colored("Invalid username or password, kemosabe!","red"))
                        return self.updatePrompt()
                    else:
                        print(colored("Command failed, kemosabe!","red"))
                        return self.updatePrompt()
                else:
                    print(colored("Command failed, kemosabe!","red"))
                    return self.updatePrompt()    
                   
       
    #help
    #documentation
    def changePassword(self, password):
        self.changedPassword=""
        for i in self.password:
            if i=='!':
                self.changedPassword = self.changedPassword + "%21"
            if i=='#':
                self.changedPassword = self.changedPassword + "%23"
            if i=='$':
                self.changedPassword = self.changedPassword + "%24"
            if i=='&':
                self.changedPassword = self.changedPassword + "%26"
            if i=='(':
                self.changedPassword = self.changedPassword + "%28"
            if i==')':
                self.changedPassword = self.changedPassword + "%29"
            if i=='\'':
                self.changedPassword = self.changedPassword + "%27"
            if i=='*':
                self.changedPassword = self.changedPassword + "%2A"
            if i=='+':
                self.changedPassword = self.changedPassword + "%2B"
            if i==',':
                self.changedPassword = self.changedPassword + "%2C"
            if i=='/':
                self.changedPassword = self.changedPassword + "%2F"
            if i==':':
                self.changedPassword = self.changedPassword + "%3A"
            if i==';':
                self.changedPassword = self.changedPassword + "%3B"
            if i=='=':
                self.changedPassword = self.changedPassword + "%3D"
            if i=='?':
                self.changedPassword = self.changedPassword + "%3F"
            if i=='@':
                self.changedPassword = self.changedPassword + "%40"
            if i=='[':
                self.changedPassword = self.changedPassword + "%5B"
            if i==']':
                self.changedPassword = self.changedPassword + "%5D"
            else:
                self.changedPassword = self.changedPassword + str(i)
        return self.changedPassword
                
                
                
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
