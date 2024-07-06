#PROGRAMM OF FIBONACCI SEQUENCE IN THE PYTHON.
# CONCEPT OF THE FIBONACCI SEQUENCE IS NOTHING THERE ARE ALWAYS TWO NUMBER IN FIBOCANNI SEQUENCE IS PRESENT 0 ITS FIRST NUMBER IN FIBONACCI SEQUENCE AND 1 IT IS THE SECOND TERM OF THE FIBOCANNI SEQUENCE IT THE PYTHON..

def fibonacci_series(n):# this function can be used to create or show fibonacci series concept in python.
    if n<=1:# desicion making statement can be used to make desicion and return particilar block.
        return n
    else:
        return (fibonacci_series(n-1)+fibonacci_series(n-2))#(n-1) is the last element of fibonacci series and (n-2) is the second last element which is add.
    #in fibonacci series have two elements which is add to give next element in fibonacci series .

n=int(input("ENTER THE TERM OF FIBONACCI SERIES YOU WANT:\n"))#takes user input integer.
    
fibonacc=[fibonacci_series(i) for i in range(n)]# in this a variable can stores the fibonacci series and for loop can be used.

print("FIBONACCI SERIES IS:\n")
print(fibonacc)#its print fibonacci series 
    
    
