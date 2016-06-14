import urllib2
import json


def detect_com(postid):
    r = urllib2.urlopen('http://www.kuaidi100.com/autonumber/autoComNum?text='+postid)
    h = r.read()
    #j = json.dumps(h)
    #k = json.loads(j)
    k = eval(h)
    kuaiditpye = k["auto"][0]['comCode']
    #print kuaiditpye
    return kuaiditpye


def cxkd(postid):
    kuaiditype = detect_com(postid)
    r = urllib2.urlopen('http://www.kuaidi100.com/query?type='+kuaiditype+'&postid='+postid)
    h = r.read()
    # print(r.json())
    #j = json.dumps(h)
    j = eval(h)
    # print(j)
    # print(j.keys())
    # print(j['data'])
    outcome = ''
    for c in j['data']:
        outcome = outcome + c['time']+'   '+c['context']+'\n'
    return outcome

#a = cxkd('280472503105')
#print a


