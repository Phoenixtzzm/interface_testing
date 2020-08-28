# _*_ coding:utf-8 _*_
__author__ = 'Tanz'
__date__ = '2018/7/28 12:39'
import requests,json,pymssql
from util.handle_result import HandleResult

# header = {
#     "Accept": "*/*",
#     "Accept-Encoding": "gzip, deflate, br",
#     "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
#
# }
# url = 'https://gzzqa.cssiot.com.cn:8465/cssmfw/customHome/doGetCustomerPrivateInfo/web'
# a=json.dumps({"mobileNo":"18506161966","privateUrl":""})
# files = {'jsonStr': (a)}
#
# r = requests.post(url, data=files,headers=header)
# print(r.text)

''' 
data_dict = json.loads(data)
data_str = data_dict['jsonStr']
form_data = json.dumps(data_str)
data = {'jsonStr':(form_data)}
'''


#
# exal = {"code": "4009", "message": "主人，小昇生病了，请您联系系统管理员，谢谢！", "msgCode": -1}
# a=exal.keys()
# data = []
# data1=[]
# data2={}
# b=exal.values()
# c=exal.items()
# for key,value in c:
#     data.append(key)
# for key,value in c:
#     data1.append(value)
# print(data)
# print(data1)
# neww = dict(zip(data,data1))
# for key,value in c:
#     va = json.dumps(value)
#     data2[key]=va
# print(data2)


from deepdiff import DeepDiff
from pprint import pprint
b= {
    "clientType": "web",
    "code": "1",
    "data": {
        "page": {
            "allPage": 2,
            "count": 71,
            "disabled": False,
            "first": 0,
            "firstPage": False,
            "firstResult": 0,
            "funcName": "page",
            "last": 0,
            "lastPage": False,
            "lastResult": 50,
            "list": [
                {
                    "checked": False,
                    "id": "1270281589196201984",
                    "showName": "子工程1"
                },

                {
                    "checked": False,
                    "id": "1278929645521215488",
                    "showName": "子项目121"
                },
                {
                    "checked": False,
                    "id": "1278930559741075456",
                    "showName": "子项目999"
                },


                {
                    "checked": False,
                    "id": "1285501503670460416",
                    "showName": "630.12"
                },
                {
                    "checked": False,
                    "id": "1285508757622759424",
                    "showName": "0721桩基"
                },
                {
                    "checked": False,
                    "id": "1285813408448520192",
                    "showName": "233"
                },
                {
                    "checked": False,
                    "id": "1286118578873049088",
                    "showName": "0723桩基工程"
                },
                {
                    "checked": False,
                    "id": "1286193936649560064",
                    "showName": "555"
                },
                {
                    "checked": False,
                    "id": "1287228752157351936",
                    "showName": "0726项目1桩基工程"
                },
                {
                    "checked": False,
                    "id": "1287278302804975616",
                    "showName": "模拟07261"
                },
                {
                    "checked": False,
                    "id": "1287701180096585728",
                    "showName": "回归07271"
                },
                {
                    "checked": False,
                    "id": "1289033287964172288",
                    "showName": "测试"
                },
                {
                    "checked": False,
                    "id": "1289067270307454976",
                    "showName": "测试"
                },
                {
                    "checked": False,
                    "id": "1289070962205138944",
                    "showName": "测试"
                },
                {
                    "checked": False,
                    "id": "1289088750428758016",
                    "showName": "测试"
                },
                {
                    "checked": False,
                    "id": "1289089553159823360",
                    "showName": "测试"
                },
                {
                    "checked": False,
                    "id": "1289096990403207168",
                    "showName": "测试"
                },
                {
                    "checked": False,
                    "id": "1289097066789871616",
                    "showName": "测试"
                },
                {
                    "checked": False,
                    "id": "1289097440389111808",
                    "showName": "测试"
                },
                {
                    "checked": False,
                    "id": "1290189771217444864",
                    "showName": "测试"
                },
                {
                    "checked": False,
                    "id": "1290190481858371584",
                    "showName": "测试"
                }
            ],
            "maxResults": 50,
            "next": 2,
            "notCount": False,
            "orderBy": "",
            "pageNo": 1,
            "pageSize": 50,
            "prev": 0,
            "totalPage": 0
        }
    },
    "loginName": "8a8a9ca4736b23ce01736f6200f41771",
    "message": "操作成功！",
    "msgCode": 1,
    "token": "8a8a9ca4736b23ce01736f6200f41771,318ebaee3fa6f41fcaea331d40ed38a4"
}

