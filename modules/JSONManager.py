import json
from collections import OrderedDict
from pathlib import Path
from modules.module_path import mkdir_if_not_exists

# 상위 디렉토리 경로
BASE_DIR = Path(__file__).resolve(strict=True).parent.parent


class JSONManager(object):
    """
    json 파일을 로드하여 로그인 정보 추출, 반환 메서드 제공
    """
    _JSON_DIR = '_config'

    def __init__(self, name, keys):
        self.site_name = name
        self.json_keys = keys
        self.json_dirname = BASE_DIR / self._JSON_DIR
        self.json_basename = ''.join([self.site_name, '.json'])
        self.json_file = self.json_dirname / self.json_basename
        self.json_data = self._load_json_file()

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
                print(f'{self.json_basename} 파일이 존재하지 않습니다.')
                self._write_json_file()
            else:
                return json_data

    def _write_json_file(self) -> bool:
        """
        json 파일 생성

       :return: bool
        """
        login_dict = OrderedDict()
        for key in self.json_keys:
            login_dict[key] = input(f'Input {self.site_name} {key}: ')

        mkdir_if_not_exists(self.json_dirname)
        with open(self.json_file, 'w', encoding='utf-8') as f:
            json.dump(login_dict, f, indent=4)
        return True

    def get_json_data(self) -> json:
        """
        json 객체 반환

        :return: user_id, user_pw
        """
        return self.json_data

    def write_and_load(self):
        self._write_json_file()
        self.json_data = self._load_json_file()


if __name__ == "__main__":
    site_name = 'test'
    lm = JSONManager(site_name, ['1','2'])
    print(lm.get_json_data())
