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
url = 'https://www.kompas.com/'
driver.get(url)
time.sleep(3)
WebDriverWait(driver, 20).until(
    EC.presence_of_all_elements_located((By.XPATH, '//div[@class="most__wrap clearfix"]/*')))
arr_div_populer = driver.find_elements_by_xpath(
    '//div[@class="most__wrap clearfix"]/*')
df_populer = pd.DataFrame()
for d in arr_div_populer:
    rank = d.find_element_by_class_name('most__count').text
    link = d.find_element_by_tag_name('a').get_attribute('href')
    title = d.find_element_by_tag_name('h4').text
    read = d.find_element_by_class_name('most__read').text
    df_populer = df_populer.append({
        'rank': rank,
        'link': link,
        'title': title,
        'read_count': read,
        'scraped_at': datetime.now()
    }, ignore_index=True)
df_populer.to_csv(
    '../scrape result/kompas/{}_populer_kompas.csv'.format(date), index=False)
print('Scraping is finished')
driver.close()