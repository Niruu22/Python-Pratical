class error(Exception):
    pass
class zeroDivison (error):
    pass
try:
    i_num=int(input("Enter no.: "))
    if i_num == 0:
        raise zeroDivison
    else:
        print("No is ", i_num)
except zeroDivison:
    print("Input value is zero try again")
    print()            