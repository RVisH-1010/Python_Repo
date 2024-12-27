# print("Hello World")
class person:
    def __init__(self,n , o):
        print("class person is called.")
        self.name = n
        self.occ = o

    name = "harry"
    occ = "coder"
    def show(self):
        print(f"my name is {name} & i am {occ}") 

a = person("rohan ","student")
a.show()

