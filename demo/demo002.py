# -*- coding: UTF-8 -*-
class demo():
    sum = 0
    
    def __init__(self, name1, age):
        self.name = name1
        self.age = age
        # print(self.name)
        # print(name1)
        
        self.sum += 1  #实例变量
        
        self.__class__.sum += 1; # 类变量
        
        self.__score = 0
    
    # 类方法
    @classmethod
    def demo001(cls):
        cls.sum +=1
        
    # 静态方法
    @staticmethod
    def demo002(x, y):
        print(x + y)
    
demo1 = demo('test', 18)
print(demo1.sum) # 1
print(demo.sum)  # 1

demo1.demo001()
demo.demo001()
print(demo1.sum) # 1
print(demo.sum)  # 3

print('=====================================')
demo2 = demo('demo2', 2)
demo3 = demo('demo3', 3)

# {'age': 2, 'name': 'demo2', '_demo__score': 0, 'sum': 4}
print(demo2.__dict__)
# {'age': 3, 'name': 'demo3', '_demo__score': 0, 'sum': 5}
print(demo3.__dict__)

demo2.__score = 1
print(demo2.__score)       # 1
print(demo2._demo__score)  # 0
print(demo3._demo__score)  # 0