import pandas as pd
import re
import time
import requests
import json
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from datetime import datetime
date = datetime.today().strftime("%Y-%m-%d")
from selenium import webdriver

def scroll_down():
    """A method for scrolling the page."""
    last_height = driver.execute_script(
        "return document.body.scrollHeight")

    while True:
        driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)

        new_height = driver.execute_script(
            "return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

# insert your chrome driver here
driver = webdriver.Chrome(
    '../chromedriver_linux64/chromedriver')
url = 'https://kumparan.com/trending'
driver.get(url)
time.sleep(3)
scroll_down()
arr_div_trending = driver.find_elements_by_xpath(
    '//div[@class="Viewweb__StyledView-p5eu6e-0 hWzdds"]/*')
print(len(arr_div_trending))
df_trending = pd.DataFrame()
for d in arr_div_trending:
    try:
	    link = d.find_element_by_tag_name('a').get_attribute('href')
	    slug = re.sub(r'\/berita-viral\/', '', link)
	    api = 'https://cdn-graphql-v4.kumparan.com/query?operationName=FindStoryBySlug&variables=%7B%22slug%22%3A%22{}%22%7D&extensions=%7B%22persistedQuery%22%3A%7B%22version%22%3A1%2C%22sha256Hash%22%3A%22c05aebe153dfd967395d35aa6f9516d6141475b2223b445d01248b79b5506223%22%7D%7D&cache-ttl=10'.format(
	        slug)
	    print(api)
	    response = requests.get(api)
	    data = json.loads(response.content)
	    df_temp = pd.DataFrame.from_dict(
	        data['data']).T.reset_index().drop(columns=['index'])
	    df_trending = df_trending.append(df_temp, ignore_index=True)
    except:
        pass
df_trending.to_csv('../scrape result/kumparan/{}_trending_kumparan.csv'.format(date), index=False)
print('Scraping is finished')
driver.close()