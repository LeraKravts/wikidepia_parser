#! /usr/bin/env python
# -*- coding: utf-8 -*-
import collections
from collections import Counter
import time
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
import csv
import urllib
from urllib.request import urlretrieve
import urllib3


try:
    browser = webdriver.Chrome('/Users/valeriya/node_modules/chromedriver/lib/chromedriver/chromedriver')
    browser.implicitly_wait(6)

except WebDriverException:
    print("Wrong webdriver link! Change it")
    exit(1)

try:
    browser.get('https://ru.wikipedia.org/wiki/Красная_площадь')


    # --находим самые популярные слова--

    def get_popular_words():
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

    get_popular_words()


    # достаем адреса
    def get_address():
        geo_coordinates = browser.find_element_by_class_name('mw-kartographer-maplink')
        full_address = browser.find_element_by_xpath("//span[@data-wikidata-property-id]")
        print(geo_coordinates.text)
        print(full_address.text)
    get_address()

except Exception as e:
    print('Ошибка в программе')
    print(e)


finally:
    browser.quit()


