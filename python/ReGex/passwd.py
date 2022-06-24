from numpy import char


def password_check(passwd):
    specialSym= ['$','@','#','%']
    val=True

    if len (passwd) <6 :
        print('length should be at least 6')
        val=False
    if len (passwd) >20 :
        print('length should be not greater than 8')
        val=False    
    if not any (char.isdigit() for char in passwd):
        print('password should have at least one Numerical')
        val=False
    if not any (char.isupper() for char in passwd):
        print('password should have at least one UpperCase')
        val=False
    if not any (char.islower() for char in passwd):
        print('password should have at least one LowerCase')
        val=False            
    if not any (char in specialSym  for char in passwd):
        print('password should have at least one Symbol')
        val=False
    if val:
        return val

#Main method 
def main():
    passwd ='Niraj22'
    if(password_check(passwd)):
        print("password is valid")
    else:
        print("Invalid passsword") 


#Driver 
if __name__ == '__main__':
    main()                            