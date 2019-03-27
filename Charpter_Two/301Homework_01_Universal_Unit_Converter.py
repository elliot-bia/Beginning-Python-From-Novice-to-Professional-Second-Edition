##!/usr/bin/env Python
# -*- coding:utf-8 -*-
# 万能单位转换器
# 对外能单位转换器的完善
# author: Elliot

print('欢迎使用万能单位转换器'.center(30,'*'))
menu = {
    'T':'温度转换',
    'L':'长度转换',
    'C':'货币转换'
}
for k,v in menu.items():
    print(k,v)
choose = input('请输入转换类型：')

if choose == 'T':
    temp = input('请输入温度（示例：1C或1F）：')
    if temp.find('C')!=-1:
        temp = float(temp.strip('C').strip('F'))
        #摄氏温度转华氏温度 Tf=（9/5）Tc+32
        Tf = (9/5) * temp +32
        print(Tf,end="华氏度")

    elif temp.find('F')!=-1:
        temp = float(temp.strip('C').strip('F'))
        #华氏温度转摄氏温度 Tc=(Tf-32)（5/9）
        Tc = (temp - 32) * (5/9)
        print(Tc,end="摄氏度")

    else: print('输入出错了！')

elif choose == 'L':
    temp = input('请输入长度(实例：100km或100mi)')
    if temp.find('km')!=-1:
        temp = float(temp.strip('km').strip('mi'))
        #1公里等于0.62137英里
        mi = temp * 0.62137
        print(mi,end="英里")

    elif temp.find('mi')!=-1:
        temp = float(temp.strip('km').strip('mi'))
        #1英里等于1.61公里
        km = temp * 1.61
        print(km,end="公里")
    else: print('输入出错了！')

elif choose == 'C':
    temp = input('请输入货币(实例：100USD或100CNY)')
    if temp.find('USD')!=-1:
        temp = float(temp.strip('USD').strip('CNY'))
        #1美元等于6.7272人民币
        CNY = temp * 6.7262
        print(CNY,end="人民币")

    elif temp.find('CNY')!=-1:
        temp = float(temp.strip('USD').strip('CNY'))
        #1人民币等于0.15美元
        USD = temp * 0.15
        print(USD,end="美元")
    else: print('输入出错了！')
else: print('输入出错了！')