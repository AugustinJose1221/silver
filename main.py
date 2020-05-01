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
                                                                


Silver is a customizable shell written in Python. Silver can run basic linux and windows commands. The source code of
silver is available at "https://github.com/AugustinJose1221/silver". Making custom commands and configuring commands 
do multiple tasks is possible by making required tweaks to the source code. The entire code is written in Python and 
compatible with Windows and Unix systems. Open issues to raise errors found while installation or runtime. Any 
additional features/commands can be added by making pull requests to the master git branch.

Description
-----------

Release version            1.0
Author                     Augustin Jose
Python version             3.6
Supported Platforms        Windows and UNIX
    






"""

import os
import platform

from cmd import Cmd
from pyfiglet import Figlet


try:
    from termcolor import colored
    
    
except ImportError:
    colored = None

from src.Git import privateClone, clone, push, add, commit




class silver(Cmd):
    """ 
    Executing silver.cmdloop() starts a commandline shell.
     
    Methods:
        updatePrompt(obj, str)
        usernamePrompt(obj)
        passwordPrompt(obj)
        do_exit(obj, str)
        do_cd(obj, str)
        do_ls(obj,str)
        do_dir(obj, str)
        do_mkdir(obj, str)
        do_echo(obj, str)
        do_git(obj, str)
        changePassword(obj, str)
        emptyline(obj)
        default(obj, str)
    
    """
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
    
    
    
    def do_help(self, args):
        print("You are screwed")    
        return self.updatePrompt()
    #Complete help
    #Complete autocompletion

    def updatePrompt(self):
        """
        Updates the prompt with the path of the current directory when called.
            
        Args:
            self (obj): The class object.
        
        Returns:
            None

        """
        if platform.system() == "Windows":
            self.prompt = colored(str("~") + str(os.getcwd()) + str("> "), "green")
        else:
            self.prompt = colored(str("~") + str(os.getcwd()) + str("> "), "green", attrs=['bold'])
    
    
    
    
    def usernamePrompt(self):
        """
        Displays a prompt to input the username and returns the username.
        
        Args:
            self (obj): The class object.
        
        Returns:
            username (str): The username entered by the user.
        
        """
        if platform.system() == "Windows":
            self.username = input(colored("Username : ", "green"))
        else:
            self.username = input(colored("Username :", "green", attrs=['bold']))
        return self.username
            
    
    
    
    def passwordPrompt(self):
        """
        Displays a prompt to input the password and returns the password.
        Args:
            self (obj): The class object.
        
        Returns:
            password (str): The password entered by the user.

        """
        if platform.system() == "Windows":
            self.password = input(colored("Password : ", "green"))
        else:
            self.password = input(colored("Password :", "green", attrs=['bold']))
        return self.password
    
    
    
    
    def do_exit(self, inp):
        """
Description:
    Exits from the shell.

Usage:
    exit [OPTIONAL]<exit message>
    
        """
        """
        Args:
            self (obj): The class object.
            inp (str): Optional exit prompt.
        
        Returns:
            True (bool): if TypeError is False.
            self.updatePrompt(): if TypeError is True.

        """
        try:
            print(colored("\n                                                                \n                   🏇 Hi-Yo, Silver! Away!                      \n                                                                ", "grey", "on_white") + "\n")
            return True
        except TypeError:
            print(colored("Command not found, kemosabe!","red"))
            return self.updatePrompt()
    
    
    
    
    def do_cd(self, loc):
        """
Description:
    Changes the working directory of the shell to the user defined directory.

Usage:
    cd [OPTIONAL]<directory><path>
    
        """
        """
        Args:
            self (obj): The class object.
            loc (str): Path of the directory.
        
        Returns:
            self.updatePrompt()

        """
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
        """
Description:
    Lists the contents of the specified directory. If no path is given, the contents of the current working directory is listed. 
    Command not available for Windows platform. Returns "Command ls not found, kemosabe!" if executed in Windows. Use dir command
    instead of ls in Windows systems.

Usage:
    ls [OPTIONAL]<directory><path>
    
        """
        """
        Args:
            self (obj): The class object.
            file (path): Path of the directory to be listed.
        
        Returns:
            self.updatePrompt()

        """
        
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
        """
Description:
    Displays the contents of the directory specified. If no path is given, the path of the current working directory is used.

Usage:
    dir [OPTIONAL]<directory><path>
    
        """
        """
        Args:
            self (obj): The class object.
            file (str): The path of the directory.
        
        Returns:
            self.updatePrompt()

        """
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
        """
Description:
    Creates a directory within the current working directory.

Usage:
    mkdir directory><path>
    
        """
        """
        Args:
            self (obj): The class object.
            file (str): Path of the directory to be created.
        
        Returns:
            self.updatePrompt()

        """
        if file=="":
            print(colored("Directory name required, kemosabe!","red"))
        else:
            try:
                os.mkdir(str(file))
            except FileExistsError:
                print(colored("Directory exists, kemosabe!","red"))
        return self.updatePrompt()




    def do_echo(self, stream):
        """
Description:
    Displays a message in the shell.

Usage:
    echo [OPTIONAL]<message>
    
        """
        """
        Args:
            self (obj): The class object.
            stream (str): The string to be displayed in the shell.
        
        Returns:
            self.updatePrompt()

        """
        print(str(stream))
        return self.updatePrompt()  
    
    
    
    
    def do_git(self, args):
        """
Description:
    Executes git commands.

Usage:
    git [OPTIONAL][add <directory><path>][commit <message>][push <origin> <branch>][clone <url>]
        add     Adds file(s) to a local git repository index 
        commit  Record changes to the repository
        push    Update remote refs along with associated objects
        clone   Clone a repository into a new directory
        
        """
        """
        Args:
            self (obj): The class object.
            args (str): The subcommands and attributes of the git command.
        
        Returns:
            self.updatePrompt()

        """
        
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
       
        
       
    
    def changePassword(self, password):
        """
        Replaces special characters with their URL encodings.
        
        Args:
            self (obj): The class object.
            password (str): The input password to be formatted.
        
        Returns:
            self.changePassword :The formatted password with special characters replaced by their URL encodings.

        """
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
        """
        Executes when Return key is entered without any commands.
        
        Args:
            self (obj): The class object.
        
        Returns:
            None
        """
        pass
    
    
    
    
    def default(self, inp):
        """
        Displays error message whenever an unknown command is executed.
        
        Args:
            self (obj): The class object.
            inp (str): The command executed.        
        
        Returns:
            self.do_exit(): When the exit sequence is executed.
            self.update_Prompt(): When unknown command is executed

        """
        if inp == 'x' or inp == 'q':
            return self.do_exit(inp)
 
        print(colored("Command {} not found, kemosabe!".format(inp),"red"))
        return self.updatePrompt()



if __name__ == '__main__': 
     silver().cmdloop()
