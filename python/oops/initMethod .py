class Dog:
    attr1 = "mammal"
    def __init__(self, name):
        self.name = name

Sheru = Dog("Sheru")
Moti = Dog("Moti")
 

print("Rodger is a {}".format(Sheru.__class__.attr1))
print("Tommy is also a {}".format(Moti.__class__.attr1))
 
print("My name is {}".format(Sheru.name))
print("My name is {}".format(Moti.name))