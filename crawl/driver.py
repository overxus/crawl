import time
from seleniumwire import webdriver
from seleniumwire import utils
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class EdgeDriver(webdriver.Edge):
    def __init__(self, headless:bool=True):
        """当headless==True时，不会显示窗口"""
        options = webdriver.EdgeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])  # 禁止控制台输出日志
        options.add_argument('disable-blink-features=AutomationControlled')
        if headless:
            options.add_argument('--headless')  
            options.add_argument("user-agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'")
            options.add_argument("--window-size=1920,1080")

        super().__init__(options=options)
    
    def BotTest(self):
        self.get('https://bot.sannysoft.com')
        while True:
            time.sleep(5)
