from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from urllib.request import urlretrieve
import os


path_webdriver = 'chromedriver.exe'
url_location = 'https://ru.wikipedia.org/wiki/%D0%94%D0%BE%D0%BC_%D0%BF%D0%BE%D0%B4_%D1%88%D0%BF%D0%B8%D0%BB%D0%B5%D0%BC'
path_main_dir = 'E:/Users/vasy/Desktop'


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

    # создание папки
    path_save_dir = path_main_dir + '/' + name
    os.mkdir(path_save_dir)

    # сохранение описания
    with open(path_save_dir + '/description.txt', 'w', encoding='utf8') as f:
        f.write(text)

    # сохранение фото
    urlretrieve(image_links[0], path_save_dir + '/img.jpg')

except Exception as e:
    print('Ошибка в программе, обратитесь к разработчику.')
    print(e)
finally:
    browser.quit()
