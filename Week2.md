## Turtle

```python
# PythonDraw.py
import turtle 
turtle.setup(650,350,200,200) # (650,350)画图框大小；(200,200)画图框在屏幕中的位置
turtle.penup() # 抬笔
turtle.fd(-250)
turtle.pendown() # 落笔
turtle.pensize(25) # 画笔宽度
turtle.pencolor("purple") # 画笔颜色
turtle.seth(-40) # 画笔方向
for i in range(4):
    turtle.circle(40,80) # 海龟画弧
    turtle.circle(-40,80)
turtle.circle(40,80/2)
turtle.fd(40)
turtle.circle(16,180)
turtle.fd(40 * 2/3)
turtle.done()

```

#### Practice-I

```python
# turtle角度坐标体系
import turtle
turtle.left(45)
turtle.fd(150)
turtle.right(135)
turtle.fd(300)
turtle.left(135)
turtle.fd(150)
```

#### Practice-II

```python
# turtle空间坐标体系
import turtle
turtle.goto(100,100)
turtle.goto(100,-100)
turtle.goto(-100,-100)
turtle.goto(-100,100)
turtle.goto(0,0)

# turtle.fd(d)前进d像素
# turtle.bk(d)后退d像素
# turtle.circle(r,angle)
```

