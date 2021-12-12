from browser import Browser
from news_getting import Parser
from feedgenerator import create_xml


def read_settings():
    with open('settings.txt', 'r') as settings:
        line = settings.readline()
        while line:
            if 'url_list' in line:
                line = line.replace('url_list: ', '')
                line = line.replace('\n', '')
                urls = line.split(',')
            '''if 'channels' in line:
                line = line.replace('channels: ', '')
                line = line.replace('\n', '')
                channels = int(line)'''
            if 'browser' in line:
                line = line.replace('browser: ', '')
                line = line.replace('\n', '')
                browser_type = line
            line = settings.readline()
        return urls, browser_type


def main():
    urls, browser_type = read_settings()
    browser = Browser(browser_type)
    browser.run()
    parser = Parser(browser)
    for url in urls:
        browser.open_news(url)
        if 'madi' in url:
            data = parser.parse_news_madi()
            name = 'madi'
            create_xml(data, name)
        elif 'omgups' in url:
            data = parser.parse_news_pgups()
            name = 'omgups'
            create_xml(data, name)
        elif 'pgups' in url:
            data = parser.parse_news_pgups()
            name = 'pgups'
            create_xml(data, name)
        elif 'samgups' in url:
            data = parser.parse_news_samgups()
            name = 'samgups'
            create_xml(data, name)
        else:
            pass
    browser.stop()


if __name__ == '__main__':
    main()
