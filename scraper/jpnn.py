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
today = datetime.today().strftime("%Y-%m-%d")
from selenium import webdriver

# insert your chrome driver here
driver = webdriver.Chrome(
    '../chromedriver_linux64/chromedriver')
url = 'https://www.jpnn.com/populer'
driver.get(url)
time.sleep(3)
WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.XPATH, '//ul[@class="content-list"]/*')))
arr_li = driver.find_elements_by_xpath(
    '//ul[@class="content-list"]/*')
df_populer = pd.DataFrame()
for li in arr_li:
    category = li.find_element_by_tag_name('strong').text
    timestamp = li.find_element_by_class_name('silver').text
    a = li.find_element_by_tag_name('h1').find_element_by_tag_name('a')
    title = a.text
    link = a.get_attribute('href')
    summary = li.find_element_by_tag_name('p').text
    df_populer = df_populer.append({
        'category': category,
        'timestamp': timestamp,
        'title': title,
        'link': link,
        'summary': summary,
        'scraped_at': datetime.now()
    }, ignore_index=True)
    
# take terpopuler
a_most_popular = driver.find_element_by_xpath(
    '//*[@id="content-utama"]/div[1]/div[1]/div/div/div[1]/h1/a')
title_most_popular = a_most_popular.text
link_most_popular = a_most_popular.get_attribute('href')
category_most_popular = driver.find_element_by_xpath(
    '//*[@id="content-utama"]/div[1]/div[1]/div/div/div[1]/h6/a/strong').text
timestamp_most_popular = driver.find_element_by_xpath(
    '//*[@id="content-utama"]/div[1]/div[1]/div/div/div[1]/h6/a/span').text
summary_most_popular = driver.find_element_by_xpath(
    '//*[@id="content-utama"]/div[1]/div[1]/div/div/div[1]/p').text

df_populer['title_most_popular'] = title_most_popular
df_populer['link_most_popular'] = link_most_popular
df_populer['category_most_popular'] = category_most_popular
df_populer['timestamp_most_popular'] = timestamp_most_popular
df_populer['summary_most_popular'] = summary_most_popular

df_populer.to_csv('../scrape result/jpnn/{}_populer_jpnn.csv'.format(today), index=False)
print('Scraping is finished')
driver.close()