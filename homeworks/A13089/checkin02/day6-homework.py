#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: pluto

# 今日的作业
# 有十种菜
#   白菜、萝卜、西红柿、甲鱼、龙虾、生姜、白芍、西柚、牛肉、水饺
# 
# 1. 老妈来到了菜市场，从下标 0 开始买菜，遇到偶数的下标就买
#    遇到奇数的下标就不买，买的数量为下标 + 1 斤
#    （请写程序模拟整个过程）
#    （注意单一职责原则）
#    （注意灵活使用 def 函数（代码块））
#    
# 【提示】：
#   输出结果可能为
#   ‘老妈来到菜市场
#    老妈看到白菜，买了 1 斤
#    老妈继续逛
#    老妈看到xxx, 不买
#    老妈继续逛
#    ...
#   '
#  2. 完成后，用今天的学到的列表知识，加 3 个菜
#  3. 完成后，用今天的学到的列表知识，让老妈只逛第 5~9 个菜
def print_list(lst):
	for lst_item in lst:
		print '菜场里有人在卖%s' % (lst_item)

def homework():
	print '老妈来到菜市场 '
	lst = ['白菜 ','萝卜 ','西红柿 ','甲鱼 ','龙虾 ','生姜 ','白芍 ','西柚 ','牛肉 ','水饺 ']
	index = 0
	for lst_item in lst:
		if index%2 == 0:
			print '老妈看到%s，买了%d斤' % (lst[index],index+1)
			print '老妈继续逛'
		else:
			print '老妈看到%s, 不买' % (lst[index])
			if index < 9:
				print '老妈继续逛'
			else:
				print '----------买完了，不逛了-------------- '
		index = index +1
	
	try:
		lst.append('苹果 ','香蕉 ','橘子 ')  	#加三个菜
	except Exception, e:
		print e

	print_list(lst)
	
if __name__ == '__main__':
	homework()