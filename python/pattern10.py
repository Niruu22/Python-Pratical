row = int(input("Enter a no : "))
for i in range(row,0,-1):
    for j in range(row-i):
        print(" " , end="")
    for j in range(2*i-1):
        print('*',end='') 
    print()    