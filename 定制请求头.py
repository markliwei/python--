import requests
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36',
           'Host': 'www.santostang.com'}
r = requests.get('http://www.santostang.com/', headers=headers)
print("响应状态码：", r.status_code)