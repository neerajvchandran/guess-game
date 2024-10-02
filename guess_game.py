import random

def shuffle_list(l_): #function to shuffle the list 
    random.shuffle(l_)
    return l_
def guess(): #function to guess the position of O
    i = ''
    while i not in ['1','2','3']:
        i = input("Guess the position of O from position values [1,2,3] : ")
    return int(i)
def game(lst,guessed): #function to check if the guess was correct
        if lst[guessed-1]=='O':
            print("You guessed it right!")
            print("Congrats")
        else:
            print("Oops :/ wrong answer")
            print(lst)
       
        
game_on = True
try_ = 1
while game_on :
    if try_ <=3:
        list_ = ['','','O']
        shuffled = shuffle_list(list_)
        guessd = guess()
        game(shuffled,guessd)
        try_+=1
        continue_ = input("Do you want to play again? Enter yes or no : ")
        if continue_[0].lower() == "y":
                    game_on = True
        elif continue_[0].lower() == "n":
            game_on = False
            print("Game over")
        
    else:
         print("End of chance. Sorry.")
         game_on = False
        
        
