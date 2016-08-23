# -*- coding:utf-8 -*-
'''
Created on 2016.8.18

@author: Sanchez.Zhu
'''
import urllib2
import smtplib
from email.mime.text import MIMEText
from email.header import Header


class SinaMktData:
    
    # 初始化方法，定义一些变量
    def __init__(self):
        self.pageIndex = 1
        self.user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        # 初始化headers
        self.headers = { 'User-Agent' : self.user_agent }
        
    # 获取新浪行情
    def reqMktData(self, market, stkCode):
        try:
            url = 'http://hq.sinajs.cn/list=' + market + stkCode
            # 构建请求的request
            request = urllib2.Request(url, headers=self.headers)
            # 利用urlopen获取页面代码
            response = urllib2.urlopen(request)
            # 将页面转化为gbk编码
            origData = response.read().decode('gbk').encode("utf-8")
            
            return origData

        except urllib2.URLError, e:
            if hasattr(e, "reason"):
                print u"Connect Sina MarketData failed, reason :", e.reason
                return None
            
    # 解析新浪行情
    def parseMktData(self, stkCode, origData): 
        # 解析行情字符串
        '''
        0：”大秦铁路”，股票名字；stkName
        1：”6.350″，今日开盘价；openPrice
        2：”6.350″，昨日收盘价；closePrice
        3：”6.360″，当前价格； newPrice
        4：”6.380″，今日最高价；highestPrice
        5：”6.340″，今日最低价；lowestPrice
        6：”6.350″，竞买价，即“买一”报价；
        7：”6.360″，竞卖价，即“卖一”报价；
        8：”18085467″，成交的股票数，由于股票交易以一百股为基本单位，所以在使用时，通常把该值除以一百； exchKnockQty
        9：”114913572″，成交金额，单位为“元”，为了一目了然，通常以“万元”为成交金额的单位，所以通常把该值除以一万； exchKnockAmt
        '''
        
        temp = origData.split("\"")
        temp = temp[1].split(",")
        
        closePrice = float(temp[2])  # 昨收
        newPrice = float(temp[3])  # 今收
        highestPrice = float(temp[4])  # 最高
        lowestPrice = float(temp[5])  # 最低
        exchMatchQty = long(round(float(temp[8]) / 100))  # 市场成交量（手）
        exchMatchAmt = float(temp[9]);  # 市场成交金额
        
        if (exchMatchAmt >= 100000000):
            exchMatchAmt = str(long(round(exchMatchAmt / 100000000))) + '亿'
        elif(exchMatchAmt >= 10000):
            exchMatchAmt = str(long(round(exchMatchAmt / 10000))) + '万'
        
        # 涨跌额
        updownPrice = round(newPrice - closePrice, 2) 
        # 涨跌幅
        updownPercent = round((newPrice - closePrice) / closePrice * 100, 2)
        # 当日振幅
        tdUpdownPercent = round((highestPrice - lowestPrice) / newPrice * 100, 2)
        
        mktData = '证券代码:' + stkCode + ', 证券名称:' + temp[0] + ', 今开:' + temp[1] + ', 昨收:' + temp[2] + ', 最新:' + temp[3] + ', 最高:' + temp[4] + ', 最低:' + temp[5] + ', 成交量:' + str(exchMatchQty) + '手, 成交金额:' + str(exchMatchAmt) + ', 涨跌额:' + str(updownPrice) + ', 涨跌幅:' + str(updownPercent) + '%, 振幅:' + str(tdUpdownPercent) + '%\n'     
        
        return mktData
    
    # 获取行情信息（字符串）
    def getMktData(self, market='sh', stkCode='000001'):
        origData = self.reqMktData(market, stkCode)
        return self.parseMktData(stkCode, origData)
    
    # 发送邮件
    def sendMail(self, mktData):
        # 第三方 SMTP 服务
        mail_host = "smtp.qq.com"  # 设置服务器
        mail_user = "279143189"  # 用户名
        mail_pass = "lmzxfrktyfepbicg"  # 口令 
        
        sender = '279143189@qq.com'
        receivers = ['279143189@qq.com']
        
        message = MIMEText(mktData, 'plain', 'utf-8')
        message['From'] = Header("行情服务器", 'utf-8')
        message['To'] = Header("279143189@qq.com", 'utf-8')
        
        subject = '行情速递'
        message['Subject'] = Header(subject, 'utf-8')
        
        try:
            smtpObj = smtplib.SMTP()
            smtpObj.connect(mail_host, 587)  # SSL端口
            smtpObj.starttls()
            smtpObj.login(mail_user, mail_pass)  
            smtpObj.sendmail(sender, receivers, message.as_string())
            print "邮件发送成功"
        except smtplib.SMTPException:
            print "Error: 无法发送邮件"
        

obj = SinaMktData()
obj.sendMail(obj.getMktData() + obj.getMktData('sz', '002440'))

