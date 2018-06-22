import requests
from bs4 import BeautifulSoup
import pandas as pd
def get_companys(str,type):
    companys = [];
    for li in str.find_all('li'):
        # print li.a['href']
        href = li.a['href']
        if(type==5 or type==6):
            code = href[-5:]
            name = li.a.string[6:]
        else:
            code = href[-6:]
            name = li.a.string[7:]
        company = [code,name,type]
        companys.append(company)
    return companys

if __name__ == '__main__':
    content = requests.get("http://www.cninfo.com.cn/cninfo-new/information/companylist").content
    soup = BeautifulSoup(content,"lxml")
    all_companys = []
    str1 = soup.find('div',id='con-a-1')
    all_companys.extend(get_companys(str1,1))
    # str2 = soup.find('div',id='con-a-2')
    # all_companys.extend(get_companys(str2,2))
    # str3 = soup.find('div',id='con-a-3')
    # all_companys.extend(get_companys(str3,3))
    str4 = soup.find('div',id='con-a-4')
    all_companys.extend(get_companys(str4,4))
    # str5 = soup.find('div', id='con-a-5')
    # all_companys.extend(get_companys(str5,5))
    # str6 = soup.find('div', id='con-a-6')
    # all_companys.extend(get_companys(str6,6))
    data = pd.DataFrame(all_companys,columns=['code','name','type'])
    data.to_csv("companys_zhuban.csv",index_label='no',encoding='utf-8')