import pandas as pd
import re
import time
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
url = 'https://tirto.id/'
driver.get(url)
time.sleep(3)
WebDriverWait(driver, 20).until(
    EC.presence_of_all_elements_located((By.XPATH, '//div[@class="container mt-28 container900"]/div[13]/*')))
df_populer = pd.DataFrame()
for i in range(2, 4):
    arr_row = driver.find_elements_by_xpath(
        '//div[@class="container mt-28 container900"]/div[13]/div[{}]/*'.format(i))
    for r in arr_row:
        title = r.find_element_by_tag_name('h1').text
        link = r.find_element_by_tag_name('a').get_attribute('href')
        df_populer = df_populer.append({
            'title': title,
            'link': link,
            'scraped_at': datetime.now()
        }, ignore_index=True)
        
df_populer.to_csv('../scrape result/tirto/{}_populer_tirto.csv'.format(date), index=False)
print('Scraping is finished')
driver.close()