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
arr_types = ['6h', '12h', '1d', '3d', '1w']
df_populer = pd.DataFrame()
for t in arr_types:
    url = 'https://www.tribunnews.com/populer?section=&type={}'.format(t)
    driver.get(url)
    time.sleep(3)
    WebDriverWait(driver, 20).until(
        EC.presence_of_all_elements_located((By.XPATH, '//div[@class="lsi pt10 pb10"]/ul/*')))
    arr_li_populer = driver.find_elements_by_xpath(
        '//div[@class="lsi pt10 pb10"]/ul/*')
    
    count = 1
    for li in arr_li_populer:
        rank = driver.find_element_by_xpath(
            '//div[@class="lsi pt10 pb10"]/ul/li[{}]/div/div[1]'.format(count)).text
        link = li.find_element_by_tag_name('a').get_attribute('href')
        title = li.find_element_by_tag_name('h3').text
        timestamp = li.find_element_by_tag_name('time').text
        df_populer = df_populer.append({
            'type': t,
            'rank': rank,
            'link': link,
            'title': title,
            'timestamp': timestamp,
            'scraped_at': datetime.now()
        }, ignore_index=True)
        count += 1
df_populer.to_csv('../scrape result/tribunnews/{}_populer_tribunnews.csv'.format(date), index=False)
print('Scraping is finished')
driver.close()