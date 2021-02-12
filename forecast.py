"""
Python code to help construct web-scrapers for various open snow forecasts
"""
import random
import requests
from bs4 import BeautifulSoup

class Forecast:
    def __init__(self, url, css_selector='.post > p:nth-child(3)', css_selector_detail='.all-access-content'):
        self.url = url
        self.css_selector = css_selector
        self.css_selector_detail = css_selector_detail
    def get_forecast(self):
        get_summary = requests.get(self.url)
        soup_text = BeautifulSoup(get_summary.text, 'html.parser')
        elems_summary = soup_text.select(self.css_selector)
        summary = elems_summary[0].text
        return summary
    def get_forecast_detailed(self):
        get_summary = requests.get(self.url)
        soup_text = BeautifulSoup(get_summary.text, 'html.parser')
        elems_summary = soup_text.select(self.css_selector)
        elems_details = soup_text.select(self.css_selector_detail)
        


co_daily = Forecast('https://opensnow.com/dailysnow/colorado', '.post > p:nth-child(3)')
co_daily_detailed = Forecast('https://opensnow.com/dailysnow/colorado', '.all-access-content')
uscanada = Forecast('', '')
uscanada_detailed
print(co_daily.url)
print(co_daily.css_selector)



# snow_summary = requests.get('https://opensnow.com/dailysnow/colorado')
# soup = BeautifulSoup(snow_summary.text, 'html.parser')
# elems_summary = soup.select('.post > p:nth-child(3)')
# summary = elems_summary[0].text
# # print(summary)

# elems_forecast = soup.select('.all-access-content')
# # elems_shortforecast2 = soup.select('.all-access-content > p:nth-child(3)')
# detailed_forecast = elems_forecast[0].text
# # short_forecast2 = elems_shortforecast2[0].text

# report = f'{summary} {detailed_forecast}'
# print(report)

# #pagebox > div.page-body > div.d-lg-flex > div.w-100.dailysnow > div.dailysnow-post.content-block > div.post > p
# # .all-access-content > p:nth-child(2)
# # .all-access-content > p:nth-child(3)
# # .all-access-content