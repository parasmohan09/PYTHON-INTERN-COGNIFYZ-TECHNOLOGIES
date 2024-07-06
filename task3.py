#PROGRAMM TO CHECK PASSWORD STENTGH IN PYTHON.

import string #we can use the import kewyword to import the string module in the python it is the built in module in the python so,we can directly use the string in the python.

password=input("ENTER THE PASSWORD OF YOUR ACCOUNT:\n")#use to take user input in code.because we can take password from the user.

# print(password) used to print the password.

#now we can create the function which only shows the lenthgh of password means how many charcter can be present in the password..
def passlen():
    print("THE LENTH OF YOUR PASSWORD IS THE:",len(password))

    
def passupper(s):
 return any(char.isupper() for char in s)#this function can be used to check the presence of uppercase letter can be used in the python or not or give boolean value means true or false.

def paslower(l):
    return any(char.islower() for char in l)#this function can be used to check the presence of lower letter used in password or not.

def passdigit(d):
    return any(char.isdigit() for char in d)# this is used to check the digit can be used in the password or not.then we create this functyion 

def specialchar(c):
 special_chars = set(string.punctuation)#we can not check the the directly special character in the password then we can create the variable and in this variable set string.punctuation can be used.
 
 return any(char in special_chars for char in c)# in this we can check the presence of special charcter in the password..

 
passlen()#calling a passlen function.

print("UPPER CASE LETTER PRESENCE  IS PRESENT THEN GIVE 'TRUE'\n OTHERWISE 'FALSE':\n",passupper(password))

print("LOWER CASE LETTER PRESENCE IS PRESENT THEN GIVE 'TRUE'\n OTHERWISE 'FALSE':\n",paslower(password))

print("DIGITS PRESENCE IN YOUR PASSWORD IF PRESENT THEN 'TRUE '\n THEN OTHERWISE 'FALSE':\n",paslower(password))

print("SPECIAL CHARCTER PRESENCE IS PRESENT THEN GIVE 'TRUE'\n OTWERWISE 'FALSE'",specialchar(password))

#************************************************************************#
'''IMPORTANT TERM'''

#concept of any function in the python..
#syntax to create or use the any function.
# any function can be used to check the presence of any method of string and for loop can be used to check each and every charcter in string if its present then print it 
# any()used to give or return the boolean value in the python is also known as the any function in the python.


# return any(char.isupper() for char in p ). THIS IS THE SYNTAX OF ANY FUNCTION IN THE PYHON..


