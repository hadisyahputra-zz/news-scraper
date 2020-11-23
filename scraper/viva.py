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
df_populer = pd.DataFrame()
url = 'https://www.viva.co.id/'
driver.get(url)
time.sleep(3)

WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.XPATH, '//div[@class="side-popular"]/ul/*')))
arr_li = driver.find_elements_by_xpath(
    '//div[@class="side-popular"]/ul/*')
for li in arr_li:
    try:
        a = li.find_element_by_tag_name('a')
        title = a.text
        link = a.get_attribute('href')
        df_populer = df_populer.append({
            'link': link,
            'title': title,
            'scraped_at': datetime.now()
        }, ignore_index=True)
    except:
        pass
df_populer.to_csv('../scrape result/viva/{}_populer_viva.csv'.format(today), index=False)
print('Scraping is finished')
driver.close()