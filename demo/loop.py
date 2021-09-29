# 循环

# while while-else
count = 1;

while count <= 10 :
    count +=1
    print(count)
else:
    print('EOF')
    

# for for-else

list = [1, 2, 3, 4];
for item in list:
    print(item)
    
## for - range
for x in range(0, 10, 2):
    print(x, end=" | ") # 0 | 2 | 4 | 6 | 8 | 
print()
for x in range(10, 0, -2):
    print(x, end=" | ") # 10 | 8 | 6 | 4 | 2 | 
print()