from Entity import *
import TableManager
class EntityManager:
    def __init__(self):
        self.entity_array=[]
        self.entity_id=0
        self.table_asset=TableManager.load_all('E:\\BattleConsole\\Table')
    def add_entity(self,data):
        print("产生1个entity")
        self.entity_id+=1
        current_entity=Entity(TableManager.GetTable("Entity.json"),self.entity_id)
        #加入列表
        self.entity_array.append(current_entity)
        return current_entity
    def del_entity(self):
        pass
    