#!/usr/bin/env Python
# -*- coding:utf-8 -*-
# Guess Twenty-One Ponit
# author: Elliot


# 1.导入标准库
import random

# 2.第三方的库
# 3.自定义的库
# 因为python是从上到下进行执行的，后面的库可以替换掉前面的库

""" 
2.4.5 案例：21点

- 两个玩家，游戏开始先输入名字
- 用字典保存每个玩家信息：姓名，获胜次数
- 电脑随机产生2数，每个玩家轮流猜一个数，与电脑随机两个数求和，最接近21的获胜
- 每轮结束显示玩家信息
- 按q退出游戏
"""

target = 21

# 人类
user1 = input('第一个玩家的名字:')
user2 = input('第二个玩家的名字:')
print(f'玩家：{user1},{user2}')

users = {
    user1:{'win':0},
    user2:{'win':0}
}

print(users)

# PC 随机生成2个数
num1 = random.randint(1,10)
num2 = random.randint(1,10)

#此处不应该答应出来
# print(f'电脑随机选数:{num1},{num2}')

user1_guess = input(f'{user1} guess:')
user2_guess = input(f'{user2} guess:')
user1_sum = int(num1) + int(num2) + int(user1_guess)
user2_sum = int(num1) + int(num2) + int(user2_guess)
print(user1_sum,user2_sum)

if abs(user1_sum-21) > abs(user2_sum):
    print(f'{user1_sum}',f'{user2_sum}')
    print(f'{user2} win!')
else:
    print(f'{user1} win!')

print(f'电脑随机选数:{num1},{num2}')
