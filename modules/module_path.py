import os

def mkdir_if_not_exists(dirname):
    if os.path.isdir(dirname) is False:
        os.mkdir(dirname)