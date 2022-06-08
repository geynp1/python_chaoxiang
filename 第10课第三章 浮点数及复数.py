a = 1010.0
print(type(a))

a = 2
b = 3
c = pow(a,b)
print(c)

a = 0.1+0.2 # 精度造成浮点数不正确
print(a)

# 解决用round函数
a = round(1.234456)
print(a)

a = 11.3 + 4j
print(a)
print(type(a))
print(a.real) # 实数部分
print(a.imag) # 虚数部分