a= {
    "clientType": "web",
    "code": "1",
    "data": {
        "isRelateChildForm": "1",
        "page": {
            "allPage": 1,
            "count": 29,
            "disabled": False,
            "first": 0,
            "firstPage": False,
            "firstResult": 0,
            "funcName": "page",
            "last": 0,
            "lastPage": False,
            "lastResult": 29,
            "list": [
                {
                    "id": "1286117884556353536",
                    "showName": "0723测试1",
                    "8a8a9ca4729755f0017297a7e79003e7": {
                        "checked": False,
                        "id": "1286117884556353536",
                        "showName": "0723测试1"
                    },
                    "8a8a9ca4729755f0017297a7e79003e3": "xmxx2020-070034",
                    "8a8a9ca4729755f0017297a7e7930404": [
                        {
                            "checked": False,
                            "id": "8a8a9ca470f7120a0170f752dd9a04e4",
                            "showName": "银河小分队",
                            "type": "8"
                        }
                    ],
                    "isChildForm": "1",
                    "isMainToChild": ""
                },
                {
                    "id": "1288718305829462016",
                    "showName": "测试",
                    "8a8a9ca4729755f0017297a7e79003e7": {
                        "checked": False,
                        "id": "1288718305829462016",
                        "showName": "测试"
                    },
                    "8a8a9ca4729755f0017297a7e79003e3": "xmxx2020-070052",
                    "8a8a9ca4729755f0017297a7e7930404": [
                        {
                            "checked": False,
                            "id": "8a8a9ca470f7120a0170f752dd9a04e4",
                            "showName": "银河小分队",
                            "type": "8"
                        }
                    ],
                    "isChildForm": "1",
                    "isMainToChild": ""
                },
                {
                    "id": "1288718582691274752",
                    "showName": "周一新增测试数据",
                    "8a8a9ca4729755f0017297a7e79003e7": {
                        "checked": False,
                        "id": "1288718582691274752",
                        "showName": "周一新增测试数据"
                    },
                    "8a8a9ca4729755f0017297a7e79003e3": "1290170272917364736",
                    "8a8a9ca4729755f0017297a7e7930404": [
                        {
                            "checked": False,
                            "id": "8a8a9ca470f7120a0170f752dd9a04e4",
                            "showName": "银河小分队",
                            "type": "8"
                        }
                    ],
                    "isChildForm": "1",
                    "isMainToChild": ""
                },
                {
                    "id": "1288719780219592704",
                    "showName": "测试数据",
                    "8a8a9ca4729755f0017297a7e79003e7": {
                        "checked": False,
                        "id": "1288719780219592704",
                        "showName": "测试数据"
                    },
                    "8a8a9ca4729755f0017297a7e79003e3": "xmxx2020-070055",
                    "8a8a9ca4729755f0017297a7e7930404": [
                        {
                            "checked": False,
                            "id": "8a8a9ca470f7120a0170f752dd9a04e4",
                            "showName": "银河小分队",
                            "type": "8"
                        }
                    ],
                    "isChildForm": "1",
                    "isMainToChild": ""
                },
                {
                    "id": "1289094747444617216",
                    "showName": "测试数据",
                    "8a8a9ca4729755f0017297a7e79003e7": {
                        "checked": False,
                        "id": "1289094747444617216",
                        "showName": "测试数据"
                    },
                    "8a8a9ca4729755f0017297a7e79003e3": "xmxx2020-070100",
                    "8a8a9ca4729755f0017297a7e7930404": [
                        {
                            "checked": False,
                            "id": "8a8a9ca470f7120a0170f752dd9a04e4",
                            "showName": "银河小分队",
                            "type": "8"
                        }
                    ],
                    "isChildForm": "1",
                    "isMainToChild": ""
                },
                {
                    "id": "1290170272917364736",
                    "showName": "项目接口详情信息",
                    "8a8a9ca4729755f0017297a7e79003e7": {
                        "checked": False,
                        "id": "1290170272917364736",
                        "showName": "项目接口详情信息"
                    },
                    "8a8a9ca4729755f0017297a7e79003e3": "xmxx2020-080007",
                    "8a8a9ca4729755f0017297a7e7930404": [
                        {
                            "checked": False,
                            "id": "8a8a9ca470f7120a0170f752dd9a04e4",
                            "showName": "银河小分队",
                            "type": "8"
                        }
                    ],
                    "isChildForm": "1",
                    "isMainToChild": ""
                },
                {
                    "id": "1290177391171346432",
                    "showName": "周一新增测试数据",
                    "8a8a9ca4729755f0017297a7e79003e7": {
                        "checked": False,
                        "id": "1290177391171346432",
                        "showName": "周一新增测试数据"
                    },
                    "8a8a9ca4729755f0017297a7e79003e3": "xmxx2020-078461",
                    "8a8a9ca4729755f0017297a7e7930404": [
                        {
                            "checked": False,
                            "id": "8a8a9ca470f7120a0170f752dd9a04e4",
                            "showName": "银河小分队",
                            "type": "8"
                        }
                    ],
                    "isChildForm": "1",
                    "isMainToChild": ""
                },
                {
                    "id": "1290178113292083200",
                    "showName": "周一新增测试数据",
                    "8a8a9ca4729755f0017297a7e79003e7": {
                        "checked": False,
                        "id": "1290178113292083200",
                        "showName": "周一新增测试数据"
                    },
                    "8a8a9ca4729755f0017297a7e79003e3": "xmxx2020-079972",
                    "8a8a9ca4729755f0017297a7e7930404": [
                        {
                            "checked": False,
                            "id": "8a8a9ca470f7120a0170f752dd9a04e4",
                            "showName": "银河小分队",
                            "type": "8"
                        }
                    ],
                    "isChildForm": "1",
                    "isMainToChild": ""
                },
                {
                    "id": "1290193291366768640",
                    "showName": "周一新增测试数据",
                    "8a8a9ca4729755f0017297a7e79003e7": {
                        "checked": False,
                        "id": "1290193291366768640",
                        "showName": "周一新增测试数据"
                    },
                    "8a8a9ca4729755f0017297a7e79003e3": "xmxx2020-074561",
                    "8a8a9ca4729755f0017297a7e7930404": [
                        {
                            "checked": False,
                            "id": "8a8a9ca470f7120a0170f752dd9a04e4",
                            "showName": "银河小分队",
                            "type": "8"
                        }
                    ],
                    "isChildForm": "1",
                    "isMainToChild": ""
                },
                {
                    "id": "1290194344489394176",
                    "showName": "周一新增测试数据",
                    "8a8a9ca4729755f0017297a7e79003e7": {
                        "checked": False,
                        "id": "1290194344489394176",
                        "showName": "周一新增测试数据"
                    },
                    "8a8a9ca4729755f0017297a7e79003e3": "xmxx2020-071640",
                    "8a8a9ca4729755f0017297a7e7930404": [
                        {
                            "checked": False,
                            "id": "8a8a9ca470f7120a0170f752dd9a04e4",
                            "showName": "银河小分队",
                            "type": "8"
                        }
                    ],
                    "isChildForm": "1",
                    "isMainToChild": ""
                },
                {
                    "id": "1290194661696217088",
                    "showName": "周一新增测试数据",
                    "8a8a9ca4729755f0017297a7e79003e7": {
                        "checked": False,
                        "id": "1290194661696217088",
                        "showName": "周一新增测试数据"
                    },
                    "8a8a9ca4729755f0017297a7e79003e3": "xmxx2020-078535",
                    "8a8a9ca4729755f0017297a7e7930404": [
                        {
                            "checked": False,
                            "id": "8a8a9ca470f7120a0170f752dd9a04e4",
                            "showName": "银河小分队",
                            "type": "8"
                        }
                    ],
                    "isChildForm": "1",
                    "isMainToChild": ""
                },
                {
                    "id": "1290195334722625536",
                    "showName": "周一新增测试数据",
                    "8a8a9ca4729755f0017297a7e79003e7": {
                        "checked": False,
                        "id": "1290195334722625536",
                        "showName": "周一新增测试数据"
                    },
                    "8a8a9ca4729755f0017297a7e79003e3": "xmxx2020-071693",
                    "8a8a9ca4729755f0017297a7e7930404": [
                        {
                            "checked": False,
                            "id": "8a8a9ca470f7120a0170f752dd9a04e4",
                            "showName": "银河小分队",
                            "type": "8"
                        }
                    ],
                    "isChildForm": "1",
                    "isMainToChild": ""
                },
                {
                    "id": "1290204896968187904",
                    "showName": "测试数据aaaa",
                    "8a8a9ca4729755f0017297a7e79003e7": {
                        "checked": False,
                        "id": "1290204896968187904",
                        "showName": "测试数据aaaa"
                    },
                    "8a8a9ca4729755f0017297a7e79003e3": "xmxx2020-079012",
                    "8a8a9ca4729755f0017297a7e7930404": [
                        {
                            "checked": False,
                            "id": "8a8a9ca470f7120a0170f752dd9a04e4",
                            "showName": "银河小分队",
                            "type": "8"
                        }
                    ],
                    "isChildForm": "1",
                    "isMainToChild": ""
                },

            ],
            "maxResults": 50,
            "next": 2,
            "notCount": False,
            "orderBy": "",
            "pageNo": 1,
            "pageSize": 50,
            "prev": 0,
            "totalPage": 0
        },
        "isChildForm": "1",
        "isMainToChild": ""
    },
    "loginName": "8a8a9ca4736b23ce01736f6200f41771",
    "message": "操作成功！",
    "msgCode": 1,
    "token": "8a8a9ca4736b23ce01736f6200f41771,318ebaee3fa6f41fcaea331d40ed38a4"
}

