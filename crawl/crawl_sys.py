import os, sys, shutil, random, time, datetime


def exit():
    sys.exit(-1)


def log(message:str):
    print(f'[{datetime.datetime.now()}] {message}')


def error(message:str):
    log(f'[error] {message}')
    exit()


def roll(message:str):
    print(message, end='      \r')


def ls(dir_path:str, recursive:bool=True):
    for item in os.listdir(dir_path):
        full_path = os.path.join(dir_path, item)
        if recursive and os.path.isdir(full_path):
            yield from ls(full_path, recursive=True)
        else:
            yield full_path


def mkdir(dir_path:str):
    os.makedirs(dir_path, exist_ok=True)


def mv(src:str, dst:str):
    shutil.move(src, dst)

def rm(path:str):
    if os.path.isdir(path):
        shutil.rmtree(path, ignore_errors=True)
    else:
        os.remove(path)


def sleep(seconds:float):
    time.sleep(seconds)


def rsleep(min_seconds:float, max_seconds:float):
    time.sleep(min_seconds + random.random() * (max_seconds - min_seconds))
