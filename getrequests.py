from bs4 import BeautifulSoup
import requests

url="http://wsjkw.sc.gov.cn/scwsjkw/gzbd/fyzt.shtml"
header={
    "Host":"wsjkw.sc.gov.cn",
    "User-Agent":"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:98.0) Gecko/20100101 Firefox/98.0"
}

resp=requests.get(url,headers=header)
# print(resp.encoding)
# print(resp.status_code)
resp.encoding="utf-8"
html=resp.text
# print(html)
soup=BeautifulSoup(html)
for i in soup.find_all("a"):
    print(i)