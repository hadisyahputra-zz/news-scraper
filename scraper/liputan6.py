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
arr_types = ['hari-ini', 'minggu-ini', 'bulan-ini', 'tahun-ini', 'selamanya']
df_populer = pd.DataFrame()
for t in arr_types:
    p = 1
    arr_web_title = []
    while True:
        url = 'https://www.liputan6.com/indeks/terpopuler/{}?page={}'.format(
            t, p)
        driver.get(url)
        time.sleep(3)
        
        web_title = driver.find_element_by_xpath('//header[@class="header-index-alt"]/h1').text
        print(web_title)
        if len(arr_web_title) > 0 and arr_web_title[-1] == web_title:
            break

        arr_web_title.append(web_title) 
        
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, '//div[@class="articles--list articles--list_rows"]/*')))
        arr_div_artikel = driver.find_elements_by_xpath(
            '//div[@class="articles--list articles--list_rows"]/*')
        for d in arr_div_artikel:
            link = d.find_element_by_tag_name('a').get_attribute('href')
            header = d.find_element_by_tag_name('header')
            category = header.find_element_by_tag_name('a').text
            try:
                timestamp = header.find_element_by_tag_name(
                    'time').get_attribute('datetime')
            except:
                timestamp = None
            title = header.find_element_by_tag_name('h4').text
            summary = d.find_element_by_tag_name(
                'aside').find_element_by_tag_name('div').text
            df_populer = df_populer.append({
                'type': t,
                'page': p,
                'link': link,
                'category': category,
                'timestamp': timestamp,
                'title': title,
                'summary': summary,
                'scraped_at': datetime.now()
            }, ignore_index=True)
        p += 1
df_populer.to_csv('../scrape result/liputan6/{}_populer_liputan6.csv'.format(date), index=False)
driver.close()