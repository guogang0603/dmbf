from django.shortcuts import render,HttpResponse
from invitation import models
import json
from django.http import JsonResponse
from django.shortcuts import render
# Create your views here.

def getallmessages(request):
    ret={}
    dict1 = {}
    list1=[]
    obj = models.Temps.objects.all()
    obj2 = models.Temps.objects.filter().all()[0:2] #切片，查询前两条
    for i in obj:
        dict1['title'] = i.title
        dict1['price'] = str(i.price)
        list1.append(dict1)
    ret['list1'] = list1

    ret2 = {}
    dict2 = {}
    list2 = []
    for j in obj2:
        # list2.append(j.title)
        list2.append(str(j.price))
    ret2['list2'] = list2
    return HttpResponse(json.dumps(ret2))
    # return JsonResponse({"msg": "ok!"})
#TODO:添加信息
def add_mess(request):
    #get/post获取信息，进行添加
    subscribe = 1
    openid = 'dsgkjhjkfdjjghj555555'
    nickname = '郭杠'
    headimg = 'D://gzx'
    sex = '1'
    province = '河北'
    city = ''
    country = 'China'
    phone = '17501622407'
    use = 3
    models.User_profile.objects.create(subscribe=subscribe, openid=openid, nickname=nickname,
                                       headimg=headimg, sex=sex, province=province, city=city, country=country,
                                       phone=phone, use=use)
    man_name = "孙昌阳"
    wman_name = "航航"
    marry_tm = "werreere"
    hotel_tm = "werreere"
    hotel_name = "werreere"
    phone = "werreere"
    link = "werreere"
    use_content_id = '8'
    #酒店信息添加
    models.Hotelmessages.objects.create(man_name=man_name, wman_name=wman_name, marry_tm=marry_tm,
        hotel_name=hotel_tm, hotel_map=hotel_name, phone=phone, link=link, use_content_id=use_content_id)
    return HttpResponse('恭喜添加成功！！！！')





