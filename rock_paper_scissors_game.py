import random
rock = '''
    --------
---'   -----)
       (-----)
       (-----)
----   (---)
    '-- (--)
'''
paper = '''
    --------
---'   -----)----
           -----)
          -------)
---      -------)
    '--------)
'''
scissors = '''
    --------
---'   -----)----
           ------)
        -----------)
---     (----)
   '--(---)
'''

game_images = [rock,paper,scissors]      
user_choice=int(input("Enter your choice: Type 0 for Rock, 1 for paper, 2 for scissors. "))
if user_choice >= 3 or user_choice < 0:
    print("You entered invalid number,You Lose.")
else:
    print(game_images[user_choice])
    computer_choice=random.randint(0,2)
    print("computer Chose: ")
    print(game_images[computer_choice])
    if computer_choice == user_choice:
        
        print("It's a draw")
    elif computer_choice == 0 and user_choice:
        
        print("You Lose")
    elif user_choice == 0 and computer_choice:
        
        print("You Win") 
    elif computer_choice > user_choice:
        
        print("You Lose ") 
    elif user_choice > computer_choice:
        
        print("You Win")
    
 
