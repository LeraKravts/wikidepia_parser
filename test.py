from main import parse


path_webdriver = 'chromedriver.exe'
path_main_dir = 'E:/Users/vasy/Desktop'


def main():
    parse(path_webdriver, path_main_dir, 'https://ru.wikipedia.org/wiki/%D0%93%D0%BE%D1%81%D1%83%D0%B4%D0%B0%D1%80%D1%81%D1%82%D0%B2%D0%B5%D0%BD%D0%BD%D1%8B%D0%B9_%D0%AD%D1%80%D0%BC%D0%B8%D1%82%D0%B0%D0%B6')
    parse(path_webdriver, path_main_dir, 'https://ru.wikipedia.org/wiki/%D0%9A%D1%83%D0%BD%D1%81%D1%82%D0%BA%D0%B0%D0%BC%D0%B5%D1%80%D0%B0')
    parse(path_webdriver, path_main_dir, 'https://ru.wikipedia.org/wiki/%D0%9C%D0%B0%D1%80%D0%B8%D0%B8%D0%BD%D1%81%D0%BA%D0%B8%D0%B9_%D1%82%D0%B5%D0%B0%D1%82%D1%80')
    parse(path_webdriver, path_main_dir, 'https://ru.wikipedia.org/wiki/%D0%A0%D0%BE%D1%81%D1%81%D0%B8%D0%B9%D1%81%D0%BA%D0%B0%D1%8F_%D0%BD%D0%B0%D1%86%D0%B8%D0%BE%D0%BD%D0%B0%D0%BB%D1%8C%D0%BD%D0%B0%D1%8F_%D0%B1%D0%B8%D0%B1%D0%BB%D0%B8%D0%BE%D1%82%D0%B5%D0%BA%D0%B0')
    parse(path_webdriver, path_main_dir, 'https://ru.wikipedia.org/wiki/%D0%9F%D0%B5%D1%82%D1%80%D0%BE%D0%BF%D0%B0%D0%B2%D0%BB%D0%BE%D0%B2%D1%81%D0%BA%D0%B0%D1%8F_%D0%BA%D1%80%D0%B5%D0%BF%D0%BE%D1%81%D1%82%D1%8C')
    parse(path_webdriver, path_main_dir, 'https://ru.wikipedia.org/wiki/%D0%98%D1%81%D0%B0%D0%B0%D0%BA%D0%B8%D0%B5%D0%B2%D1%81%D0%BA%D0%B8%D0%B9_%D1%81%D0%BE%D0%B1%D0%BE%D1%80')
    parse(path_webdriver, path_main_dir, 'https://ru.wikipedia.org/wiki/%D0%9D%D0%B5%D0%B2%D1%81%D0%BA%D0%B8%D0%B9_%D0%BF%D1%80%D0%BE%D1%81%D0%BF%D0%B5%D0%BA%D1%82')


if __name__ == '__main__':
    main()
