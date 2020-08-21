"""
파일, 디렉토리 관련 처리 모듈
"""
import os


def join_path(*paths):
    return os.path.join(*paths)


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


def get_file_dirname(file_path):
    return os.path.dirname(os.path.abspath(file_path))


def get_file_list(path_dir):
    if os.path.isdir(path_dir) is True:
        return os.listdir(path_dir)
    else:
        return []


def is_file(file_path):
    return os.path.isfile(file_path)


def get_extension(language):
    ex_dict = {
        'python': '.py',
        'python3': '.py',
    }
    return ex_dict[language]


if __name__=="__main__":
    print(join_path('1','2'))