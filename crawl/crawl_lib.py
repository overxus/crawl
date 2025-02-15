import json


def OpenJson(json_path:str):
    with open(json_path, 'r', encoding='utf-8') as fp:
        content = json.load(fp)
    return content


def SaveJson(content, json_path:str):
    with open(json_path, 'w', encoding='utf-8') as fp:
        json.dump(content, fp)


def FromJson(json_str:str):
    return json.loads(json_str)


def ToJson(obj) -> str:
    return json.dumps(obj)


def Increase(start:int=0):
    while True:
        yield start
        start += 1
