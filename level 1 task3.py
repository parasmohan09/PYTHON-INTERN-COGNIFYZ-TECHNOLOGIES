import re #re module or library can be used which is used to done the xhexk the string one by one from start to end 

def check_email(email):
    # Regular expression for validating an Email
    regex = r'^\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    
    # If the string matches the regex
    if re.match(regex, email):#re.match( function can be used)
        print("EMAIL IS VALID")
    else:
        print("EMAIL IS NOT VALID")

# Taking input from user
email = input("ENTER THE EMAIL ADDRESS: \n")
check_email(email)
