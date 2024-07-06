#PROGRAMM TO CHECK PASSWORD STENTGH IN PYTHON.

import string
password=input("ENTER THE PASSWORD OF YOUR ACCOUNT:\n")
print(password)

def passlen():
    print("THE LENTH OF YOUR PASSWORD IS THE:",len(password))
    
def passupper(s):
 return any(char.isupper() for char in s)

def paslower(l):
    return any(char.islower() for char in l)

def passdigit(d):
    return any(char.isdigit() for char in d)

def specialchar(c):
 special_chars = set(string.punctuation)
 return any(char in special_chars for char in c)

 
passlen()
print("UPPER CASE LETTER PRESENCE  IS PRESENT THEN GIVE 'TRUE' AND IFNOT THEN GIVE 'FALSE':\n",passupper(password))

print("LOWER CASE LETTER PRESENCE IS PRESENT THEN GIVE 'TRUE' AND IFNOT THEN GIVE 'FALSE':\n",paslower(password))

print("DIGITS PRESENCE IN YOUR PASSWORD IF PRESENT THEN 'TRUE ' IF NOT THEN PRESENT 'FALSE':\n",paslower(password))

print("SPECIAL CHARCTER PRESENCE IS PRESENT THEN GIVE 'TRUE' OTWERWISE 'FALSE'",specialchar(password))



        