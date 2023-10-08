import json

class LogUtils:

    @staticmethod
    def stringifier(data: dict) -> str:
        return json.dumps(data,  separators=(', ', ': '))
