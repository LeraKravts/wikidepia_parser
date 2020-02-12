def find_geo_coordinates(browser):
    return browser.find_element_by_class_name('mw-kartographer-maplink').text


def find_full_address(browser):
    return browser.find_element_by_xpath("//span[@data-wikidata-property-id]").text


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
