## 程序的分支结构

#### 单分支结构

```python
guess = eval(input())
if guess == 99:
    print("Winner!")
```

#### 二分支结构

```python
guess = eval(input())
if guess == 99:
    print("Winner!")
else:
    print("Wrong!")

print("猜{}了".format("对" if guess==99 else "错"))
```

#### 多分支结构

```python
score = eval(input("请输入成绩："))
if 70 > score >= 60 :
    grade = "D"
elif 80 > score >= 70 :
    grade = "C"
elif 90 > score >= 80 :
    grade = "B"
elif 100 >= score >= 90 :
    grade = "A" 
elif 0 <= score < 60 :
    grade = "E" 
elif score <0 or score >100 :
    grade = "输入错误"
print("输入成绩属于级别：{}".format(grade))
```

#### 异常处理

```python
try:
    num = eval(input("请输入一个整数："))
    print(pow(num,2))
except:
    print("输入不是整数")

    
    
try:
    num = eval(input("请输入一个整数："))
    print(pow(num,2))
except NameError:
    print("输入不是整数")

try:
    <语句块1>
except:
    <语句块2>
else:
    <语句块3>
finally:
    <语句块4>
```



#### Practice-I

```python
# BMI
height, weight = eval(input("请输入身高（米)和体重\（公斤）[逗号隔开]："))
bmi = weight/pow(height,2)
print("BMI数值为：{:.2f}".format(bmi))

who = ""
if bmi < 18.5 :
    who = "偏瘦"
elif 18.5 <= bmi < 25 :
    who = "正常"
elif 25 <= bmi < 30  :
    who = "偏胖"
else:
    who = "肥胖"
print("BMI指标为:国际‘{0}’".format(who))

who = ""
if bmi < 18.5 :
    who = "偏瘦"
elif 18.5 <= bmi < 24 :
    who = "正常"
elif 24 <= bmi < 28  :
    who = "偏胖"
else:
    who = "肥胖"
print("BMI指标为:国内‘{0}’".format(who))
```

#### Practice-II

```python
# BMI
height, weight = eval(input("请输入身高（米)和体重\（公斤）[逗号隔开]："))
bmi = weight/pow(height,2)
print("BMI数值为：{:.2f}".format(bmi))

who,nat = "",""
if bmi < 18.5 :
    who,nat = "偏瘦","偏瘦"
elif 18.5 <= bmi < 24 :
    who,nat = "正常","正常"
elif 24 <= bmi < 25 :
    who,nat = "正常","偏胖"
elif 25 <= bmi < 28  :
    who,nat = "偏胖","偏胖"
elif 28 <= bmi < 30  :
    who,nat = "偏胖","偏胖"
else:
    who = "肥胖"
print("BMI指标为:国际‘{0}’,国内‘{1}’".format(who,nat))
```

## 程序的循环结构

#### 遍历循环

```python
for <循环变量> in <遍历结构> :
    <语句块>

# 计数循环（N次）
for i in range(N)
for in in range(M,N,K)
# 字符串遍历循环
for c in str
# 列表遍历循环
for item in ls
# 文件遍历循环
for line in fi
```

#### 无限循环

```python
while <条件>:
    <语句块>
```

#### 循环控制保留字

```python
# continue
for c in "PYTHON":
    if c == "T":
        continue
    print(c,end='')

# break
for c in "PYTHON":
    if c == "T":
        break
    print(c,end='')
```

```Python
s = "python"
while s != "":
    for c in s :
        print(c,end="")
    s = s[0:-1]
# pythonpythopythpytpyp
    
s = "python"
while s != "":
    for c in s :
        if c == "t":
            continue
        print(c,end="")
    s = s[0:-1]
# pyhonpyhopyhpypyp

s = "python"
while s != "":
    for c in s :
        if c == "t":
            break
        print(c,end="")
    s = s[0:-1]
# pypypypypyp
```

#### 循环的扩展用法

```python
for c in "PYTHON":
    if c == "T":
        continue
    print(c,end='')
else:
    print('正常退出')

for c in "PYTHON":
    if c == "T":
        break
    print(c,end='')
else:
    print('正常退出')
```

## random库

```python
# 基本随机数函数
import random
random.seed(10)
random.random() # [0,1]之间
random.random()

import random
random.seed(10)
random.random()
random.random()

# 扩展随机函数
randint(a,b) #生成一个[a,b]之间的整数
randrange(m,n,k) #生成一个[m,n)之间以k为步长的随机整数
getrandbits(k) #生成一个k比特长的随机整数
uniform(a,b) #生成一个[a,b]之间的随机小数
choice(seq) #从序列seq中随机选择一个元素
shuffle(seq) #将序列seq中的元素随机排列，返回打乱后的序列
```

## 圆周率计算

#### Practice-I

```python
# CalPi.py
pi = 0
N = 100
for k in range(N):
    pi = pi + 1/pow(16,k)*(4/(8*k+1)-2/(8*k+4)-1/(8*k+5)-1/(8*k+6))
print("圆周率值是：{}".format(pi))
```

#### Practice-II

```python
# CalPi.py
import random
import time
DARTS= 1000*1000
hits = 0.0
start = time.perf_counter()
for i in range(1, DARTS+1):
    x, y = random.random(), random.random()
    dist = pow(x**2 + y**2,0.5)
    if dist <= 1.0:
        hits = hits +1
pi = 4*(hits/DARTS)
print("圆周率值：{}".format(pi))
print("运行时间：{:.5f}s".format(time.perf_counter()-start))
```

