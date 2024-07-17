#CALCULATOR WHICH CLACULATES THE BASIC OPERATION IN THE PYTHON..

# def func(choose):
#  return choose

a=int(input('ENTER THE NUMBER FIRST :\n'))
print()
b=int(input("ENTER THE NUMBER SECOND :\n"))
print()

choose=input("PLEASE CHOOSE THE OPERATION +,-,/,* etc..")
if(choose=="+"):
    print("YOU CAN CHOOSE THE ADDITION FUNCTION")
    print("THE ADDITION OF THE NUMBER IS:", a+b)
if(choose=="-"):
    print("YOU CAN CHOOSE THE SUBTRACTION FUNCTION")
    print("THE SUBTRACTION OF THE NUMBER IS:", a-b)
if(choose=="*"):
    print("YOU CAN CHOOSE THE MULTIPLICATION FUNCTION")
    print("THE MULTIPLICATION  OF THE NUMBER IS:", a*b)
if(choose=="/"):
    print("YOU CAN CHOOSE THE DIVISION FUNCTION")
    print("THE DIVISION OF THE NUMBER IS:", a/b)
else:
    print("YOU CAN NOT CHOOSE THE APPROPIRATE SYMBOL TO DONE THE NUMBER")
