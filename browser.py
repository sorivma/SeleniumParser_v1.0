from os import path

from selenium import webdriver
from selenium.webdriver.chrome.service import Service


def main_url_to_news_url(url):
    news_url = url + '/news/'
    return news_url


class Browser:
    def __init__(self, browser_type):
        self.browser_type = browser_type
        self.__driver = None
        self.__driver_path = None

    def run(self):
        double_slash = r'\\'
        slash = double_slash[1:]
        if self.browser_type == 'Firefox':
            self.__driver_path = path.abspath('geckodriver.exe').replace(slash, double_slash)
            self.__driver = webdriver.Firefox(service=Service(self.__driver_path))
        elif self.browser_type == 'Chrome':
            self.__driver_path = path.abspath('chromedriver.exe').replace(slash, double_slash)
            self.__driver = webdriver.Chrome(service=Service(self.__driver_path))

    def open_url(self, url):
        self.__driver.get(url=url)

    def open_news(self, url):
        news_url = main_url_to_news_url(url)
        self.open_url(news_url)

    def stop(self):
        self.__driver.close()
        self.__driver.quit()

    def return_driver(self):
        return self.__driver
