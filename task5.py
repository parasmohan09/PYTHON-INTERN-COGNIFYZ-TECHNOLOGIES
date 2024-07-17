# PROGRAMM TO CHECK THE PALINDROME IN THE PYTHON 

# PALINDROME IS NOTHING IT IS THE ANY WORD,SENTENCE,PHARSE ETC WHICH IS SAME FROM BOTH SIDE IT WHEN WE CAN WRITE THE WORD LIKE :
    
#     MADAM - MADAM CAN BE SAME FROM BOTH SIDE 
#     ROTOR - ROTOR ITS ALSO SAME
# NOW WE CAN WRITE THE PROGRAMM TO CHECK

def check_palindrome(string):
    # Check if the string is equal to its reverse
    return string == string[::-1]#it means string is equal to reverse string in this palindrome..

a=input("PLEASE ENTER THE WORD OR SENTENCE::\n")

if check_palindrome(a):
    print("THE STRING IS THE PALINDROME")
else:
    print("THE STRING IS NOT THE PLAINDROME")    
