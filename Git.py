from git import Repo
from git.exc import GitCommandError
import os

def privateClone(url, dest, username, password):
    try:
        Remote_Url = "https://" + str(username) + ":" + str(password) + "@" + str(url.split("https://")[1])
        Repo.clone_from(Remote_Url, str(dest))
    except GitCommandError as e:
        return e
    return True

def clone(url, dest):
    try:
        Repo.clone_from(url, dest)
    except GitCommandError as e:
        return e
    return True


def push(username, password, repo):
    try:
        command = "git push https://"+str(username) + ":" + str(password) + "@github.com/" + str(username) + "/" + str(repo) + ".git master"
        os.system(str(command))
    except OSError as e:
        return e
    return True


def add(file):
    try:
        command = "git add " + str(file)
        os.system(str(command))
    except OSError as e:
        return e
    return True


def commit(message):
    try:
        command = "git commit -m " + str(message)
        os.system(str(command))
    except OSError as e:
        return e
    return True
