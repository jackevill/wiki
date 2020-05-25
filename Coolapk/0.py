#!/usr/bin/python
import re
import requests
import urllib
for i in range(2014, 2020):
    url = 'https://www.wandoujia.com/apps/998339/history_y' + str(i)
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)
    data = response.read()
    data = data.decode('utf-8')
    li = re.findall("https://www.wandoujia.com/apps/998339/history_v[0-9]+", data, flags=0)
    s = len(li)
    for n in range(1, s):
        url = li[n]
        request = urllib.request.Request(url)
        response = urllib.request.urlopen(request)
        data = response.read()
        data = data.decode('utf-8')
        title = re.findall("<title>.*</title>", data, flags=0)
        version = re.findall("v[0-9.]{1,8}", str(title), flags=0)
        version = str(version[0]) + ".apk"
        l = re.findall("https://android-apps.pp.cn/[a-zA-Z0-9_/]{1,}.apk", data, flags=0)
        f=requests.get(l[1])
        with open(version,"wb") as code:
            code.write(f.content)
