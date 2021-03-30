#Cherilus Sam Bracley
#cherilussambracley@gmail.com
import random

LETTERS=['a','b','c','d',
         'e','f','g','h',
         'i','j','k','l',
         'm','n','o','p',
         'q','r','s','t',
         'u','v','w','x',
         'y','z']




RANDOM_INDEX = random.randint(0,25)

RANDOM_VALUES= LETTERS[RANDOM_INDEX]

#print(RANDOM_VALUES)



USER_ONE= input("Insert your name... (Player One) \n")
USER_TWO= input("Insert your name  (Player Two) \n")
USER_THREE =input("Insert your name...  (Player Three) \n")

RANDOM_INDEX = random.randint(0,25)
RANDOM_VALUES= LETTERS[RANDOM_INDEX]




PLAYER_ONE_CHOICE= 3
PLAYER_TWO_CHOICE= 3
PLAYER_THREE_CHOICE= 3





GAME = "START"






while True:
    RANDOM_INDEX = random.randint(0,25)
    RANDOM_VALUES= LETTERS[RANDOM_INDEX]
    


    ask_value_one = input(str(USER_ONE) +" \n")
    if(ask_value_one == RANDOM_VALUES):
        print("You win "+ str(USER_ONE))
    else:
        print("The word was "+ str (RANDOM_VALUES))
        print("You lose "+ str(USER_ONE))
        PLAYER_ONE_CHOICE = PLAYER_ONE_CHOICE - 1
    



    ask_value_two = input(str(USER_TWO) +" \n")
    if(ask_value_two == RANDOM_VALUES):
        print("You win "+ str(USER_TWO))
    else:
        print("The word was "+ str (RANDOM_VALUES))
        print("You lose "+ str (USER_TWO))
        PLAYER_TWO_CHOICE = PLAYER_TWO_CHOICE - 1


    ask_value_three = input(str(USER_THREE) +" \n")
    if(ask_value_three == RANDOM_VALUES):
        print("You win "+ str(USER_THREE))
    else:
        print("The word was "+ str (RANDOM_VALUES))
        print("You lose " + str(USER_THREE))
        PLAYER_THREE_CHOICE = PLAYER_THREE_CHOICE - 1




    if(PLAYER_ONE_CHOICE == 0):
        print("RESUME")
        print(str(USER_ONE)+ " " + str(PLAYER_ONE_CHOICE))
        print(str(USER_TWO)+ " " + str(PLAYER_TWO_CHOICE))
        print(str(USER_THREE)+ " " + str(PLAYER_THREE_CHOICE))
        break


    if(PLAYER_TWO_CHOICE == 0):
        print("RESUME")
        print(str(USER_ONE)+ " " + str(PLAYER_ONE_CHOICE))
        print(str(USER_TWO)+ " " + str(PLAYER_TWO_CHOICE))
        print(str(USER_THREE)+ " " + str(PLAYER_THREE_CHOICE))
        break


    if(PLAYER_THREE_CHOICE == 0):
        print("RESUME")
        print(str(USER_ONE)+ " " + str(PLAYER_ONE_CHOICE))
        print(str(USER_TWO)+ " " + str(PLAYER_TWO_CHOICE))
        print(str(USER_THREE)+ " " + str(PLAYER_THREE_CHOICE))
        break





      
