# -*- coding: utf-8 -*-
import hashlib
import web
import lxml
import time
import requests
import os
import urllib2
import json
from lxml import etree
import cookielib
import re
import random
import cxkd
from imgtest import *

class WeixinInterface:

    def __init__(self):
        self.app_root = os.path.dirname(__file__)
        self.templates_root = os.path.join(self.app_root, 'templates')
        self.render = web.template.render(self.templates_root)

    def GET(self):
        #获取输入参数
        data = web.input()
        signature=data.signature
        timestamp=data.timestamp
        nonce=data.nonce
        echostr = data.echostr
        #自己的token
        token="wxpytest" #这里改写你在微信公众平台里输入的token
        #字典序排序
        list=[token,timestamp,nonce]
        list.sort()
        sha1=hashlib.sha1()
        map(sha1.update,list)
        hashcode=sha1.hexdigest()
        #sha1加密算法

        #如果是来自微信的请求，则回复echostr
        if hashcode == signature:
            return echostr

    def POST(self):
        str_xml = web.data() #获得post来的数据
        xml = etree.fromstring(str_xml)#进行XML解析
        #content=xml.find("Content").text#获得用户所输入的内容
        msgType=xml.find("MsgType").text
        fromUser=xml.find("FromUserName").text
        toUser=xml.find("ToUserName").text
        #picurl = xml.find('PicUrl').text
        #return self.render.reply_text(fromUser,toUser,int(time.time()), content)
        if msgType == 'image':
            try:
                picurl = xml.find('PicUrl').text
                datas = imgtest(picurl)
                return self.render.reply_text(fromUser, toUser, int(time.time()), '图中人物性别为'+datas[0]+'\n'+'年龄为'+datas[1])
            except:
                return self.render.reply_text(fromUser, toUser, int(time.time()),  '识别失败，换张图片试试吧')
        else:
            content = xml.find("Content").text  # 获得用户所输入的内容
            if content[0:2] == u"快递":
                post = str(content[2:])
                #result = cxkd.cxkd('PQ00708467161')

                r = urllib2.urlopen('http://www.kuaidi100.com/autonumber/autoComNum?text='+post)
                h = r.read()
                k = eval(h)
                kuaidi = k["auto"][0]['comCode']
                '''
                j = requests.get('http://www.kuaidi100.com/query?type=huitongkuaidi&postid=280472503105')
                l = j.text
                #l = j.read()
                #m = eval(l)
                #outcome = ''
                #for c in m['data']:
                '''
                    #outcome = outcome + c['time']+'   '+c['context']+'\n'

                return self.render.reply_text(fromUser,toUser,int(time.time()), kuaidi)

            else:
                return self.render.reply_text(fromUser,toUser,int(time.time()), content)




