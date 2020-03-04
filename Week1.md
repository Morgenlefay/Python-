### Bioconda

```bash
## Miniconda
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh

## Add channels
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/conda-forge/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/msys2/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/menpo/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/pytorch/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/bioconda/
conda config --set show_channel_urls yes
```

### Environment

```
conda create -n Python python=3.7
conda activate Python
conda deactivate
```

### Practice-I

```python
# CalCircle.py
r = 25
area = 3.1415*r*r
print(area)
print("{:.2f}".format(area))
```

### Practice-II

```python
# TangentCirclesDraw.py
import turtle
turtle.pensize(2)
turtle.circle(10)
turtle.circle(20)
turtle.circle(40)
turtle.circle(80)
turtle.circle(160)
```

### Practice-III

```python
# StarDraw.py
from turtle import *
begin_fill()
for i in range(5):
    fd(200)
    rt(144)
end_fill()
done()
```

#### Practice-IIII

```python
# TempConvert.py
TempStr = input("请输入带有符号的温度值：")
if TempStr[-1] in ['F','f']:
    C = (eval(TempStr[0:-1]) - 32)/1.8
    print("转换后的温度是{:.2f}C".format(C))
elif TempStr[-1] in ['C','c']:
    F = 1.8*eval(TempStr[0:-1]) + 32
    print("转换后的温度是{:.2f}F".format(F))
else:
    print("输入格式错误")
```



