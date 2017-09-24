# -*- coding: utf-8 -*-
#from sys import argv
import random
dict={} #存储输入名字
a = 0
go = 1
while go  == 1:
    name = raw_input("请输入您的姓名：")
    if not (name in dict):
        dict[name] = 0
    num = random. randint(0,100)
    print num
    for n in range(4):
        n1 = int(raw_input("请输入您的随机数："))
        if n1 < num:
            print("您输入的数太小了：")
        elif n1 > num:
            print("您输入的数太大了：")
        else:
            print("恭喜您答对了：")
            a = 1
            if name in dict:
                dict[name]+=1
            break
    if a == 0:
         print("很遗憾您输了")
    print int(raw_input("继续玩请输入 1  不玩请输入 2"))
    go = int(raw_input("请输入您的选项："))

print('''
您本次游戏的排名值是：
''')

#key,zhi = argv
for key,valer in dict.items():
 print "姓名：%r , 成绩：%d." % (key,valer)