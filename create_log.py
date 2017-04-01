import requests
import re
from bs4 import BeautifulSoup
S = requests.session()

def login():
    login_data = {
        'username': 'lijinsong@eqxiu.com',
        'password': '720822'
    }

    login_url = 'http://max.eqxiu.com/login'
    S.post(login_url, login_data)


def make_url_page():
    regex = '共\s\w{1,5}\s\w'
    url = 'http://max.eqxiu.com/m/eqs/stat/scene'
    html = S.get(url).text
    sum_page = re.findall(regex,html)[0].replace('共','').replace(' ','').replace('条','')
    return int(sum_page)

def page_info():
    count = 0
    while count != make_url_page():
        count += 1
        url = 'http://max.eqxiu.com/m/eqs/stat/scene.html?pageNo={}'.format(count)
        soup = BeautifulSoup(S.get(url).text,'lxml')
        lxml = soup.select('body > div > div > div > table > tbody > tr > td')
        print(lxml)
login()
# make_url_page()
page_info()
