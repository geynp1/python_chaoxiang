# 查询python内置函数
print(dir(__builtins__))

# 查询具体函数的说明
print(help(abs))
print(help(pow))
# 输出所有的关键词
print(help('keywords'))

print(help('if'))


a = 3+4j
print(a.real)
# 通过对变量a查询方法
print(dir(a))
print(help(a.imag))