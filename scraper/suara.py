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
url = 'https://suara.com/'
driver.get(url)
time.sleep(3)

WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.XPATH, '/html/body/div[3]/div[3]/article[2]/div/div[4]/div/div/ul/*')))
arr_li = driver.find_elements_by_xpath(
    '/html/body/div[3]/div[3]/article[2]/div/div[4]/div/div/ul/*')
df_populer = pd.DataFrame()
for li in arr_li:
    category_time = li.find_element_by_tag_name('span').text
    category = re.sub(r'\|.*', '', category_time).strip()
    timestamp = re.sub(r'.*\|', '', category_time).strip()
    h3 = li.find_element_by_tag_name('h3')
    link = h3.find_element_by_tag_name('a').get_attribute('href')
    title = h3.text
    df_populer = df_populer.append({
        'category': category,
        'time': timestamp,
        'link': link,
        'title': title,
        'scraped_at': datetime.now()
    }, ignore_index=True)
df_populer.to_csv('../scrape result/suara/{}_populer_suara.csv'.format(today), index=False)
print('Scraping is finished')
driver.close()