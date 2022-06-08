print('世界和平')

# 输出变量
a = 123
b = 345
c = a+b
print(c) # 468
print(a,b,c)
print('a的值为{},b的值为{},和是{}'.format(a,b,c)) # a的值为123,b的值为345,和是468

# 去掉最后的换行符
print(a,end='')
print(a,end='\n')
print(a)

# input()函数输入信息
a = input('请输入你的姓名:')
print(a)

# input输入的都是文本
a = input('请输入数字:')
b = input('请输入数字:')
print('{} + {}的值是:{}'.format(a,b,a+b)) # 12