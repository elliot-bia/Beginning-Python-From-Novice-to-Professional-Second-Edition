#!/usr/bin/env Python
# -*- coding:utf-8 -*-
# Homework_03_51memo.py
# A memo 51备忘录
# author: Elliot


__author__ = 'Elliot'

desc = '51备忘录'.center(30,'-')
print(desc)
welcome = 'welcome'
print(f'{welcome}',__author__)
print('请输入备忘信息')

all_memo = []

# todo:这里要继续完成某个代码，这里对颜色进行定义


    #颜色转码格式为

    #   \033[显示方式;字体色;背景色m 这里是输出字符 [\ 033 [0m]

    # 具体参照：https://blog.csdn.net/qq_34857250/article/details/79673698

    # 已知字体色范围在 30-37
text_color = 30



# s = 'hi, Siri, 明天早上8点提醒我带手机'
# s.find('点')
# s[s.find('点')-1:s.find('点')]
# s[s.find('点')+1:]'


is_add = True
while(is_add):
    all_thing = input('输入一句话信息：')
    in_date = all_thing[all_thing.find('天')-1:all_thing.find('点')+1]
    in_thing = all_thing[all_thing.find('点')+1:]
    print('代办列表'.center(30,'-'))
    one = '{date},处理{thing}'.format(date=in_date,thing=in_thing)
    all_memo.append(one)
    num = 0

    #对颜色范围进行判断
    if text_color > 37:
        text_color = 30



    for m in all_memo:
        num += 1
        text_color += 1
        print(f'\033[1;{text_color}m%s:%s\033[0m!' %(num,m))

    print(f'共{len(all_memo)}条代办事项',end='')
    print('(y:继续添加，n:退出）')
    is_add = input().strip() == 'y'

