import requests
from bs4 import BeautifulSoup

url = 'https://hr.tencent.com/position.php?keywords=python'

headers = {
"User-Agent":"User-Agent, Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"
}

rep = requests.get(url,headers=headers)
soup = BeautifulSoup(rep.content.decode('utf-8'),'lxml')

tr_list = soup.select('.tablelist tr')

for tr in tr_list:
    print(tr.text)