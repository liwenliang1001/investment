import requests
from bs4 import BeautifulSoup
response = requests.get("http://www.cninfo.com.cn/cninfo-new/information/companylist")
content = requests.get("http://www.cninfo.com.cn/cninfo-new/information/companylist").content
# print "response headers:", response.headers
# print "content:", content
soup = BeautifulSoup(content,"lxml")
# print soup.prettify()
str = soup.find('div',id='con-a-1')
# print str
for li in str.find_all('li'):
    print li.a['href']
    print li.a.string