from collections import OrderedDict
#collections OrderDict 一个有序字典

from random import randint
#包含生成随机数的函数
words = OrderedDict()

words["变量"] = "可以改变值的"
words["while"] = "can run circle"
words["遍历"] = "依次读出"

#for key,val in words.items():
#	print(key + ": " + val)
 
x = randint(1,6)

class Die:
	'''一个可以设置面数的筛子，使用randint 生成随机数'''
	def __init__(self, face):
		self.face = face
	def roll_die(self):
		i = 1
		while(i <= self.face):
			print(randint(1,self.face))
			i+=1
		print("End!\n")
	def Set_face(self, face):
		self.face = face

tmp = Die(6)
tmp.roll_die()

tmp.Set_face(10)
tmp.roll_die()

tmp.Set_face(20)
tmp.roll_die()

print(tmp.__doc__)
