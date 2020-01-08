# print函数
# 1.用法
print('hello world')
name='小白'
print(name)

# 2.用法：print(name,age,gender)
age=18
gender='male'
print(name,age,gender)

# 2.用法：print(value,value,value,...,sep=' ',end='\n')
print(name,age,gender,sep=' ') # sep='#',sep='$',sep='*'

# 转义字符：\n 换行
print('hello\nkitty')

print('AAA',end='')
print('BBB',end='')

print('AAA',end='\n')
print('BBB',end='\n')

# 练习：亲爱的xxx:
#           请点击链接激活用户：激活用户
print('亲爱的xxx:\n','请点击链接激活用户：激活用户',sep='    ',end='\n')

# 转义字符：\t 制表符Tab
print('亲爱的xxx:\n','请点击链接激活用户：激活用户',sep='\t',end='\n')
print('乔治说："想吃冰淇淋！！"')
