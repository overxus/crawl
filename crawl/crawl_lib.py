import json


def OpenJson(json_path:str):
    with open(json_path, 'r', encoding='utf-8') as fp:
        content = json.load(fp)
    return content


def SaveJson(content, json_path:str):
    with open(json_path, 'w', encoding='utf-8') as fp:
        json.dump(content, fp)


def Increase(start:int=0):
    while True:
        yield start
        start += 1
