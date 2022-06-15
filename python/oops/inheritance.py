class Dog:

    breed="Lab"

    def __init__(self,name):
         self.name=name

    def speak(self):
        print("My Dog name is {}".format(self.name))


Moti = Dog("Moti")
Sheru = Dog("Sheru")

Moti.speak()
Sheru.speak()




  
