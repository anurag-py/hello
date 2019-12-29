import requests
import re
from bs4 import BeautifulSoup

def weather_data():

    
    url = 'https://www.weatheronline.in/India/Mathura.htm'

    data = requests.get(url)
    # print(data.text)
    soup = BeautifulSoup(data.text, 'html.parser')
    a = soup.findAll('td')
    a = str(a)
    # print(a)
    b = a.split("""class="Temp_minus">""", 2)
    min_str = b[1]
    temp_min = min_str.split('°',2)
    temp_min = temp_min[0]
    # print(temp_min)
    c = a.split("""class="Temp_plus">""", 2)
    max_str = c[1]
    temp_max = max_str.split('°',2)
    temp_max = temp_max[0]
    # print(temp_max)
    temp = {temp_max,temp_min}
    return(temp)

    

res = weather_data()
print(res)