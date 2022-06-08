# eval可以去引号，让数值直接相加


a = eval('1.2+3.4') 
print(a)

a = eval(input('请输入数字')) # 输入非数值报错
print(a)
print(type(a))
b = a + 321
print(b)