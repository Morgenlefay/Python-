## 函数

```python
def <函数名> ()：
	<函数体>
	return <函数值>

# 计算 x!
def f(x):
    s = 1
    for i in range(1,x+1):
        s= s * i
    return s
y=f(4)
print(y)

# 可选参数
def <函数名> (<非可选参数>, <可选参数>)：
	<函数体>
	return <函数值>
# 计算 x!//m，m为可选参数
def f(x,m=1):
    s = 1
    for i in range(1,x+1):
        s= s * i
    return s//m
y=f(4,5)
print(y)

# 可变参数
def <函数名> (<参数>, *b)：
	<函数体>
	return <函数值>
# Example
def f(x,*b):
    s = 1
    for i in range(1,x+1):
        s= s * i
    for item in b:
        s= s * item
    return s
y=f(4,5)
print(y)
y=f(4,5,2)
print(y)
y=f(4,5,2,1)
print(y)

# 参数的传递
def f(x,m=1):
    s = 1
    for i in range(1,x+1):
        s= s * i
    return s//m
y=f(4,5) # 位置传递
print(y)
y=f(m=5,x=4) # 名称传递
print(y)

# 函数的返回值
def f(x,m=1):
    s = 1
    for i in range(1,x+1):
        s= s * i
    return s//m, x, m
y=f(4,5) 
print(y)

# 局部变量和全局变量
x,y=10,1000 # x,y全局变量
def f(x): # x,y局部变量
    y = 1 
    for i in range(1,x+1):
        y = y * i
    return y
print(f(x),y)

# x!*y
x,y=10,1000 # x,y全局变量
def f(x): # 
    global y # global声明使用全局变量
    for i in range(1,x+1):
        y = y * i
    return y 
print(f(x),y)

# 局部变量为组合数据类型且未创建，等同于全局变量
ls = ["F","f"]
def func(a):
    ls.append(a) # 此处ls是列表类型，未真实创建则等同于全局变量
    return
func("C")
print(ls)

ls = ["F","f"]
def func(a):
    ls = [] # 此处ls是列表类型，真实创建，ls是局部变量
    ls.append(a)
    return
func("C")
print(ls)

# lambda函数
<函数名> = lambda <参数>:<表达式>
f = lambda x,y : x+y

# example
f = lambda x,y : x+y
z = f(10,15)
print(z)

f =  lambda : "lambda函数"
print(f())
```

## 七段数码管

```python
import turtle
import time

def drawGap():
    turtle.penup()
    turtle.fd(5)

def drawLine(draw): # 绘制单段数码管
    drawGap()
    turtle.pendown() if draw else turtle.penup()
    turtle.fd(40)
    drawGap()
    turtle.right(90)

def drawDigit(digit): # 根据数字绘制七段数码管
    drawLine(True) if digit in [2,3,4,5,6,8,9] else drawLine(False)
    drawLine(True) if digit in [0,1,3,4,5,6,7,8,9] else drawLine(False)
    drawLine(True) if digit in [0,2,3,5,6,8,9] else drawLine(False)
    drawLine(True) if digit in [0,2,6,8] else drawLine(False)
    turtle.left(90)
    drawLine(True) if digit in [0,4,5,6,8,9] else drawLine(False)
    drawLine(True) if digit in [0,2,3,5,6,7,8,9] else drawLine(False)
    drawLine(True) if digit in [0,1,2,3,4,7,8,9] else drawLine(False)
    turtle.left(180)
    turtle.penup()
    turtle.fd(20)

def drawDate(date): # date为日期，格式为‘%Y-%m=%d+’
    turtle.pencolor('red')
    for i in date:
        if i == '-':
            turtle.write('年',font=('Arial',18,'normal'))
            turtle.pencolor('green')
            turtle.fd(40)
        elif i == '=':
            turtle.write('月',font=('Arial',18,'normal'))
            turtle.pencolor('blue')
            turtle.fd(40)
        elif i == '+':
            turtle.write('日',font=('Arial',18,'normal'))
        else:
            drawDigit(eval(i))

def main():
    turtle.setup(800,350,200,200)
    turtle.penup()
    turtle.fd(-300)
    turtle.pensize(5)
    drawDate(time.strftime('%Y-%m=%d+',time.gmtime()))
    turtle.hideturtle
    turtle.done()
main()
```

