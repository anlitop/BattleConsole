import BattleManager
import Entity

class Battle:
	def __init(self):
		self.MAX_TURN_NUMBER=8
		self.EntityArray=[]
#实体相关
#战场相关
	def battle_start(self,entitys):
		#传入战队初始化信息
		self.EntityArray=entitys
		self.battle_start(8)
	def battle_excute(self,turn_number):
		for turn in range(0,turn_number):
			print("第{0}回合开始".format(turn))
			self.TurnStart()
			self.TurnExcute()
			self.TurnEnd()
		self.battle_end()
	def battle_end(self):
		pass
#回合相关	
	def TurnStart(self):
		pass
		#[回合开始前BUFF处理]
		#按照速度排序，压入队中
	def TurnExcute(self):
		#依次出手
		for entity in self.EntityArray:
			self.ActStart(entity)
			self.ActExcute(entity)
			self.ActEnd(entity)
	def TurnEnd(self):
		pass
#出手相关
	def ActStart(self,actor):
		#遍历出手者[出手前]BUFF
		#从actor中skill组件中，依次释放技能
		pass
	def ActExcute(self,actor):
		pass
	def ActEnd(self,actor):
		pass
#主入口
	def Run(self):
		pass




