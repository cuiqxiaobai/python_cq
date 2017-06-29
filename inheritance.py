"""
__mtime__ = '2017/6/29'
"""
class SchoolMember(object):
    members = 0
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.enroll()

    def tell(self):
        pass

    def enroll(self):
        """注册"""
        SchoolMember.members += 1
        print("New member [%s] is enrolled, now there are [%s] members ."%(self.name,SchoolMember.members))

    def __del(self):
        """析构方法"""


class Teacher(SchoolMember):    #（）里面就是要继承的基类
    def __init__(self,name,age,cource,salary):
        # SchoolMember.__init__(self,name,age)  #继承基类的属性
        super(Teacher,self).__init__(name,age)
        self.cource = cource
        self.salary = salary
    def teaching(self):
        print("%s is teaching .."%self.name)


class Student(SchoolMember):
    def __init__(self,name,age,grade,sid):
        SchoolMember.__init__(self,name,age)
        self.grade = grade
        self.sif = sid

    def tell(self):
        '''自我介绍方法'''
        msg = '''Hi, my name is [%s], I'm studying [%s] in [%s]!''' % (self.name, self.grade, 'Oldboy')
        print(msg)

t1 = Teacher('Alex',22,'python',100000)
s1 = Student('cq',26,'python_auto',6700)
s2 = Student('laowang',30,'linux',600)

# t1.teaching()
s2.tell()