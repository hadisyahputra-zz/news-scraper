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
url = 'https://www.sindonews.com'
driver.get(url)
time.sleep(3)
WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.XPATH, '//div[@class="populer"]/ul/*')))
arr_li = driver.find_elements_by_xpath('//div[@class="populer"]/ul/*')
df_populer = pd.DataFrame()
for li in arr_li:
    a = li.find_element_by_tag_name('a')
    title = a.text
    link = a.get_attribute('href')
    df_populer = df_populer.append({
        'title': title,
        'link': link,
        'scraped_at': datetime.now()
    }, ignore_index=True)
df_populer.to_csv('../scrape result/sindonews/{}_populer_sindonews.csv'.format(today), index=False)
print('Scraping is finished')
driver.close()