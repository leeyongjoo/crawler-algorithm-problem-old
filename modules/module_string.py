import re


def del_win_special_char(before_str):
    """
    windows에서 파일명으로 사용하지 못하는 특수문자 제거

    :param before_str: 문자열
    :return: 특수문자가 제거된 문자열
    """
    return re.sub('[\\\/:*?"<>|]', '', before_str)


if __name__=="__main__":
    print(del_win_special_char('12\\/:*?"<>|34'))