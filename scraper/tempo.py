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
arr_types = ['6jam', '12jam', '1hari', '1minggu', '1bulan', '1tahun']
df_populer = pd.DataFrame()
for t in arr_types:
    url = 'https://www.tempo.co/populer/?tipe={}'.format(t)
    driver.get(url)
    time.sleep(3)
    WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.XPATH, '//ul[@class="wrapper"]/*')))
    arr_li = driver.find_elements_by_xpath(
        '//ul[@class="wrapper"]/*')
    for li in arr_li:
        link = li.find_element_by_tag_name('a').get_attribute('href')
        title = li.find_element_by_tag_name('h2').text
        summary = li.find_element_by_tag_name('p').text
        timestamp = li.find_element_by_tag_name('span').text
        df_populer = df_populer.append({
            'type': t,
            'link': link,
            'title': title,
            'summary': summary,
            'timestamp': timestamp,
            'scraped_at': datetime.now()
        }, ignore_index=True)
df_populer.to_csv('../scrape result/tempo/{}_populer_tempo.csv'.format(today), index=False)
print('Scraping is finished')
driver.close()