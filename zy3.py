# -*- coding: utf-8
import random

dict = {}  # 存储玩家名和猜对次数
name = []  # 存储玩家名
cai = 4  # 设默认猜的次数
a = 0
lun = 1


def num(names):
    for x in names.split(','):  # 将玩家以逗号隔开
        dict[x] = 0  # 设定玩家初始赢得数据为0


pk = int(raw_input('主持人确定游戏次数【默认为4次】：'))
print '主持人确定猜数范围，【默认范围1-30】'
min = int(raw_input('主持人输入猜数字的最小值:'))
max = int(raw_input('主持人输入猜数字的最大值:'))
cai = int(raw_input('主持人确定猜的次数【默认为4次】：'))
name1 = raw_input('请参赛者依次输入名字【并用逗号隔开】:')
num(name1)
print '游戏开始，请做好准备'

while pk > 0:
    ran = random.randint(min, max)
    print ran
    print '第', lun, '轮==='
    for n in range(cai):
        print '第', lun, '轮,第', n + 1, '次'
        for nu in dict:
            print nu,'玩家：'
            n1 = int(raw_input("请输入你的数字："))
            if n1 < ran:
                print("您输入的数太小了：")
            elif n1 > ran:
                print("您输入的数太大了：")
            else:
                print("恭喜您答对了：")
                a = 1
                dict[nu] += 1
                ran = random.randint(min, max)
                break
        if a == 0:
            print '很遗憾您输了'
            print  '游戏随机数是：', ran
            ran = random.randint(min, max)
    pk -= 1
    if pk > 0:
        lun+= 1

print('''
您本次游戏的排名值是：
''')

for key, valer in dict.items():
    print "姓名：%r , 成绩：%d." % (key, valer)