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
df_trending = pd.DataFrame()
index = 1
while True:
    url = 'https://www.merdeka.com/trending/index{}'.format(index)
    driver.get(url)
    time.sleep(3)
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, '//div[@class="inner-content"]/ul/*')))
        arr_li = driver.find_elements_by_xpath(
            '//div[@class="inner-content"]/ul/*')
        for count in range(len(arr_li)):
            try:
                a = driver.find_element_by_xpath(
                    '//div[@class="inner-content"]/ul/li[{}]/div/h3/a'.format(count+1))
                title = a.text
                link = a.get_attribute('href')
                try:
                    summary = driver.find_element_by_xpath(
                        '//div[@class="inner-content"]/ul/li[{}]/div/div[2]/p'.format(count+1)).text
                except:
                    summary = None
                timestamp = driver.find_element_by_xpath(
                    '//div[@class="inner-content"]/ul/li[{}]/div/div[2]/span[2]'.format(count+1)).text
                df_trending = df_trending.append({
                    'title': title,
                    'link': link,
                    'summary': summary,
                    'timestamp': timestamp,
                    'scraped_at': datetime.now(),
                    'page': index
                }, ignore_index=True)

            except:
                try:
                    a = driver.find_element_by_xpath(
                        '//div[@class="inner-content"]/ul/li[{}]/div/div[2]/h3/a'.format(count+1))
                    title = a.text
                    link = a.get_attribute('href')
                    try:
                        summary = driver.find_element_by_xpath(
                            '//div[@class="inner-content"]/ul/li[{}]/div/div[2]/p'.format(count+1)).text
                    except:
                        summary = None
                    timestamp = driver.find_element_by_xpath(
                        '//div[@class="inner-content"]/ul/li[{}]/div/div[2]/span[2]'.format(count+1)).text
                    df_trending = df_trending.append({
                        'title': title,
                        'link': link,
                        'summary': summary,
                        'timestamp': timestamp,
                        'scraped_at': datetime.now(),
                        'page': index
                    }, ignore_index=True)
                except:
                    pass
    except:
        break
    index += 1
df_trending.to_csv('../scrape result/merdeka/{}_trending_merdeka.csv'.format(date), index=False)
print('Scraping is finished')
driver.close()