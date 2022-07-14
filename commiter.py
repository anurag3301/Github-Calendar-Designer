import subprocess
import os
import datetime
import time
from main import *

def commit_init():
    os.chdir(REPO_DIR)

    git_dir = subprocess.run(['git rev-parse --git-dir'], stdout=subprocess.PIPE,
                                 stderr=subprocess.PIPE, text=True, shell=True)
    if git_dir.stderr:
        print("Not a git repo")
        exit()

    git_signing = subprocess.run(['git config commit.gpgsign false'], stdout=subprocess.PIPE,
                                 stderr=subprocess.PIPE, text=True, shell=True)
    if git_signing.stderr:
        print(git_signing.stderr)
        exit()

def commit(date):

    commit_init()

    message = float.hex(time.time())
    with open('file', "w") as f:
        f.write(message)

    git_stage = subprocess.run(['git add .'],
          stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, text=True)

    if git_stage.stderr:
        print(git_stage.stderr)
        exit()
    else:
        print("Staged!" + str(date))

    git_commit = subprocess.run([f'git commit --author="{USERNAME} <{USEREMAIL}>" -m "{message}"'],
          stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, text=True)

    if git_commit.stderr:
        print(git_commit.stderr)
        exit()
    else:
        print("Commited!" + str(date))
    
    commit_time = f"{date.year}-{date.month}-{date.day} 12:00:00"
    git_ammend = subprocess.run([f'git commit --amend --no-edit --date="{commit_time}"'],
          stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, text=True)

    if git_ammend.stderr:
        print(git_ammend.stderr)
        exit()
    else:
        print("Ammended!" + str(date))

    print()

