## 函数递归

```python
# n!
def f(n):
    if n == 0:
        return 1
    else:
        return n * f(n-1)
y = f(5)
print(y)

# 字符串反转
def rvs(s):
    if s == '':
        return s
    else:
        return rvs(s[1:]) + s[0]
a = 'abcde'
y = rvs(a)
print(y)

z = a[::-1]
print(z)

# 斐波那契数列
def F(n):
    if n == 1 or n == 2:
        return 1
    else:
        return F(n-1) + F(n-2)
y = F(6)
print(y)

# 汉诺塔
count = 0
def hanoi(n,src,dst,mid):
    global count
    if n == 1:
        print("{}:{}->{}".format(1,src,dst))
        count = count + 1
    else:
        hanoi(n-1,src,mid,dst)
        print("{}:{}->{}".format(n,src,dst))
        count = count + 1
        hanoi(n-1,mid,dst,src)

hanoi(3,"A","C","B")
print(count)
```

## 科赫雪花

```python
# 科赫曲线
import turtle
def koch(size,n):
    if n == 0:
        turtle.fd(size)
    else:
        for angle in [0,60,-120,60]:
            turtle.left(angle)
            koch(size/3,n-1)

def main():
    turtle.setup(800,800)
    turtle.penup()
    turtle.goto(-300,-50)
    turtle.pendown()
    koch(600,3) # 3阶科赫曲线
    turtle.hideturtle
    turtle.done()
main()

# 科赫雪花
import turtle
def koch(size,n):
    if n == 0:
        turtle.fd(size)
    else:
        for angle in [0,60,-120,60]:
            turtle.left(angle)
            koch(size/3,n-1)

def main():
    turtle.setup(800,800)
    turtle.penup()
    turtle.goto(-300,-50)
    turtle.pendown()
    turtle.pensize(2)
    level = 3
    koch(400,level)
    turtle.right(120)
    koch(400,level)
    turtle.right(120)
    koch(400,level)
    turtle.hideturtle()
    turtle.done()
main()
```



