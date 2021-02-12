"""
Python code to help construct web-scrapers for various open snow forecasts
"""
import json
from datetime import date
import requests
from bs4 import BeautifulSoup

today = date.today()

class Forecast:
    def __init__(self, url, css_selector='.post > p:nth-child(3)', css_selector_detail='.all-access-content'):
        self.url = url
        self.css_selector = css_selector
        self.css_selector_detail = css_selector_detail
    def get_forecast(self):
        get_summary = requests.get(self.url)
        soup_text = BeautifulSoup(get_summary.text, 'html.parser')
        elems_summary = soup_text.select(self.css_selector)
        return elems_summary[0].text
    def get_forecast_detailed(self):
        get_summary = requests.get(self.url)
        soup_text = BeautifulSoup(get_summary.text, 'html.parser')
        elems_summary = soup_text.select(self.css_selector)
        elems_details = soup_text.select(self.css_selector_detail)
        return f'{elems_summary[0].text} {elems_details[0].text}'


co_daily = Forecast('https://opensnow.com/dailysnow/colorado', '.post > p:nth-child(3)')
co_daily_detailed = Forecast('https://opensnow.com/dailysnow/colorado', '.post > p:nth-child(3)', '.all-access-content')
uscanada = Forecast('https://opensnow.com/dailysnow/usandcanada', '.post > p:nth-child(3)')
uscanada_detailed = Forecast('https://opensnow.com/dailysnow/usandcanada', '.post > p:nth-child(3)', '.all-access-content')

co_daily_forecast = Forecast.get_forecast(co_daily)
co_daily_forecast_detailed = Forecast.get_forecast_detailed(co_daily_detailed)
uscanada_forecast = Forecast.get_forecast(uscanada)
uscanada_forecast_detailed = Forecast.get_forecast_detailed(uscanada_detailed)


forecasts = {}
forecasts['dailysnow'] = []
forecasts['dailysnow'].append({
    'name': 'Colorado Daily Snow',
    'url': 'https://opensnow.com/dailysnow/colorado',
    'text': co_daily_forecast,
    'date_updated': str(today)
})
forecasts['dailysnow'].append({
    'name': 'Colorado Daily Snow Detailed',
    'url': 'https://opensnow.com/dailysnow/colorado',
    'text': co_daily_forecast_detailed,
    'date_updated': str(today)
})
forecasts['dailysnow'].append({
    'name': 'U.S. & Canada Daily Snow',
    'url': 'https://opensnow.com/dailysnow/usandcanada',
    'text': uscanada_forecast,
    'date_updated': str(today)
})
forecasts['dailysnow'].append({
    'name': 'U.S. & Canada Daily Snow Detailed',
    'url': 'https://opensnow.com/dailysnow/usandcanada',
    'text': uscanada_forecast_detailed,
    'date_updated': str(today)
})

with open('forecasts.json', 'w') as outfile:
    json.dump(forecasts, outfile, indent=4, ensure_ascii=False)