# python: 命名的时候，名字是大写的
NAME='Jack'
print(NAME)

print('hello') # 输出的是字符串

value='hello'
print(value)

value='python'
print(value)

#字符串：字符串 表示：'', " ", ''' '''
value='python'
print(value)
value="python"
print(value)
value='''python'''
print(value)

message='''
[淘宝]你正在使用验证码登录，
验证码是：8906，
涉及个人账户安全，请保密。'''
print(message)
## 作用：1.保留格式的字符串使用；2.作为多行注释使用


person='大圣哥'
address='武汉大学'
phone='1111'

print('订单的收件人是：'+person+ '收货地址是：'+address+ '联系方式：'+phone)
print('订单的收件人是：%s,收货地址是：%s,联系方式：%s' % (person,address,phone))

# 占位符%s,%d,%f用法(%s=str(), %d=int(), %f= 小数点后的位数，而且是四舍五入)
name='赵飞'
age=18
print('姓名：%s,年龄：%s' % (name,age))
print('姓名：'+name+'，'+'年龄：'+str(age))
print('姓名：%s,年龄： %d' % (name,age))
salary=8999.32
print('我的薪水是：%.2f' % salary)


# 联系
movie='大侦探皮卡丘'
count=35
ticket=45.9
total=count*ticket

message='''
电影：%s
人数: %d
单价: %.1f
总票价: %.1f
''' % (movie, count, ticket, total)

print(message)

print('电影：%s' % movie)
print('人数：%d' % count)
print('单价：%.1f' % ticket)
print('总票价: %.1f' % total)

# format用法：format是一个字符串中的函数。''.format()。此处的‘.’为调用
name='Geroge'
age=2
s='已经上'
message='{}说："我今年{}岁了，{}幼儿园！"'.format(name,age,s)
print(message)









