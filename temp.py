"""
__mtime__ = '2017/6/26'
"""

class Role(object):
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

d1 = Role('cui','ak47')
d2 = Role('wang','B51')
d1.shot()
print(d1._Role__high)

print(d1.high())