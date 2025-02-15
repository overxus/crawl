from os import path
from requests import get, post
import pandas as pd
import matplotlib.pyplot as plt


from .crawl_sys import exit, error, log, roll, mv, rm, mkdir, ls, sleep, rsleep
from .crawl_lib import OpenJson, SaveJson, Increase
from .crawl_sql import OpenSql


class Config:
    def __init__(self):
        data_dir = 'data'
        self.input_dir = path.join(data_dir, 'input')
        mkdir(self.input_dir)
        self.output_dir = path.join(data_dir, 'output')
        mkdir(self.output_dir)
        self.temp_dir = path.join(data_dir, 'temp')
        mkdir(self.temp_dir)
