def a(deco):
    return deco.upper()

print(a("niraj"))    



#add deco function

def a(x):
    def b(y):
        return x+y
    return b
add = a(20)
print(add(30))  




