import os


def mkdir_if_not_exists(path_dir):
    while True:
        try:
            if os.path.isdir(path_dir) is False:
                os.mkdir(path_dir)
        except FileNotFoundError:
            print(os.path.abspath(os.path.join(path_dir, os.pardir)))
            mkdir_if_not_exists(
                os.path.abspath(os.path.join(path_dir, os.pardir)))
        else:
            break


def get_file_list(path_dir):
    if os.path.isdir(path_dir) is True:
        return os.listdir(path_dir)
    else:
        return []


if __name__=="__main__":
    print(join_path('1','2'))