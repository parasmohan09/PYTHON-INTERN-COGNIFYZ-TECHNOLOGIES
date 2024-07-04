#PROGRAMM TO GUESSING A NUMBER GAME  IN PYTHON.
#1.we can generate a random number first in this programm.

import random #IMPORT KEYWORD CAN BE USED TO IMPORT  MODULE IN PYTHON.

r=random.randint(1,100) # RANDINT CAN BE USED TO SHOW ONLY INTEGER RANDOM NUMBER.


attemepts=0 # INTILIAZATION OF WHILE LOOP IN PYTHON.
 

while True: #WE CAN USE IT BECAUSE LOOP TAKES USER INPUT GIVE AGAIN AND AGAIN IF ITS TRUE THEN STOP 
    user_guess=int(input("CHOOSE THE NUMBER BETWEEN 1 TO 100 \nPLAEASE GUESSING NUMBER\nWON 1000 RUPEE IF NUMBER GUESSING IS CORRECT\n"))
    
    attemepts += 1 # check 
   

    if (user_guess<r): # desicion making statements.#indentation maintain
     print("your guess is to low number ",user_guess)
     print("you loose the game,'try agin' ")
    elif(user_guess>r):
     print("your guess is to high",user_guess)
     print("you loose the game,'try agin'/")  
    
    elif(user_guess==r):
     print("your guess equal to random number",r)
     print("you won the 1000 rupee,thanks for plaing this game")
     break
    
    print("THE GAME IS OVER\n")    
    
          



    

