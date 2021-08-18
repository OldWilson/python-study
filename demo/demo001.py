# encoding:utf-8
# -*-coding:utf-8-*-
# 元组不可变
# python 没有自增和自减 ++ --

# 运算符
## 平方
print(2 ** 2);
print(2 ** 3);
print("-----------------------");
# // 整数除法
print(2 // 3); # 0
print(2 // 1); # 2
print(5 // 2); # 2
print("-----------------------");
# % 求余
print(2 % 3);
print(5 % 2);
print("-----------------------");
# 比较运算
b = 1;
b += b >= 1;
print(b); # 2  b += b >= 1 => b += true => 2
print("-----------------------");
# 判断变量类型
a = 'hello';
print(type(a) == str);
print(isinstance(a, str));
print(isinstance(a, (int, float, str)));
print("-----------------------");
