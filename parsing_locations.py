from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from urllib.request import urlretrieve
from collections import Counter
import os

path_webdriver = '/Users/valeriya/node_modules/chromedriver/lib/chromedriver/chromedriver'
url_location = 'https://ru.wikipedia.org/wiki/%D0%91%D0%BE%D0%BB%D1%8C%D1%88%D0%BE%D0%B9_%D1%82%D0%B5%D0%B0%D1%82%D1%80'
path_main_dir = '/Users/Valeriya/Desktop'


def open_browser():
    try:
        browser = webdriver.Chrome(path_webdriver)
        browser.implicitly_wait(6)
        return browser
    except WebDriverException as e:
        print("Указан не верный путь к webdriver! Исправите его и попробуйте снова!")
        exit(1)


def find_geo_coordinates(browser):
    return browser.find_element_by_class_name('mw-kartographer-maplink').text


def find_full_address(browser):
    return browser.find_element_by_xpath("//span[@data-wikidata-property-id]").text


def save_photo(image_link, path_save_dir):
    urlretrieve(image_link, path_save_dir + '/img.jpg')


def save_description(text, path_save_dir):
    with open(path_save_dir + '/description.txt', 'w', encoding='utf8') as f:
        f.write(text)


def save_geo_coordinates(text, path_save_dir):
    with open(path_save_dir + '/geo_coordinates.txt', 'w', encoding='utf8') as f:
        f.write(text)


def save_full_address(text, path_save_dir):
    with open(path_save_dir + '/full_address.txt', 'w', encoding='utf8') as f:
        f.write(text)


def save_word_list(text, path_save_dir):
    with open(path_save_dir + '/word_list.txt', 'w', encoding='utf8') as f:
        f.write(text)


def find_word_list(browser):
    text = browser.find_element_by_class_name('mw-parser-output').text
    word_list = []
    for word in text.split():
        clear_word = ''
        for letter in word:
            if letter.isalpha():
                clear_word += letter.lower()
        word_list.append(clear_word)
    return word_list


def find_image_link(browser):
    infobox_image = browser.find_elements_by_class_name('infobox-image')[0]
    images = infobox_image.find_elements_by_tag_name('img')
    image_links = []
    for image in images:
        image_link = image.get_attribute('src')
        image_links.append(image_link)
    return image_links[0]


def find_description(browser):
    body_content = browser.find_elements_by_class_name('mw-parser-output')[0]
    paragraphs = body_content.find_elements_by_tag_name('p')
    description = ""
    if paragraphs[0] is not None:
        description += paragraphs[0].text
    if paragraphs[1] is not None:
        description += '\n' + paragraphs[1].text
    return description


def main():
    browser = open_browser()
    try:
        browser.get(url_location)
        name = browser.find_element_by_id('firstHeading').text

        # поиск
        description = find_description(browser)
        image_link = find_image_link(browser)
        word_list = find_word_list(browser)
        geo_coordinates = find_geo_coordinates(browser)
        full_address = find_full_address(browser)

        path_save_dir = path_main_dir + '/' + name
        os.mkdir(path_save_dir)

        # сохранение
        save_description(description, path_save_dir)
        save_geo_coordinates(geo_coordinates, path_save_dir)
        save_full_address(full_address, path_save_dir)
        save_word_list(Counter(word_list).most_common(30), path_save_dir)
        save_photo(image_link, path_save_dir)

    except Exception as e:
        print('Ошибка в программе, обратитесь к разработчику.')
        print(e)
    finally:
        browser.quit()


if __name__ == '__main__':
    main()
