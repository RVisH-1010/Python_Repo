# print("starting of day 4!!!")
# 1. topic: super keyword
# class employee:
#     def __init__(self, name, id):
#         self.name = name
#         self.id = id
# class programmer(employee):
#     def __init__(self, name, id,lang):
#         super().__init__(name, id)
#         self.lang = lang

# rohan = employee("Rohan", 8789)
# hari = programmer("hari", 6798, "python")
# print(hari.name,hari.id, hari.lang)        
# print(rohan.name, rohan.id)



# 2. magic or dunder method in py
# class employee:
#     def __init__(self,name):
#         self.name = name
#     def __len__(self):
#         i=0 
#         for c in self.name:
#             i = i+1
#         return i
#     # def __str__(self):
#     #     return f"the employee is {self.name} (str)"
    
#     def __repr__(self):
#         return f"the empployee is {self.name} (repr)"
#     def __call__(self, *args, **kwds):
#         print("hello world!!")

# e = employee("Roahn")
# print(e.name)
# print(len(e))



# 3. method overriding
# class shape:
#     def __init__(self,x, y):
#         self.x = x
#         self.y = y
#     def area(self):
#         return self.x*self.y    

# class circle(shape):
#     def __init__(self, radius):
#         self.radius = radius
#         super().__init__(radius,radius)
#     def area(self):
#         return 3.14*super().area()        

# c = circle(7)
# print(c.area())            



# operator overloading
# print("operator overloading")
# class vector:
#     def __init__(self, i ,j ,k):
#         self.i = i
#         self.j = j
#         self.k = k 
#     def __str__(self):
#         return f"{self.i}i+{self.j}j+{self.k}k"
#     def __add__(self,x):
#         return vector(self.i+x.i,self.j+x.j,self.k+x.k)
    
# v1 = vector(1,2,8)
# print(v1)
# v2 = vector(2,3,4)
# print(v2) 
# print(v1+v2)
# print(type(v1+v2))   



# 4. single inheritance in py
class animal:
    def __init__(self,name, species):
        self.name = name 
        self.species = species
    def make_sound(self):
        print(f"sound made by {self.name}")

class cat(animal):
    def __init__(self, name, color):
        animal.__init__(self, name, species = "cat")            
        self.color = color
    def make_sound(self):
        print("Meow")

c = cat("cat","balck")
a = animal("bird", "bird")
print(a.make_sound())
print(c.make_sound())
