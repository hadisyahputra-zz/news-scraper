import pandas as pd
import re
import time
import requests
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from datetime import datetime
date = datetime.today().strftime("%Y-%m-%d")
from selenium import webdriver

# insert your chrome driver here
driver = webdriver.Chrome(
    '../chromedriver_linux64/chromedriver')
tags = ['detikcom', 'news', 'finance', 'hot', 'inet', 'sport', 'oto',
        'travel', 'sepakbola', 'food', 'health', 'wolipop']
df_populer = pd.DataFrame()
for t in tags:
    if t == 'detikcom':
        url = 'https://www.detik.com/terpopuler/'
    else:
        url = 'https://www.detik.com/terpopuler/{}'.format(t)
    driver.get(url)
    time.sleep(3)
    
    WebDriverWait(driver, 20).until(
        EC.presence_of_all_elements_located((By.XPATH, '//div[@class="grid-row list-content"]/*')))
    arr_div_populer = driver.find_elements_by_xpath(
        '//div[@class="grid-row list-content"]/*')
    last_update = driver.find_element_by_xpath(
        '//div[@class="page__indeks-info font-base-semibold"]').text
    for d in arr_div_populer:
        link = d.find_element_by_tag_name('a').get_attribute('href')
        title = d.find_element_by_tag_name('h3').text
        div_other_info = d.find_element_by_class_name('media__date')
        category = div_other_info.text
        timestamp = div_other_info.find_element_by_tag_name(
            'span').get_attribute('d-time')
        df_populer = df_populer.append({
            'link': link,
            'title': title,
            'category': re.sub(r'\|.*', '', category).strip(),
            'timestamp': timestamp,
            'last_update': last_update,
            'scraped_at': datetime.now()
        }, ignore_index=True)
df_populer = df_populer.drop_duplicates(subset='link')
df_populer.to_csv(
    '../scrape result/detik/{}_populer_detik.csv'.format(date), index=False)
print('Scraping is finished')
driver.close()