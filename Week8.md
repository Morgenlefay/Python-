## 集合

#### 定义

```python
# 集合用{}表示，元素间用逗号分隔
# 集合中每个元素唯一，不存在相同元素
# 集合元素之间无序
A = {"python",123,("python",123)} # 使用{}建立集合
B = set("pypy123") # 使用set()建立集合
C = {"python",123，"python",123}
```

#### 集合操作符

```python
S|T # 并集
S-T # 差集
S&T # 交集
S^T # 补集
S <= T 或 S < T # 返回True/False，判断S和T的子集关系
S >= T 或 S > T # 返回True/False，判断S和T的包含关系
```

#### 集合处理方法

```python
S.add(x) # 如果x不在集合S中，将x增加到S
S.discard(x) # 移除S中元素x,如果x不在集合S中，不报错
S.remove(x) # 移除S中元素x,如果x不在集合S中，产生KeyError异常
S.clear() # 移除S中所有元素
S.pop() # 随机返回S的一个元素，更新S,若S为空产生KeyError异常
S.copy() # 返回集合S的一个副本
len(S) # 返回集合S的元素个数
x in S # 判断S中的元素x，x在集合S中，返回True，否则返回False
x not in S # 判断S中的元素x，x不在集合S中，返回True，否则返回False
set(x) # 将其他类型变量x转变为集合类型
```

## 序列

#### 序列类型通用操作符

```python
x in s # 如果x是序列S中的元素，返回True，否则返回False
x not in s # 如果x不是序列S中的元素，返回True，否则返回False
s+t # 连接两个序列s和t
s*n或n*s # 将序列s复制n次
s[i] #索引，返回s中的第i个元素，i是序列的序号
s[i:j]或s[i:j:k] # 切片，返回序列s中第i到第j以k为步长的元素子序列
```

#### 序列类型通用函数和方法

```python
len(s) #返回序列s的长度
min(s) #返回序列s的最小元素，s中的元素需要可比较
max(s) #返回序列s的最大元素，s中的元素需要可比较
s.index(x)或s.index(x,i,j) # 返回序列s从i到j位置中第一次出现元素x的位置
s.count(x) #返回序列s中出现x的总次数
```

#### 列表类型及操作

```python
ls(i)=x #替换列表ls第i元素为x
ls[i:j:k]=lt #用列表lt替换ls切片后所对应元素子列表
del ls[i] #删除列表ls中第i元素
del ls[i:j:k] #删除列表ls中第i到第j以k为步长的元素
ls=ls+lt #更新列表ls,将列表lt元素增加至列表ls中
ls=ls*n #更新列表ls,其元素重复n次

ls.append(x) #在列表ls最后增加一个元素x
ls.clear() #删除列表ls中所有元素
ls.copy() # 生成一个新列表，赋值ls中所有元素
ls.insert(i,x) #在列表ls的第i位置增加元素x
ls.pop(i) #将列表ls中第i位置元素去除病删除该元素
ls.remove(x) #将列表ls中出现的第一个元素x删除
ls.reverse() #将列表ls中的元素反转
```

#### Practice-基本统计值

```python
# CalStatistics.py
# 获取用户不定长度的输入
def getNum():
    nums = []
    iNumStr = input("请输入数字（回车退出）：")
    while iNumStr != "":
        nums.append(eval(iNumStr))
        iNumStr = input("请输入数字（回车退出）：")
    return nums

# 计算平均值
def mean(numbers):
    s = 0.0
    for num in numbers:
        s = s + num
    return s/len(numbers)

# 计算方差
def dev(numbers,mean):
    sdev = 0.0
    for num in numbers:
        sdev = sdev + (num-mean)**2
    return pow(sdev/(len(numbers)-1),0.5)

# 计算中位数
def median(numbers):
    sorted(numbers)
    size = len(numbers)
    if size % 2 == 0:
        med =(numbers[size//2-1]+numbers[size//2])/2
    else:
        med = numbers[size//2]
    return med

n = getNum()
m = mean(n)
print("平均值：{}，方差：{:.2}，中位数：{}.".format(m,dev(n,m),median(n)))
```