if __name__ == "__main__":
    res = DeepDiff(a, b,ignore_order=True).to_dict()
    if res.get('dictionary_item_removed') or res.get('dictionary_item_added') or res.get(
            'type_changes'):
        print(res)

# data = {"data": {"customerList": [{"checked": False, "id": "8a8a9ca470af922d0170bd1605ff02be"}]}}
# print(data['data']['customerList'][0]['id'])
# hea={
#     "Accept": "*/*",
#     "Accept-Encoding": "gzip, deflate, br",
#     "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36"
# }
# url= 'https://gzzqa.cssiot.com.cn:8465/cssmfw/bizForm/doImportFormExcelInfo/web/8a8a9ca4736b23ce01736f6200f41771,70f83a1ab35f34320511fce21fed8651/8a8a9ca4736b23ce01736f6200f41771?formId=8a8a9ca4729755f0017297a7e6890253'
#
# with open('C:/Users/pcsales/Desktop/项目信息导入模版.xlsx', 'rb') as f:
#     response = requests.post(url=url,data=f,headers=hea)
# print(response.text)
# a={
#     "clientType": "web",
#     "code": "1",
#     "data": {
#         "formJson": {
#             "startItemName ": " ",
#             "majorStartItemId ": " ",
#             "groupId ": "ff80808171a60cf30171b530ae78045b ",
#             "icon ": "dataForm ",
#             "dataRight ": "0 ",
#             "schemeId ": "8a8a9ca4729755f0017297a7e63901f5 ",
#             "isSaveShare ": "1 ",
#             "formEnName ": "newForm ",
#             "majorEndItemId ": " ",
#             "isImportant ": "1 ",
#             "isAppDetailShot ": "1 ",
#             "endItemId ": " ",
#             "isCalendar ": "1 ",
#             "isPlatformDataVisible ": "1 ",
#             "formId ": "8a8a9ca4729755f0017297a7e6890253 ",
#             "max ": 21,
#             "titleItemName ": " ",
#             "isAppShow ": "0 ",
#             "layout ": "1 ",
#             "isBaseData ": "1 ",
#             "endItemName ": " ",
#             "mainTitle ": " ",
#             "iconColor ": "#3179ec ",
#             "describe ": " ",
#             "titleItemId ": " ",
#             "items": [
#                 {
#                     "defaultType ": "0 ",
#                     "defaultValue ": " ",
#                     "describe ": " ",
#                     "elementCnName ": "项目编号 ",
#                     "elementEnName ": "_0item5C2338456A ",
#                     "formId ": "8a8a9ca4729755f0017297a7e6890253 ",
#                     "format ": "0 ",
#                     "id ": "8a8a9ca4729755f0017297a7e68c0260 ",
#                     "isAppVisible ": "0 ",
#                     "isEdit ": "1 ",
#                     "isProtected ": "1 ",
#                     "isRequired ": "0 ",
#                     "isScan ": "1 ",
#                     "isTextReco ": "1 ",
#                     "isUnique ": "1 ",
#                     "isUpdateScan ": "0 ",
#                     "isVisible ": "0 ",
#                     "isVoiceReco ": "1 ",
#                     "itemId ": "_0item5C2338456A ",
#                     "itemSort ": "0 ",
#                     "layout ": "1 ",
#                     "length ": "1000 ",
#                     "type ": "0 ",
#                     "weight ": 0
#                 },
#                 {
#                     "bizExePoint ": "1 ",
#                     "conditionList ": [],
#                     "dataType ": "0 ",
#                     "defaultType ": "2 ",
#                     "defaultValue ": " ",
#                     "defaultValueName ": " ",
#                     "describe ": " ",
#                     "elementCnName ": "项目名称 ",
#                     "elementEnName ": "_20item312EEF416F ",
#                     "formId ": "8a8a9ca4729755f0017297a7e6890253 ",
#                     "id ": "8a8a9ca4729755f0017297a7e68d0264 ",
#                     "isAppVisible ": "0 ",
#                     "isEdit ": "0 ",
#                     "isHref ": "1 ",
#                     "isLinkFormSeg ": "1 ",
#                     "isMultiple ": "1 ",
#                     "isProtected ": "1 ",
#                     "isRequired ": "0 ",
#                     "isUnique ": "1 ",
#                     "isVisible ": "0 ",
#                     "itemId ": "_20item312EEF416F ",
#                     "itemSort ": "1 ",
#                     "layout ": "1 ",
#                     "linkFormElementId ": "8a8a9ca4729755f0017297a7e67a0212 ",
#                     "linkFormElementName ": "项目名称 ",
#                     "linkFormId ": "8a8a9ca4729755f0017297a7e65e01fc ",
#                     "linkFormName ": "项目信息 ",
#                     "linkSchemeId ": "ff80808171a60cf30171b527db72043f ",
#                     "linkSchemeName ": "场景测试方案 ",
#                     "relateShowList ": [
#                         {
#                             "elementId ": "8a8a9ca4729755f0017297a7e68d0264 ",
#                             "relateElementId ": "8a8a9ca4729755f0017297a7e68c0260 ",
#                             "relateElementItemId ": "_0item5C2338456A ",
#                             "relateFormElementId ": "8a8a9ca4729755f0017297a7e666020b ",
#                             "relateFormElementName ": "项目编号 "
#                         },
#                         {
#                             "elementId ": "8a8a9ca4729755f0017297a7e68d0264 ",
#                             "relateElementId ": "8a8a9ca4729755f0017297a7e691026e ",
#                             "relateElementItemId ": "_8itemF98E3B1BBE ",
#                             "relateFormElementId ": "8a8a9ca4729755f0017297a7e6800236 ",
#                             "relateFormElementName ": "项目成员 "
#                         }
#                     ],
#                     "type ": "20 ",
#                     "weight ": 1
#                 },
#                 {
#                     "defaultType ": "0 ",
#                     "defaultValue ": " ",
#                     "describe ": " ",
#                     "elementCnName ": "子项目名称 ",
#                     "elementEnName ": "_0item871FAC9A81 ",
#                     "formId ": "8a8a9ca4729755f0017297a7e6890253 ",
#                     "format ": "0 ",
#                     "id ": "8a8a9ca4729755f0017297a7e690026a ",
#                     "isAppVisible ": "0 ",
#                     "isEdit ": "0 ",
#                     "isProtected ": "1 ",
#                     "isRequired ": "0 ",
#                     "isScan ": "1 ",
#                     "isTextReco ": "1 ",
#                     "isUnique ": "1 ",
#                     "isUpdateScan ": "0 ",
#                     "isVisible ": "0 ",
#                     "isVoiceReco ": "1 ",
#                     "itemId ": "_0item871FAC9A81 ",
#                     "itemSort ": "2 ",
#                     "layout ": "1 ",
#                     "length ": "255 ",
#                     "type ": "0 ",
#                     "weight ": 2
#                 },
#                 {
#                     "dataValue ": [
#                         {
#                             "showName ": "银河小分队 ",
#                             "isSelfChildForm ": "1 ",
#                             "id ": "8a8a9ca470f7120a0170f752dd9a04e4 ",
#                             "isChildForm ": "0 ",
#                             "isMainToChild ": " "
#                         }
#                     ],
#                     "defaultObject ": [
#                         {
#                             "showName ": "银河小分队 ",
#                             "isSelfChildForm ": "1 ",
#                             "id ": "8a8a9ca470f7120a0170f752dd9a04e4 ",
#                             "isChildForm ": "0 ",
#                             "isMainToChild ": " "
#                         }
#                     ],
#                     "defaultType ": "4 ",
#                     "defaultValue ": " ",
#                     "defaultValueName ": " ",
#                     "describe ": " ",
#                     "elementCnName ": "项目成员 ",
#                     "elementEnName ": "_8itemF98E3B1BBE ",
#                     "formId ": "8a8a9ca4729755f0017297a7e6890253 ",
#                     "id ": "8a8a9ca4729755f0017297a7e691026e ",
#                     "isAppVisible ": "0 ",
#                     "isDataDictionary ": "1 ",
#                     "isDataOperate ": " ",
#                     "isDataSeparate ": " ",
#                     "isEdit ": "1 ",
#                     "isEmptyOption ": "0 ",
#                     "isProtected ": "1 ",
#                     "isRequired ": "1 ",
#                     "isUnique ": "1 ",
#                     "isVisible ": "0 ",
#                     "itemId ": "_8itemF98E3B1BBE ",
#                     "itemSort ": "3 ",
#                     "layout ": "1 ",
#                     "messageArr ": [],
#                     "module ": "1 ",
#                     "relateShowList ": [],
#                     "type ": "8 ",
#                     "weight ": 3
#                 },
#                 {
#                     "defaultType ": "1 ",
#                     "describe ": " ",
#                     "elementCnName ": "子项目金额 ",
#                     "elementEnName ": "_6itemC75067CFAC ",
#                     "endRange ": " ",
#                     "expression ": [
#                         {
#                             "elementCnName ": "SUM ",
#                             "expId ": "01004 ",
#                             "type ": "exp ",
#                             "weight ": 0
#                         },
#                         {
#                             "elementCnName ": "( ",
#                             "expId ": "00004 ",
#                             "type ": "quot ",
#                             "weight ": 0
#                         },
#                         {
#                             "elementCnName ": "工程量清单-合同合计 ",
#                             "itemId ": "_6subItemA6292E9CA7 ",
#                             "subItemId ": "_12item669BEE048B ",
#                             "type ": "6 ",
#                             "weight ": 0
#                         },
#                         {
#                             "elementCnName ": ") ",
#                             "expId ": "00005 ",
#                             "type ": "quot ",
#                             "weight ": 0
#                         }
#                     ],
#                     "formId ": "8a8a9ca4729755f0017297a7e6890253 ",
#                     "format ": "2 ",
#                     "id ": "8a8a9ca4729755f0017297a7e6950272 ",
#                     "isAppVisible ": "0 ",
#                     "isEdit ": "1 ",
#                     "isProtected ": "1 ",
#                     "isRequired ": "0 ",
#                     "isUpperCase ": "1 ",
#                     "isVisible ": "0 ",
#                     "itemId ": "_6itemC75067CFAC ",
#                     "itemSort ": "4 ",
#                     "layout ": "0 ",
#                     "length ": "18 ",
#                     "startRange ": " ",
#                     "symbol ": "0 ",
#                     "type ": "6 ",
#                     "weight ": 4
#                 },
#                 {
#                     "childFormId ": "8a8a9ca4729755f0017297a7e69a0281 ",
#                     "dataType ": "1 ",
#                     "describe ": " ",
#                     "elementCnName ": "工程量清单 ",
#                     "elementEnName ": "_12item669BEE048B ",
#                     "formId ": "8a8a9ca4729755f0017297a7e6890253 ",
#                     "id ": "8a8a9ca4729755f0017297a7e6950271 ",
#                     "isRequired ": "0 ",
#                     "isSubChecks ": "0 ",
#                     "isSubFormInner ": "1 ",
#                     "itemId ": "_12item669BEE048B ",
#                     "itemSort ": "5 ",
#                     "items ": [
#                         {
#                             "bizExePoint ": "1 ",
#                             "columnWidth ": " ",
#                             "conditionList ": [],
#                             "dataType ": "1 ",
#                             "defaultType ": "2 ",
#                             "defaultValue ": " ",
#                             "defaultValueName ": " ",
#                             "describe ": " ",
#                             "elementCnName ": "收入项目名称 ",
#                             "elementEnName ": "_20subItemB0F5F5F899 ",
#                             "formId ": "8a8a9ca4729755f0017297a7e69a0281 ",
#                             "id ": "8a8a9ca4729755f0017297a7e69a0282 ",
#                             "isAppVisible ": "0 ",
#                             "isEdit ": "0 ",
#                             "isHref ": "1 ",
#                             "isLinkFormSeg ": "1 ",
#                             "isMultiple ": "1 ",
#                             "isProtected ": "1 ",
#                             "isRecordUnique ": "1 ",
#                             "isRequired ": "0 ",
#                             "isSubChecks ": "0 ",
#                             "isUnique ": "1 ",
#                             "isVisible ": "0 ",
#                             "itemId ": "_20subItemB0F5F5F899 ",
#                             "itemSort ": "0 ",
#                             "layout ": "0 ",
#                             "linkFormElementId ": "8a8a9ca4729755f0017297a7e7ac0472 ",
#                             "linkFormElementName ": "收入项目名称 ",
#                             "linkFormId ": "8a8a9ca4729755f0017297a7e7aa0459 ",
#                             "linkFormName ": "收入项目名称 ",
#                             "linkSchemeId ": "2 ",
#                             "linkSchemeName ": "基础平台 ",
#                             "relateShowList ": [
#                                 {
#                                     "elementId ": "8a8a9ca4729755f0017297a7e69a0282 ",
#                                     "innChildItemId ": "_12item669BEE048B ",
#                                     "relateElementId ": "8a8a9ca4729755f0017297a7e69d028e ",
#                                     "relateElementItemId ": "_2subItem8B8F79B3C4 ",
#                                     "relateFormElementId ": "8a8a9ca4729755f0017297a7e7ac0476 ",
#                                     "relateFormElementName ": "直径 "
#                                 },
#                                 {
#                                     "elementId ": "8a8a9ca4729755f0017297a7e69a0282 ",
#                                     "innChildItemId ": "_12item669BEE048B ",
#                                     "relateElementId ": "8a8a9ca4729755f0017297a7e69b0286 ",
#                                     "relateElementItemId ": "_0subItemE2860D27BA ",
#                                     "relateFormElementId ": "8a8a9ca4729755f0017297a7e7ac0479 ",
#                                     "relateFormElementName ": "计量单位 "
#                                 },
#                                 {
#                                     "elementId ": "8a8a9ca4729755f0017297a7e69a0282 ",
#                                     "innChildItemId ": "_12item669BEE048B ",
#                                     "relateElementId ": "8a8a9ca4729755f0017297a7e69e028f ",
#                                     "relateElementItemId ": "_8subItem6523213A10 ",
#                                     "relateFormElementId ": "8a8a9ca4729755f0017297a7e7ab046b ",
#                                     "relateFormElementName ": "工程类型 "
#                                 }
#                             ],
#                             "type ": "20 ",
#                             "weight ": 0
#                         },
#                         {
#                             "columnWidth ": " ",
#                             "defaultType ": "0 ",
#                             "defaultValue ": " ",
#                             "describe ": " ",
#                             "elementCnName ": "桩直径 ",
#                             "elementEnName ": "_2subItem8B8F79B3C4 ",
#                             "endRange ": " ",
#                             "formId ": "8a8a9ca4729755f0017297a7e69a0281 ",
#                             "format ": "0 ",
#                             "id ": "8a8a9ca4729755f0017297a7e69d028e ",
#                             "isAppVisible ": "0 ",
#                             "isEdit ": "1 ",
#                             "isProtected ": "1 ",
#                             "isRequired ": "1 ",
#                             "isVisible ": "0 ",
#                             "itemId ": "_2subItem8B8F79B3C4 ",
#                             "itemSort ": "1 ",
#                             "layout ": "0 ",
#                             "length ": "18 ",
#                             "startRange ": " ",
#                             "type ": "2 ",
#                             "weight ": 1
#                         },
#                         {
#                             "columnWidth ": " ",
#                             "defaultType ": "0 ",
#                             "defaultValue ": " ",
#                             "describe ": " ",
#                             "elementCnName ": "计量单位 ",
#                             "elementEnName ": "_0subItemE2860D27BA ",
#                             "expression ": [],
#                             "formId ": "8a8a9ca4729755f0017297a7e69a0281 ",
#                             "format ": "0 ",
#                             "id ": "8a8a9ca4729755f0017297a7e69b0286 ",
#                             "isAppVisible ": "0 ",
#                             "isEdit ": "1 ",
#                             "isProtected ": "1 ",
#                             "isRecordUnique ": "1 ",
#                             "isRequired ": "1 ",
#                             "isScan ": "1 ",
#                             "isTextReco ": "1 ",
#                             "isUnique ": "1 ",
#                             "isUpdateScan ": "0 ",
#                             "isVisible ": "0 ",
#                             "isVoiceReco ": "1 ",
#                             "itemId ": "_0subItemE2860D27BA ",
#                             "itemSort ": "2 ",
#                             "layout ": "0 ",
#                             "length ": "255 ",
#                             "type ": "0 ",
#                             "userField ": " ",
#                             "weight ": 2
#                         },
#                         {
#                             "bizExePoint ": "1 ",
#                             "columnWidth ": " ",
#                             "dataType ": "1 ",
#                             "defaultType ": "3 ",
#                             "defaultValue ": " ",
#                             "defaultValueName ": " ",
#                             "describe ": " ",
#                             "elementCnName ": "工程类型 ",
#                             "elementEnName ": "_8subItem6523213A10 ",
#                             "formId ": "8a8a9ca4729755f0017297a7e69a0281 ",
#                             "id ": "8a8a9ca4729755f0017297a7e69e028f ",
#                             "isAppVisible ": "0 ",
#                             "isEdit ": "0 ",
#                             "isEmptyOption ": "1 ",
#                             "isHref ": "1 ",
#                             "isLinkFormSeg ": "1 ",
#                             "isProtected ": "1 ",
#                             "isRecordUnique ": "1 ",
#                             "isRequired ": "0 ",
#                             "isUnique ": "1 ",
#                             "isVisible ": "0 ",
#                             "itemId ": "_8subItem6523213A10 ",
#                             "itemSort ": "3 ",
#                             "layout ": "0 ",
#                             "linkFormElementId ": "8a8a9ca4729755f0017297a7e7b104a2 ",
#                             "linkFormElementName ": "工程类型名称 ",
#                             "linkFormId ": "8a8a9ca4729755f0017297a7e7b0048c ",
#                             "linkFormName ": "工程类型 ",
#                             "linkSchemeId ": "2 ",
#                             "linkSchemeName ": "基础平台 ",
#                             "type ": "8 ",
#                             "weight ": 3
#                         },
#                         {
#                             "columnWidth ": " ",
#                             "defaultType ": "0 ",
#                             "defaultValue ": " ",
#                             "describe ": " ",
#                             "elementCnName ": "工程量 ",
#                             "elementEnName ": "_2subItem2E327C6534 ",
#                             "endRange ": " ",
#                             "formId ": "8a8a9ca4729755f0017297a7e69a0281 ",
#                             "format ": "0 ",
#                             "id ": "8a8a9ca4729755f0017297a7e69b0287 ",
#                             "isAppVisible ": "0 ",
#                             "isEdit ": "0 ",
#                             "isProtected ": "1 ",
#                             "isRequired ": "1 ",
#                             "isVisible ": "0 ",
#                             "itemId ": "_2subItem2E327C6534 ",
#                             "itemSort ": "4 ",
#                             "layout ": "0 ",
#                             "length ": "18 ",
#                             "startRange ": " ",
#                             "type ": "2 ",
#                             "weight ": 4
#                         },
#                         {
#                             "columnWidth ": " ",
#                             "defaultType ": "0 ",
#                             "defaultValue ": " ",
#                             "describe ": " ",
#                             "elementCnName ": "合同单价 ",
#                             "elementEnName ": "_6subItem6C8952F6FF ",
#                             "endRange ": " ",
#                             "formId ": "8a8a9ca4729755f0017297a7e69a0281 ",
#                             "format ": "2 ",
#                             "id ": "8a8a9ca4729755f0017297a7e69b0288 ",
#                             "isAppVisible ": "0 ",
#                             "isEdit ": "0 ",
#                             "isProtected ": "1 ",
#                             "isRequired ": "1 ",
#                             "isUpperCase ": "1 ",
#                             "isVisible ": "0 ",
#                             "itemId ": "_6subItem6C8952F6FF ",
#                             "itemSort ": "5 ",
#                             "layout ": "0 ",
#                             "length ": "18 ",
#                             "startRange ": " ",
#                             "symbol ": "0 ",
#                             "type ": "6 ",
#                             "weight ": 5
#                         },
#                         {
#                             "columnWidth ": " ",
#                             "defaultType ": "1 ",
#                             "describe ": " ",
#                             "elementCnName ": "合同合计 ",
#                             "elementEnName ": "_6subItemA6292E9CA7 ",
#                             "endRange ": " ",
#                             "expression ": [
#                                 {
#                                     "elementCnName ": "工程量清单-工程量 ",
#                                     "itemId ": "_2subItem2E327C6534 ",
#                                     "subItemId ": "_12item669BEE048B ",
#                                     "type ": "2 ",
#                                     "weight ": 0
#                                 },
#                                 {
#                                     "elementCnName ": "* ",
#                                     "expId ": "00002 ",
#                                     "type ": "symbol ",
#                                     "weight ": 0
#                                 },
#                                 {
#                                     "elementCnName ": "工程量清单-合同单价 ",
#                                     "itemId ": "_6subItem6C8952F6FF ",
#                                     "subItemId ": "_12item669BEE048B ",
#                                     "type ": "6 ",
#                                     "weight ": 0
#                                 }
#                             ],
#                             "formId ": "8a8a9ca4729755f0017297a7e69a0281 ",
#                             "format ": "2 ",
#                             "id ": "8a8a9ca4729755f0017297a7e69b0289 ",
#                             "isAppVisible ": "0 ",
#                             "isEdit ": "0 ",
#                             "isProtected ": "1 ",
#                             "isRequired ": "1 ",
#                             "isUpperCase ": "1 ",
#                             "isVisible ": "0 ",
#                             "itemId ": "_6subItemA6292E9CA7 ",
#                             "itemSort ": "6 ",
#                             "layout ": "0 ",
#                             "length ": "18 ",
#                             "startRange ": " ",
#                             "symbol ": "0 ",
#                             "type ": "6 ",
#                             "weight ": 6
#                         },
#                         {
#                             "columnWidth ": " ",
#                             "defaultType ": "0 ",
#                             "defaultValue ": " ",
#                             "describe ": " ",
#                             "elementCnName ": "备注 ",
#                             "elementEnName ": "_0subItem2DA0CD7B11 ",
#                             "expression ": [],
#                             "formId ": "8a8a9ca4729755f0017297a7e69a0281 ",
#                             "format ": "0 ",
#                             "id ": "8a8a9ca4729755f0017297a7e69d028d ",
#                             "isAppVisible ": "0 ",
#                             "isEdit ": "0 ",
#                             "isProtected ": "1 ",
#                             "isRecordUnique ": "1 ",
#                             "isRequired ": "1 ",
#                             "isScan ": "1 ",
#                             "isTextReco ": "1 ",
#                             "isUnique ": "1 ",
#                             "isUpdateScan ": "0 ",
#                             "isVisible ": "0 ",
#                             "isVoiceReco ": "1 ",
#                             "itemId ": "_0subItem2DA0CD7B11 ",
#                             "itemSort ": "7 ",
#                             "layout ": "0 ",
#                             "length ": "255 ",
#                             "type ": "0 ",
#                             "userField ": " ",
#                             "weight ": 7
#                         }
#                     ],
#                     "linkFormElementId ": "8a8a9ca4729755f0017297a7e7ac0472 ",
#                     "linkFormElementName ": "收入项目名称 ",
#                     "linkFormId ": "8a8a9ca4729755f0017297a7e7aa0459 ",
#                     "linkFormName ": "收入项目名称 ",
#                     "relateShowList ": [
#                         {
#                             "elementId ": "8a8a9ca4729755f0017297a7e69a0282 ",
#                             "innChildItemId ": "_12item669BEE048B ",
#                             "relateElementId ": "8a8a9ca4729755f0017297a7e69d028e ",
#                             "relateElementItemId ": "_2subItem8B8F79B3C4 ",
#                             "relateFormElementId ": "8a8a9ca4729755f0017297a7e7ac0476 ",
#                             "relateFormElementName ": "直径 "
#                         },
#                         {
#                             "elementId ": "8a8a9ca4729755f0017297a7e69a0282 ",
#                             "innChildItemId ": "_12item669BEE048B ",
#                             "relateElementId ": "8a8a9ca4729755f0017297a7e69b0286 ",
#                             "relateElementItemId ": "_0subItemE2860D27BA ",
#                             "relateFormElementId ": "8a8a9ca4729755f0017297a7e7ac0479 ",
#                             "relateFormElementName ": "计量单位 "
#                         },
#                         {
#                             "elementId ": "8a8a9ca4729755f0017297a7e69a0282 ",
#                             "innChildItemId ": "_12item669BEE048B ",
#                             "relateElementId ": "8a8a9ca4729755f0017297a7e69e028f ",
#                             "relateElementItemId ": "_8subItem6523213A10 ",
#                             "relateFormElementId ": "8a8a9ca4729755f0017297a7e7ab046b ",
#                             "relateFormElementName ": "工程类型 "
#                         },
#                         {
#                             "elementId ": "8a8a9ca4729755f0017297a7e69a0282 ",
#                             "innChildItemId ": "_12item669BEE048B ",
#                             "relateElementId ": "8a8a9ca4729755f0017297a7e69a0282 ",
#                             "relateFormElementId ": "8a8a9ca4729755f0017297a7e7ac0472 "
#                         }
#                     ],
#                     "subCheckElementId ": "8a8a9ca4729755f0017297a7e69a0282 ",
#                     "type ": "12 ",
#                     "weight ": 5
#                 },
#                 {
#                     "defaultType ": "0 ",
#                     "describe ": " ",
#                     "elementCnName ": "图片19 ",
#                     "elementEnName ": "_25item8B09BC74A1 ",
#                     "fileNum ": "1 ",
#                     "fileType ": "0 ",
#                     "formId ": "8a8a9ca4729755f0017297a7e6890253 ",
#                     "id ": "8a8a9ca472ca937a0172cb88a9a813e5 ",
#                     "isAppVisible ": "0 ",
#                     "isEdit ": "0 ",
#                     "isRequired ": "1 ",
#                     "isVisible ": "0 ",
#                     "itemId ": "_25item8B09BC74A1 ",
#                     "itemSort ": "6 ",
#                     "layout ": "0 ",
#                     "shootLimit ": "1 ",
#                     "type ": "25 ",
#                     "weight ": 6
#                 },
#                 {
#                     "defaultType ": "0 ",
#                     "describe ": " ",
#                     "elementCnName ": "附件20 ",
#                     "elementEnName ": "_10item022413F2B4 ",
#                     "fileNum ": "1 ",
#                     "fileType ": " ",
#                     "formId ": "8a8a9ca4729755f0017297a7e6890253 ",
#                     "id ": "8a8a9ca472ca937a0172cb88a9a813e6 ",
#                     "isAppVisible ": "0 ",
#                     "isEdit ": "0 ",
#                     "isRequired ": "1 ",
#                     "isVisible ": "0 ",
#                     "itemId ": "_10item022413F2B4 ",
#                     "itemSort ": "7 ",
#                     "layout ": "0 ",
#                     "showItemId ": " ",
#                     "type ": "10 ",
#                     "weight ": 7
#                 }
#             ],
#             "showItemId ": " ",
#             "formCnName ": "子项目信息 ",
#             "startItemId ": " "
#         }
#     },
#     "loginName": "8a8a9ca4736b23ce01736f6200f41771",
#     "message": "操作成功！",
#     "msgCode": 1,
#     "token": "8a8a9ca4736b23ce01736f6200f41771,d09cc4a275afa6e8b7e963b9cc429c70"
# }
#
