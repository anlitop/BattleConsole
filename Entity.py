class Entity:
    def __init__(self,data,id):
        print("a entity init")
        self.name=data["name"]
        self.attack=data["attack"]
        self.hp=data["hp"]
        self.speed=data["speed"]
        self.skills_id=data["skills"]
        self.entity_id=id
    
    def update(self):
        pass
    def work(self,skill_id):
        #获取技能信息
        #根据技能选择目标
        #对目标释放技能
        print("{0}释放{1}".format(self.name,skill_id))
        pass
    def on_work(self):
        pass
    def e_destory(self):
        pass
    def e_create(self):
        pass

    