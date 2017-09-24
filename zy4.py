# -*- coding: utf-8 -*-
class Person(object):  #定义类  class 类名（所调用，继承的类）
    def __init__(self, name, ages):  #类的属性
        self.name = name
        self.ages = ages

    def print_way(self):  #类的方法
        print '%s，正在走路 ' % (self.name)



class Student(Person):
    def __init__(self,name,ages,xuehao):
        Person.__init__(self, name, ages)
        self.xuehao = xuehao

    def print_xh(self):
        print '%s, %s,正在上课' %(self.name,self.xuehao)



class Teacher(Person):
    def __init__(self,name, ages, jihe):
        Person.__init__(self, name, ages)
        self.jihe = jihe

    def print_shangke(self):
        print '%s 正在授课' % (self.name)
        for n in self.jihe:
            n.print_xh()

    def Teach(self):
        print '--------熬了50分钟--------'

    def print_xiake(self):
        print self.name, '说下课了...'
        for i in self.jihe:
            i.print_way()

if __name__ == "__main__":
    bart1 = Student('wu', 12, '7150211')
    bart2 = Student('zhi', 12, '07150212')
    bart3 = Student('sheng', 12, '07150213')
    studentlist=[bart1,bart2,bart3]
    bart5 = Teacher('teacher', 20, studentlist)

bart5.print_shangke()
bart5.Teach()
bart5.print_xiake()


