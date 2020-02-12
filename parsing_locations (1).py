from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from urllib.request import urlretrieve
from collections import Counter
import os

path_webdriver = '/Users/valeriya/node_modules/chromedriver/lib/chromedriver/chromedriver'
url_location = 'https://ru.wikipedia.org/wiki/%D0%91%D0%BE%D0%BB%D1%8C%D1%88%D0%BE%D0%B9_%D1%82%D0%B5%D0%B0%D1%82%D1%80'
path_main_dir = '/Users/Valeriya/Desktop'

browser = None
try:
    browser = webdriver.Chrome(path_webdriver)
    browser.implicitly_wait(6)
except WebDriverException as e:
    print("Указан не верный путь к webdriver! Исправите её!")
    exit(1)

try:
    browser.get(url_location)
    name = browser.find_element_by_id('firstHeading').text
    bodyContent = browser.find_elements_by_class_name('mw-parser-output')[0]
    paragraphs = bodyContent.find_elements_by_tag_name('p')
    text = ""
    if paragraphs[0] is not None:
        text += paragraphs[0].text
    if paragraphs[1] is not None:
        text += '\n' + paragraphs[1].text

    infobox_image = browser.find_elements_by_class_name('infobox-image')[0]
    images = infobox_image.find_elements_by_tag_name('img')
    image_links = []
    for image in images:
        image_link = image.get_attribute('src')
        image_links.append(image_link)


    # достаем популярные слова

    all_text = browser.find_element_by_class_name('mw-parser-output')

    txt = all_text.text
    word_list = []

    for word in txt.split():
        clear_word = ''
        for letter in word:
            if letter.isalpha():
                clear_word += letter.lower()

        word_list.append(clear_word)
    print(Counter(word_list).most_common(30))


    # достаем адреса

    geo_coordinates = browser.find_element_by_class_name('mw-kartographer-maplink')
    full_address = browser.find_element_by_xpath("//span[@data-wikidata-property-id]")
    print(geo_coordinates.text)
    print(full_address.text)



    # создание папки
    path_save_dir = path_main_dir + '/' + name
    os.mkdir(path_save_dir)

    # сохранение описания
    with open(path_save_dir + '/description.txt', 'w', encoding='utf8') as f:
        f.write(text)
        f.write('  1)Географические координаты {}   '.format(geo_coordinates.text))
        f.write(' 2)Top 30 слов {}'.format(Counter(word_list).most_common(30)))



    # сохранение фото
    urlretrieve(image_links[0], path_save_dir + '/img.jpg')

except Exception as e:
    print('Ошибка в программе, обратитесь к разработчику.')
    print(e)
finally:
    browser.quit()

