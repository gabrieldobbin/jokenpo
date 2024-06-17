import random

def FromNumberToWord(choiceNumber):
    choiceWord=""
    if choiceNumber==1:
        choiceWord="Rock"
    if choiceNumber==2:
        choiceWord="Paper"
    if choiceNumber==3:
        choiceWord="Scissors"
    return choiceWord

playerName=input("Enter your name: ")
firstTo=input("How many round wins to win the match? ")
firstToNumber=int(firstTo)
print("Hello", playerName,"!")
roundNumber=1
print(playerName,"0 x 0 Computer")
playerScore=0
computerScore=0
while playerScore<firstToNumber and computerScore<firstToNumber:
    print("Round", roundNumber)
    print("Choose a number from 1 to 3")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")

    userChoice=input("Choose a number from 1 to 3: ")
    userChoiceNumber=int(userChoice) 
    userChoiceWord=FromNumberToWord(userChoiceNumber)

    computerChoiceNumber=random.randint(1, 3)
    computerChoiceWord=FromNumberToWord(computerChoiceNumber)
        
    print(playerName,"chose:", userChoiceWord,"!")
    print("Computer chose:", computerChoiceWord,"!")
    print()




    if userChoiceWord=="Rock" and computerChoiceWord=="Scissors" or \
       userChoiceWord=="Scissors" and computerChoiceWord=="Paper" or \
       userChoiceWord=="Paper" and computerChoiceWord=="Rock": 
        print(playerName,"wins!")
        playerScore=playerScore+1
    elif userChoiceWord=="Rock" and computerChoiceWord=="Paper" or \
       userChoiceWord=="Scissors" and computerChoiceWord=="Rock" or \
       userChoiceWord=="Paper" and computerChoiceWord=="Scissors": 
        print("Computer wins!")
        computerScore=computerScore+1
    else:
        print("It's a tie!")
        
    print()
    print(playerName,playerScore,"x",computerScore,"Computer")    
    print()
    
    
    
    
    #end of loop
    roundNumber=roundNumber+1
    #end of loop
    
    
    
    


