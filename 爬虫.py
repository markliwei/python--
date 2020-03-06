import requests
from bs4 import BeautifulSoup
import re
url = 'http://www.cntour.cn/'
headers = {'User - Agent': 'Mozilla / 5.0(Windows NT 10.0; Win64;x64) AppleWebKit / 537.36(KHTML, like Gecko) /'
                           'Chrome / 64.03282.140 Safari / 537.36 Edge / 17.17134'}
proxies= {
    "http": "http://10.10.1.10:3128",
    "https": "http://10.10.1.10:1080",
}
response = requests.get(url, proxies=proxies)
soup = BeautifulSoup(response.text, 'lxml')
data = soup.select('#main > div > div.mtop.firstMod.clearfix > div.centerBox > ul.newsList > li > a')
for item in data:
    result = {
        'title': item.get_text(),
        'link': item.get('href'),
       'ID': re.findall('\d+', item.get('href'))
    }
    print(result)




