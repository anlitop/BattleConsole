class Buff:
    def __init__(self,data):
        self.level=data["level"]
        self.type=data["type"]
        self.owner=None
        self.giver=None
        self.name=data["name"]
        self.effect_type=data["effect_type"]
        self.times=data["times"]
        self.turns=data["turns"]
        self.values=data["values"]
    def work(self):
        pass