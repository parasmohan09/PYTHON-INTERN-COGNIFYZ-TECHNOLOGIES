#programm to number guesser in the python.

import random 

r=random.randint(1,500)
# print(r)

attempt=0
while True:
    i=int(input("PLEASE GUESS THE NUMBER BETWEEN 1 TO 500\n"))
    
    attempt+=1
    
    if(i < r):
        print(f"try again,too low number")
        print(f"the orginal number is the:{r}") 
    elif(i > r):
        print(f"try again guys, too high number")  
        print(f"the orginal number is the:{r}")  
    else:
        print("CORRECT NUMBER GUYS YOU WON THE 1000 RUPPE")
        print("CONGRATS GUYS,THANKS FOR GUESSING THEH NUMBER GUYS")
        print(f"THE RANDOM NUMBER IS{r} and you number is{input}")
    
    print("OK THANKS TO PLAY THIS GAME,BYE BYE") 
    
        
        


            
        
        
        
    
