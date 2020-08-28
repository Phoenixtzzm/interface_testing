# _*_ coding:utf-8 _*_
__author__ = 'Tanz'
__date__ = '2018/6/17 17:04'
import requests
import json

local = 'https://admin.racingoo.com/eApi'

# url = local + '/user/login'
# header = {
#     'Content-Type': 'application/json',
#     'Authorization': 'Basic SmllV2VpZnU6SmllV2VpZnUyMDE0MDY=',
#
# }
# data = {
#     'mobile': '15895711766',
#     'password': '123456',
# }
# # python的值转换为json格式的字符串; loads json格式的字符串转换成python的数据类型(dict)
# json_string = json.dumps(data)
#
# result = requests.post(headers=header,url=url,json=data).json()
#
# token = result['data']
#
# url_getUserInfo = local + '/user/getUserInfo'
# header_userInfo = {
# 'Content-Type':'application/json',
# 'Authorization':'Basic SmllV2VpZnU6SmllV2VpZnUyMDE0MDY=',
# 'AuthToken':token
# }
#
# user_info_result = requests.get(url=url_getUserInfo,headers=header_userInfo)
# user = user_info_result.json()
# print(json.dumps(user,indent=2,ensure_ascii=False))
#
#
#
#
#
upLoadPic_url = local + '/common/UploadImg'

files = {'123.png': open('C:/Users/14329/Desktop/2.png', 'rb')}


r = requests.post(url=upLoadPic_url,files=files)
print(r.json())


urll = 'https://www.baidu.com'

re = requests.get(url=urll).content
with open('C:/Users/14329/Desktop/123.apk','wb') as f:
    f.write(re)












saveInfoHeaders = {

    "avatar":"头像.png",
    "nickname":"Tanz",
    "gender":"1",
    "email":"1432957306@qq.com",
    "is_private":"1"

}