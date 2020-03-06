## 字符串操作

#### Practice-I

```python
# WeekNamePrint.py
weekStr = "星期一星期二星期三星期四星期五星期六星期日"
weekID =  eval(input("请输入星期数字(1-7)："))
pos = (weekID-1) * 3
print(weekStr[pos: pos+3])
```

#### Practice-II

```python
# WeekNamePrint.py
weekStr = "一二三四五六日"
weekID =  eval(input("请输入星期数字(1-7)："))
pos = (weekID-1)
print("星期"+ weekStr[pos])
```

#### 字符串处理方法

```R
str.lower()或者str.upper() # 全部字符小写或大写
str.split() # 返回被分隔的列表
str.count() # 计算子串在str中出现的次数
str.replace(old,new) # old被new替换
str.center(width[,fillchar]) # "python".center(20,"=)结果为 =======python=======
str.strip(chars) # 从str中去掉起左右侧chars中列出的字符 “=python=”.strip("=np")结果为ytho
str.join(iter) # 在iter变量除最后元素外每个元素后增加一个str “,”.join(“12345”)结果为“1,2,3,4,5”
```



```python
for i in range(12):
    print(chr(9800 + i), end="")
```



## Time库

```python
import time
time.time()
time.ctime()
time.gmtime()

start = time.perf_counter()
end = time.perf_counter()
end-start

def wait():
    time.sleep(3.3)
wait()

t = time.gmtime()
time.strftime("%Y-%m-%d %H:%M:%S",t)

timeStr = "2020-03-06 01:27:15"
time.strptime(timeStr,"%Y-%m-%d %H:%M:%S")
```

### Practice-I

```python
# TextProBar.py
import time
scale = 10
print("------执行开始------")
for i in range(scale+1):
    a = '*' * i
    b = '.' * (scale-i)
    c = (i/scale)*100
    print("{:^3.0f}%[{}->{}]".format(c,a,b))
    time.sleep(0.5)
print("------执行结束------")
```

#### Practice-II

```python
# TextProBar.py
import time
for i in range(101):
    print("\r{:3}%".format(i),end="")
    time.sleep(0.5)
```

#### Practice-III

```python
import time
scale = 50
print("执行开始".center(scale//2,"="))
start = time.perf_counter()
for i in range(scale+1):
    a = '*' * i
    b = '.' * (scale-i)
    c = (i/scale)*100
    dur = time.perf_counter()-start
    print("\r{:^3.0f}%[{}->{}]{:.2f}".format(c,a,b,dur),end="")
    time.sleep(0.1)
print("\n"+"执行结束".center(scale//2,"="))
```

