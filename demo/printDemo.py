# 条件控制
# if else

flg = False
if flg :
    print('flg is true')
else :
    print('flg is false')

# 控制台输入
print('please input id')
# user_id = input()
# print('id is ', user_id)

# print
print("hello world")
list = [1, 2, 3, "aaa"];
for item in list:
    print(item);

for item in list:
    print(item, end="") # 123aaa

print()
for item in list:
    print(item, end=", ") # 1, 2, 3, aaa
print()  # 若不写，最后一个循环的输出末尾会有%输出

#### print 字符串格式化
# %s
value = "world"
name = "python"
print("hello %s" %value) # hello world
print("hello %s, this is %s" %(value, name)) # hello world, this is python

# format
print("hello {}".format(value)) # hello world
print("hello {}, this is {}".format(value, name)) # hello world, this is python
## 填充对齐 索引：[填充字符][对齐方式][宽度]
### *<20 左对齐, 宽度20，不够*填充
print('{0:*<20}'.format("hello python")) # hello python********
### *>20 右对齐, 宽度20，不够*填充
print('{0:*>20}'.format("hello python")) # ********hello python
### *^20 居中对齐, 宽度20，不够*填充
print('{0:*^20}'.format("hello python")) # ****hello python****

## 位数与进制转换
# 保留2位小数
print("{:.2f}".format(3.136415)) # 3.14 会进行四舍五入
# 转换成二进制
print('{0:b}'.format(16)) # 10000
# 转换成八进制
print('{0:o}'.format(16)) # 20
# 转换成十六进制
print('{0:x}'.format(16)) # 10

## v3.6引入了f-strings
print(f'hello {value}, {name}') # hello world, python


