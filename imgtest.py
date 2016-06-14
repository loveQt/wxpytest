# -*- coding: utf-8 -*-
import requests
import re
def imgtest(picurl):
    s = requests.session()
    url = 'http://how-old.net/Home/Analyze?isTest=False&source=&version=001'
    header = {
    'Accept-Encoding':'gzip, deflate',
    'User-Agent': "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:34.0) Gecko/20100101 Firefox/34.0",
    'Host': "how-old.net",
    'Referer': "http://how-old.net/",
    'X-Requested-With': "XMLHttpRequest"
        }


    data = {'file':s.get(picurl).content}
    #data = {'file': open(sid+'.jpg', 'rb')}
     #此处打开指定的jpg文件

    r = s.post(url, files=data, headers=header)
    h = r.content
    i = h.replace('\\','')
    #j = eval(i)

    gender = re.search(r'"gender": "(.*?)"rn', i)
    age = re.search(r'"age": (.*?),rn', i)
    if gender.group(1) == 'Male':
        gender1 = '男'
    else:
        gender1 = '女'
    #print gender1
    #print age.group(1)
    datas = [gender1, age.group(1)]
    return datas
#picurl = 'http://ent.cnr.cn/list/20151111/W020151111322757495693.jpg'
#imgtest(picurl)