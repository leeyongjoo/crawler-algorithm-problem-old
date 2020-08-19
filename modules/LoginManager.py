import json
import os
from collections import OrderedDict
from pathlib import Path
import modules.module_path

# 상위 디렉토리 경로
# 다음과 같이 경로 연결: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve(strict=True).parent.parent


class LoginManager(object):
    """
    json 파일을 로드하여 로그인 정보 추출, 반환 메서드 제공
    """
    _JSON_DIR = 'login_info'
    _JSON_SUFFIX = '_login.json'
    _JSON_KEYS = {
        'user_id': 'userId',
        'user_pw': 'userPw',
    }

    def __init__(self, name):
        self.site_name = name
        self.json_dirname = BASE_DIR / self._JSON_DIR
        self.json_basename = ''.join([self.site_name, self._JSON_SUFFIX])
        self.json_file = self.json_dirname / self.json_basename
        # self.json_data = self._load_json_file()

    def _load_json_file(self) -> json:
        """
        json 파일 로드

        :return: json 파일 객체
        """
        while True:
            try:
                with open(self.json_file) as f:
                    json_data = json.load(f)
            except FileNotFoundError:
                print(f'<< 로그인 정보 파일 생성 >>')
                print(f'>> 로그인 정보 파일 생성', '성공.' if self._write_json() else '실패!')
            else:
                return json_data

    def _write_json(self) -> bool:
        """
        json 파일 생성

        :return: 성공 시 True, 실패 시 False
        """
        login_dict = OrderedDict()
        login_dict[self._JSON_KEYS['user_id']] = input(f'Input {self.site_name} User ID: ')
        login_dict[self._JSON_KEYS['user_pw']] = input(f'Input {self.site_name} User PW: ')

        modules.module_path.mkdir_if_not_exists(self.json_dirname)

        with open(self.json_file, 'w', encoding='utf-8') as f:
            json.dump(login_dict, f, indent=4)
        return True

    def get_idpw_from_json(self) -> tuple:
        """
        json 객체에서 id와 pw만 반환

        :return: user_id, user_pw
        """
        json_data = self._load_json_file()
        return json_data[self._JSON_KEYS['user_id']], json_data[self._JSON_KEYS['user_pw']]

    def write_and_load(self):
        self._write_json()
        self._load_json_file()


if __name__ == "__main__":
    site_name = 'test'
    lm = LoginManager(site_name)
    print(lm.get_idpw_from_json())
