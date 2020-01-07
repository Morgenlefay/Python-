## pip
#### 升级
python -m pip install --upgrade pip
#### 安装包
pip install
#### 卸载包
pip uninstall
#### 查看版本
pip -V
#### 输出环境
pip freeze > C:\Users\Lenovo-PC\Documents\requirements.txt
#### 安装环境包
pip install -r C:\Users\Lenovo-PC\Documents\requirements.txt

## 变量命名规则
由字母，数字，_组成，不能以数字开头

严格区分大小写

不能使用python关键字
```python
import keyword
print(keyword.kwlist)
```
