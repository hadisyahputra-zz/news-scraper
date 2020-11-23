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
url = 'https://www.antaranews.com/#tab-popular'
driver.get(url)
time.sleep(3)

WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.XPATH, '//*[@id="tab-popular"]/*')))
arr_article = driver.find_elements_by_xpath('//*[@id="tab-popular"]/*')
df_populer = pd.DataFrame()
for r in arr_article:
    a = r.find_element_by_tag_name('h3').find_element_by_tag_name('a')
    title = a.text
    link = a.get_attribute('href')
    df_populer = df_populer.append({
        'title': title,
        'link': link,
        'scraped_at': datetime.now()
    }, ignore_index=True)
df_populer.to_csv(
    '../scrape result/antaranews/{}_populer_antaranews.csv'.format(today), index=False)
print('Scraping is finished')
driver.close()