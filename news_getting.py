from selenium.webdriver.common.by import By


class Parser:
    def __init__(self, browser):
        self.__browser = browser
        self.__driver = browser.return_driver()

    def parse_news_pgups(self):

        data = []
        news_elements = self.__driver.find_elements(By.CLASS_NAME, 'news')
        for news_element in news_elements:
            title = news_element.find_element(By.TAG_NAME, 'a').text
            description = news_element.find_element(By.CLASS_NAME, 'text').text
            link = news_element.find_element(By.TAG_NAME, 'a').get_attribute('href')
            date = news_element.find_element(By.CLASS_NAME, 'date').text
            data.append([title, description, date, link])
        return data

    def parse_news_madi(self):

        data = []

        row = self.__driver.find_element(By.CLASS_NAME, 'row')
        news_elements = row.find_elements(By.CLASS_NAME, 'col-md-6')
        for news_element in news_elements:
            title_date = news_element.text.split('\n')
            title = title_date[0]
            try:
                date = title_date[1]
            except:
                date = None
            link = news_element.find_element(By.TAG_NAME, 'a').get_attribute('href')

            data.append([title, date, link])

        for data_block in data:
            self.__driver.get(data_block[2])
            main_element = self.__driver.find_element(By.CLASS_NAME, 'container-fluid')
            description = main_element.find_element(By.TAG_NAME, 'p')
            data_block.insert(1, description.text)

        return data

    def parse_news_omgups(self):

        data = []

        row = self.__driver.find_element(By.CLASS_NAME, 'news-list').find_element(By.CLASS_NAME, 'row')
        news_elements = row.find_elements(By.CLASS_NAME, 'row')
        for news_element in news_elements:
            title = news_element.find_element(By.CLASS_NAME, 'news-title').text
            description = news_element.find_element(By.TAG_NAME, 'p').text
            date = news_element.find_element(By.CLASS_NAME, 'news-date-time').text
            links_elements = news_element.find_elements(By.TAG_NAME, 'a')
            try:
                link = links_elements[0].get_attribute('href')
            except:
                link = None
            data.append([title, description, date, link])

        return data

    def parse_news_samgups(self):

        data = []

        main_element = self.__driver.find_element(By.CLASS_NAME, 'news-list')

        news_elements = main_element.find_elements(By.CLASS_NAME, 'news-item')
        for news_element in news_elements:
            headline = news_element.find_element(By.TAG_NAME, 'b').text
            description = news_element.find_element(By.CLASS_NAME, 'news-anons').text
            date = news_element.find_element(By.CLASS_NAME, 'news-date-time').text
            link = news_element.find_element(By.TAG_NAME, 'a').get_attribute('href')
            data.append([headline, description, date, link])

        return data
