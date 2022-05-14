from urllib import request
url ="http://www.dianping.com"

header = {
    "User-Agent":"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:98.0) Gecko/20100101 Firefox/98.0"

}
req=request.Request(url,headers=header)
res=request.urlopen(url)

print(res.geturl())
print()
print(res.getcode())
print()
print(res.info())

html=res.read()
html.decode("utf-8")
print()
# print(html)


