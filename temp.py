"""
__mtime__ = '2017/6/26'
"""

class Role(object):
    sex = 'male'

    def __init__(self,name,weapon,life_value = 100,money = 15000):
        self.name = name
        self.weapon = weapon
        self.life_value = life_value
        self.Money = money
        self.__high = 175  #定义一个私有属性

    def shot(self):
        print('%s is shooting'%self.name)
        print(self.__high)      #内部可以调用
    def got_shot(self):
        print("ah...,I got shot...")
    def buy_gun(self,gun_name):
        print('%s bought %s'%(self.name,gun_name))
        self.weapon = gun_name  #替换原有的武器
    def high(self):     #提供了一个外部访问私有属性的只读接口
        return self.__high
    def __del__(self):
        print('deldeldel')
d1 = Role('cui','ak47')
# d2 = Role('wang','B51')
# d1.sex = 'female'   #修改d1的sex属性
# print(d1.sex,d2.sex,Role.sex)
# print("修改公有属性")
# Role.sex = 'god'    #修改全局的公有属性
# print(d1.sex,d2.sex,Role.sex)

