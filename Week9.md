## 字典

#### 字典类型定义

```python
# 键值对
# 字典是键值对的集合，键值对之间无序
# 采用{}和dict()创建，键值对用冒号：表示
{<键1>:<值1>,<键2>:<值2>，...,<键n>:<值n>}
# Example
d = {"China":"Beijing","USA":"Washington","France":"Paris"}
d["China"]

# 空字典
d = {}
d = dict()
```

#### 字典处理函数及方法

```python
del d[k] # 删除字典d中键k对应的数据值
k in d # 判断键k是否在字典d中，如果在返回True,否则False
d.keys() # 返回字典d中所有的键的信息
d.values() # 返回字典d中所有的值的信息
d.items()# 返回字典d中所有的键值对信息

d.get(k,<default>) # 键k存在，则返回相应值，不在则返回<default>值
d.pop(k,<default>) # 键k存在，则取出相应值，不在则返回<default>值
d.popitem() # 随机从字典d中取出一个键值对，以元组形式返回
d.clear() # 删除所有的键值对
len(d) # 返回字典d中元素的个数
```

#### jieba库

```python
jieba.lcut() #精确模式
jieba.lcut(s,cut_all=True) #全模式
jieba.lcut_for_search(s) #搜索引擎模式
jieba.add_word(w) #向分词词典增加新词
```

#### Practice-文本词频统计

##### Hamlet

```python
def getText():
    txt = open('hamlet.txt','r').read()
    txt =  txt.lower()
    for ch in ',./<>?;:"[][\|}`~!@#$%^&*()-_=+':
        txt = txt.replace(ch," ")
    return txt
hamletTxt = getText()
words = hamletTxt.split()
counts = {}
for word in words:
    counts[word] = counts.get(word,0) + 1
items = list(counts.items())
items.sort(key=lambda x:x[1],reverse=True)
for i in range(10):
    word,count = items[i]
    print("{0:<10}{1:>5}".format(word,count))
```

##### 三国演义出场人物统计

```python
import jieba
txt = open('threekingdoms.txt','r',encoding='utf-8').read()
excludes = {"将军","却说","荆州","二人","不可","不能","如此"}
words = jieba.lcut(txt)
counts = {}
for word in words:
    if len(word) == 1:
        continue
    elif word == "诸葛亮" or word == "孔明曰":
        rword = "孔明"
    elif word == "关公" or word == "云长":
        rword = "关羽"
    elif word == "玄德" or word == "玄德曰":
        rword = "刘备"
    else:
        rword = word
    counts[rword] = counts.get(rword,0) + 1
for word in excludes:
    del counts[word]
items = list(counts.items())
items.sort(key=lambda x:x[1],reverse=True)
for i in range(15):
    word,count = items[i]
    print("{0:<10}{1:>5}".format(word,count))
```

