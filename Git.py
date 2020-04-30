#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 14:34:51 2020

@author: augustinjose
"""


from git import Repo
from git.exc import GitCommandError
import os




def privateClone(url, dest, username, password):
    """
    Clones private repositories to the directory specified.
    
    Args:
        url (str): The github repository url.
        dest (str): The path of the directory.
        username (str): The username of the github account.
        password (str): The password of the github account.
        
    Returns:
        True (bool): If git clone is successful
        GitCommandError (obj): If an exception occurs.

    """
    try:
        Remote_Url = "https://" + str(username) + ":" + str(password) + "@" + str(url.split("https://")[1])
        """
            Making git queries in the form of "https://username:password@github.com/username/repository" to clone the private repository.
        """
        Repo.clone_from(Remote_Url, str(dest))
    except GitCommandError as e:
        return e
    return True




def clone(url, dest):
    """
    Clones public repositories to the directory specified.
    
    Args:
        url (str): The github repository url.
        dest (str): The path of the directory.
    
    Returns:
        True (bool): If git clone is successful
        GitCommandError (obj): If an exception occurs. 

    """
    try:
        Repo.clone_from(url, dest)
    except GitCommandError as e:
        return e
    return True




def push(username, password, repo):
    """
    Pushes a git initialized local repository to remote github repository.
    
    Args:
        username (str): The username of the github account.
        password (str): The password of the github account.
        repo (str): The path of the git initialized repository.
    
    Returns:
        True (bool): If git push is successful.
        OSError (obj): If an exception occurs.

    """
    try:
        command = "git push https://"+str(username) + ":" + str(password) + "@github.com/" + str(username) + "/" + str(repo) + ".git master"
        os.system(str(command))
    except OSError as e:
        return e
    return True




def add(file):
    """
    Adds file(s) to a local git repository index. 
    
    Args:
        file (str): The path to the file.
    
    Returns:
        True (bool): If git add is successful.
        OSError (obj): If an exception occurs.

    """
    try:
        command = "git add " + str(file)
        os.system(str(command))
    except OSError as e:
        return e
    return True




def commit(message):
    """
    Commits changes made to the local git repository with a user defined commit message.
    
    Args:
        message (str): The user's commit message.
    
    Returns:
        True (bool): If successful.
        OSError (obj): If an exception occurs.

    """
    try:
        command = "git commit -m " + str(message)
        os.system(str(command))
    except OSError as e:
        return e
    return True
