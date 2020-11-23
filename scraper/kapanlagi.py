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
df_trending = pd.DataFrame()
index = 1
while True:
    if index <= 1:
        url = 'https://www.kapanlagi.com/trending/index.html'
    else:
        url = 'https://www.kapanlagi.com/trending/index{}.html'.format(index)
        headline_title = None
        headline_link = None

    driver.get(url)
    time.sleep(3)

    if index <= 1:
        a_headline = driver.find_element_by_xpath(
            '//h2[@class="title-tag"]/a')
        headline_title = a_headline.text
        headline_link = a_headline.get_attribute('href')
    
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, '//li[@id="tagli"]')))
        arr_li = driver.find_elements_by_xpath('//li[@id="tagli"]')
        for li in arr_li:
            a = li.find_element_by_tag_name('div').find_element_by_tag_name('a')
            link = a.get_attribute('href')
            title = a.text
            date = li.find_element_by_class_name('date').text
            df_trending = df_trending.append({
                'link': link,
                'title': title,
                'date': date,
                'scraped_at': datetime.now(),
                'page': index,
                'headline_title': headline_title,
                'headline_link': headline_link
            }, ignore_index=True)
    except:
        break
    index += 1
    
df_trending.to_csv('../scrape result/kapanlagi/{}_trending_kapanlagi.csv'.format(today), index=False)
print('Scraping is finished')
driver.close()