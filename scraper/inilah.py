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
url = 'https://inilah.com/'
driver.get(url)
time.sleep(3)
WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.XPATH, '//*[@id="populer"]/*')))
arr_div = driver.find_elements_by_xpath('//*[@id="populer"]/*')
df_populer = pd.DataFrame()
for d in arr_div:
    a = d.find_element_by_tag_name('a')
    title = a.find_element_by_class_name('pop-title').text
    link = a.get_attribute('href')
    rank = a.find_element_by_class_name('pop-count').text
    df_populer = df_populer.append({
        'title': title,
        'link': link,
        'rank': rank,
        'scraped_at': datetime.now()
    }, ignore_index=True)
df_populer.to_csv('../scrape result/inilah/{}_populer_inilah.csv'.format(today), index=False)
print('Scraping is finished')
driver.close()