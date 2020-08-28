# _*_ coding:utf-8 _*_
__author__ = 'Tanz'
__date__ = '2020/8/4 17:53'
import re,json,requests

a={"clientType": "web", "code": "1", "data": {"dataId": "1295183064116371456", "taskApplyId": "8a8a9ca473e225d00173fa3590511baf"}, "loginName": "8a8a9ca473e225d00173e24d5b2e006e", "message": "操作成功！", "msgCode": 1, "token": "8a8a9ca473e225d00173e24d5b2e006e,08d8283a49790441517079afde53852b"}
print(a['data']['taskApplyId'])