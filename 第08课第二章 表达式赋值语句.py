a = 1024*32
print(a)
a = '对酒当歌，人生几何？' + '譬如朝露，去日苦多'
print(a)

# 同步赋值语句
a,b,c = 3,4,8
print(a,b,c)

a,b = 3,4
a,b = b,a
print(a,b)

#type函数
a = 4 
b = type(a)
print(b) # int证书，str字符串

a = 'w网名' 
b = type(a)
print(b) # int证书，str字符串

a = input('请输入任意字符')
b = type(a)
print(b) # int证书，str字符串


