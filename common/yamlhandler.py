import yaml
from typing import Any


class YamlHandler:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def load(self) -> Any:
        """加载YAML文件内容"""
        try:
            with open(self.file_path, "r", encoding="utf-8") as file:
                return yaml.safe_load(file)
        except FileNotFoundError:
            print(f"The file {self.file_path} does not exist.")
            return None
        except yaml.YAMLError as exc:
            print(f"Error in loading YAML file: {exc}")
            return None

    def save(self, data: Any) -> None:
        """将YAML数据保存到文件"""
        try:
            with open(self.file_path, "w", encoding="utf-8") as file:
                yaml.safe_dump(data, file, default_flow_style=False, allow_unicode=True)
        except Exception as exc:
            print(f"Error in saving YAML file: {exc}")

    def read(self, key: str) -> Any:
        """读取特定的YAML数据"""
        data = self.load()
        if data is not None:
            return self._get_nested_key(data, key)
        return None

    def write(self, key: str, value: Any) -> None:
        """写入特定的YAML数据"""
        data = self.load()
        if data is not None:
            self._set_nested_key(data, key, value)
            self.save(data)

    def _get_nested_key(self, data: dict, key: str) -> Any:
        """递归获取嵌套的键值"""
        keys = key.split(".")
        for k in keys:
            if isinstance(data, dict) and k in data:
                data = data[k]
            else:
                return None
        return data

    def _set_nested_key(self, data: dict, key: str, value: Any) -> None:
        """递归设置嵌套的键值"""
        keys = key.split(".")
        for k in keys[:-1]:
            if k not in data or not isinstance(data[k], dict):
                data[k] = {}
            data = data[k]
        data[keys[-1]] = value


# 使用示例
if __name__ == "__main__":
    yaml_file_path = r"/config/config.yaml"
    yaml_handler = YamlHandler(yaml_file_path)
    # print(yaml_handler.load()['database'])
    # print(yaml_handler.read('database'))

    # 写入YAML数据
    data_to_write = {
        "database": {"host": "localhost", "port": 3306},
        "user": {"name": "admin", "password": "password123"},
    }
    yaml_file_path2 = r"D:\CODE\AUTOMATED_UI_QA\test_case_data\config2.yaml"
    yaml_handler = YamlHandler(yaml_file_path2)
    yaml_handler.save(data_to_write)
    yaml_handler.write("database.host", "192.168.1.100")
    print(yaml_handler.load())
    yaml_handler.save(data_to_write)

    # 读取YAML数据
    database_host = yaml_handler.read("database.host")
    print(f"Database Host: {database_host}")

    # 加载整个YAML文件内容
    loaded_data = yaml_handler.load()
    print(loaded_data)
