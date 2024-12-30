print("starting of day 4!!!")
# 1. topic: super keyword
class employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id
class programmer(employee):
    def __init__(self, name, id,lang):
        super().__init__(name, id)
        self.lang = lang

rohan = employee("Rohan", 8789)
hari = programmer("hari", 6798, "python")
print(hari.name,hari.id, hari.lang)        
print(rohan.name, rohan.id)