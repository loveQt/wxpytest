import requests
import json
global s
s = requests.session()
headers = {
    'Host':'www.kuaidi100.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate',
    'Connection': 'keep-alive',
}


def detect_com(postid):
    r = s.get('http://www.kuaidi100.com/autonumber/autoComNum?text='+postid)
    j = r.json()
    kuaiditpye = j["auto"][0]['comCode']
    #print kuaiditpye
    return kuaiditpye


def cxkd(postid):
    kuaiditype = detect_com(postid)
    r = s.post('http://www.kuaidi100.com/query?type='+kuaiditype+'&postid='+postid, headers=headers)
    # print(r.json())
    j = r.json()
    # print(j)
    # print(j.keys())
    # print(j['data'])
    outcome = ''
    for c in j['data']:
        outcome = outcome + c['time']+'   '+c['context']+'\n'
    return outcome

#a = cxkd('280472503105')
#print a


