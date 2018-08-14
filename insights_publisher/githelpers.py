import subprocess
import logging

def get_path_in_repo(file_dir):
    command = "git -C " + file_dir + " rev-parse --show-prefix"
    try:
        output = subprocess.check_output(command.split(" "), stderr=subprocess.STDOUT).decode("utf-8").strip()
    except subprocess.CalledProcessError as e:
        logging.error("Failed to get notebook path relative to repository root.\n\n" + str(e.output.decode("utf-8")))
        raise

    return output

def get_repo_url(repo_root):
    command = "git -C " + repo_root + " config --get remote.origin.url"
    try:
        output = subprocess.check_output(command.split(" "), stderr=subprocess.STDOUT).decode("utf-8").strip()
    except subprocess.CalledProcessError as e:
        logging.error("Failed to get repository remote url.\n\n" + str(e.output.decode("utf-8")))
        raise
    return output

def get_commit_id(repo_root, branch='origin/master'):
    command = "git -C " + repo_root + " rev-parse " + branch
    try:
        output = subprocess.check_output(command.split(" "), stderr=subprocess.STDOUT).decode("utf-8").strip()
    except subprocess.CalledProcessError as e:
        logging.warning("Failed to get commit id from branch " + branch + "\n\n" + str(e.output.decode("utf-8")))
        raise
    return output

def get_repo_root(file_dir):
    command = "git -C " + file_dir + " rev-parse --show-toplevel"

    try:
        output = subprocess.check_output(command.split(" "), stderr=subprocess.STDOUT).decode("utf-8").strip()
    except subprocess.CalledProcessError as e:
        logging.error("Failed to get root directory of repository.\n\n" + str(e.output.decode("utf-8")))
        raise
    
    return output


def is_git_repo(repo_root):
    command = "git -C " + repo_root + " rev-parse"
    try:
        output = subprocess.check_output(command.split(" "), stderr=subprocess.STDOUT).decode("utf-8")
    except subprocess.CalledProcessError as e:
        raise ValueError("The notebook must be part of a git repository \n\n" + str(e.output))

    if output != '':
        raise ValueError("The notebook must be part of a git repository \n\n" + str(output))

    return True


def is_commited(repo_root):
    command = "git -C " + repo_root + " status -s"
    try:
        output = subprocess.check_output(command.split(" "), stderr=subprocess.STDOUT).decode("utf-8")
    except subprocess.CalledProcessError as e:
        logging.warning("Failed to determine if there are uncommited changes in the repo.\n\n" + str(e.output))
        raise
       
    if output != '':
        return False

    return True

def is_master(repo_root):
    command = "git -C " + repo_root + " rev-parse --abbrev-ref HEAD"
    try:
        output = subprocess.check_output(command.split(" "), stderr=subprocess.STDOUT).decode("utf-8")
    except subprocess.CalledProcessError as e:
        raise
       
    if output.strip() != 'master':
        return False

    return True

def is_synced(repo_root):

    try:
        commit1 = get_commit_id(repo_root, "master")
        commit2 = get_commit_id(repo_root, "origin/master")
    except subprocess.CalledProcessError as e:
        raise

    if commit1 != commit2:          
        return False

    return True

def git_clone(repo_url, clone_path):
    command = "git -C " + clone_path + " clone " + repo_url 
    try:
        output = subprocess.check_output(command.split(" "), stderr=subprocess.STDOUT).decode("utf-8")
    except subprocessCalledProcessError as e:
        logging.error("Failed to clone remote repository.")
        raise

