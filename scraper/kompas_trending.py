import sys
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
from selenium import webdriver

# scraped_date = '2020-10-12'
scraped_date = sys.argv[1]

# insert your chrome driver here
driver = webdriver.Chrome(
    '../chromedriver_linux64/chromedriver')
df_trending = pd.DataFrame()
p = 1
while True:
    url = 'https://www.kompas.com/tren/search/{}/{}'.format(scraped_date, p)
    driver.get(url)
    time.sleep(3)
    arr_div = driver.find_elements_by_xpath('//div[@class="latest--news mt2 clearfix"]/*')
    if len(arr_div) <= 0:
        break
    else:
        for d in arr_div:
            a = d.find_element_by_tag_name('h3').find_element_by_tag_name('a')
            title = a.text
            link = a.get_attribute('href')
            timestamp = d.find_element_by_class_name('article__date').text
            df_trending = df_trending.append({
                'page': p,
                'title': title,
                'link': link,
                'timestamp': timestamp,
                'scraped_at': datetime.now()
            }, ignore_index=True)
        p += 1

df_trending.to_csv('../scrape result/kompas/{}_trending_kompas.csv'.format(scraped_date), index=False)
print('Scraping is finished')
driver.close()