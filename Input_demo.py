# 输入：input
name=input('请输入名字：')
print(name)

# 练习
'''
游戏：捕鱼达人
输入游戏者用户名：
输入明码：
充值：500
'''

print('''
****************
     捕鱼达人
****************
''')
username=input('输入游戏者用户名：')
password=input('输入密码：')
print('%s请充值才能开始游戏' % username)
coins=input('请充值：')
coins=int(coins)
print('%s充值成功！当前游戏币是：%d' % (username,coins))


# 练习
'''
游戏：王者荣耀
角色：
拥有的装备：
输入想购买的装备：
购买装备：500
付款金额：
'''

print('''
****************
     英雄联盟
****************
''')
role=input('请输入角色名称：')
equipment=input('拥有的装备：')
upgrade_equipment=input('输入想购买的装备：')
pay=input('请输入付款金额：')
equipment=upgrade_equipment 

print('{}拥有{}装备，购买此装备花了{}钱'.format(role,equipment,pay))



















