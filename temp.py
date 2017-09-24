# -*- coding: utf-8
import random

dict = {}
name = []
a = 0


# def mun(min=1,max=30):
#	random = int(random.randint(min,max))
#	return random

def num(names):
    for x in names.split(','):
        dict[x] = 0


print '主持人确定猜数范围，【默认范围1-30】'
min = int(raw_input('主持人输入猜数字的最小值:'))
max = int(raw_input('主持人输入猜数字的最大值:'))

pk = 1
while pk > 0:
    ran = random.randint(min, max)
    name1 = raw_input('请参赛者依次输入名字【并用逗号隔开】:')
    num(name1)
    pk = int(raw_input('主持人确定游戏次数【默认为4次】：'))
    for n in range(pk):
        for nu in name1:
            print nu
            n1 = int(raw_input("请输入你的数字："))
        if n1 < ran:
            print("您输入的数太小了：")
        elif n1 > ran:
            print("您输入的数太大了：")
        else:
            print("恭喜您答对了：")
    a = 1
    dict[nu] += 1
    if a == 0:
        print '很遗憾您输了'
        print  '游戏随机数是：', ran
    pk -= 1

print('''
您本次游戏的排名值是：
''')

for key, valer in dict.items():
    print "姓名：%r , 成绩：%d." % (key, valer)