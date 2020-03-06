## 天天向上的力量

#### Practice-I

```python
# DayDayUp.py
dayfactor = 0.005
dayup = pow(1+dayfactor,365)
daydown = pow(1-dayfactor,365)
print("向上：{:.2f},向下：{:.2f}".format(dayup,daydown))
```

#### Practice-II

```python
# DayDayUp.py
dayup = 1.0
dayfactor = 0.01
for i in range(365):
    if i % 7 in [6,0]:
        dayup = dayup*(1-dayfactor)
    else:
        dayup=dayup*(1+dayfactor)

print("工作日的力量：{:.2f}".format(dayup))
```

#### Practice-III

```R
# DayDayUp.py

def dayUP(df):
    dayup = 1.0
    for i in range(365):
        if i % 7 in [6,0]:
            dayup = dayup*(1-0.01)
        else:
            dayup = dayup*(1 + df)
    return dayup

dayfacotr = 0.01
while dayUP(dayfactor) < 37.78:
    dayfactor = dayfactor + 0.001

print("工作日的力量努力参数：{:.3f}".format(dayfactor))
```

