# _*_ coding:utf-8 _*_
__author__ = 'Tanz'
__date__ = '2020/7/31 14:11'
import yagmail,datetime

def send_email():
    yag = yagmail.SMTP(user='1432957306@qq.com', password='kuytmivxpnaliijg', host='smtp.qq.com')
    # 邮件正文
    contents = ['昇云星河接口']
    # 邮件主题
    subject = datetime.datetime.now().strftime('%Y-%m-%d') + ' 接口测试报告'
    yag.send('1432957306@qq.com', subject, contents,'C:/Users/pcsales/Desktop/ApiAuto/report/api_test.html')
    yag.close()