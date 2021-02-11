"""
Python code to help construct web-scrapers for various open snow forecasts
"""

import random
import requests
from bs4 import BeautifulSoup

snow_summary = requests.get('https://opensnow.com/dailysnow/colorado')
soup = BeautifulSoup(snow_summary.text, 'html.parser')
elems_summary = soup.select('.post > p:nth-child(3)')
summary = elems_summary[0].text
# print(summary)

elems_shortforecast1 = soup.select('.all-access-content')
# elems_shortforecast2 = soup.select('.all-access-content > p:nth-child(3)')
short_forecast = elems_shortforecast1[0].text
# short_forecast2 = elems_shortforecast2[0].text
print(short_forecast)

#pagebox > div.page-body > div.d-lg-flex > div.w-100.dailysnow > div.dailysnow-post.content-block > div.post > p
# .all-access-content > p:nth-child(2)
# .all-access-content > p:nth-child(3)
# .all-access-content