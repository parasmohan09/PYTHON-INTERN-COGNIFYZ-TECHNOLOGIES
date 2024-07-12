#PROGRAMM TO CREATE A TEMPREATURE CONVERSION IN THE PYTHON..

def celusis_to_farhenit(celsius):
    return(celsius*9/5)+32

def farhenit_to_celusis(faranit):
    return(faranit-32)*5/9

numb=int(input("ENTER THE TEMPREATURE PLEASE:"))


ask=input("CHOOSE WHICH CONVERTER YOU NEED\n IF YOU NEED THE celusis_to_farhenit THEN WRITE ctof OTHERWISE ftoc\n")

if(ask=='ctof'):
   m=celusis_to_farhenit(numb) 
   print(m)
elif(ask=='ftoc'):
    p=farhenit_to_celusis(numb)
    print(f"{numb}*f to {p}*c") 
    
    
   
