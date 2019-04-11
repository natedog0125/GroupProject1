import random

#generates players first 2 cards
def playersCards(playerCounter, randList):
    #generates a random card
    randomCard = random.choice(randList)
    
    #if card is an Ace, give the user the option between 1 and 11
    if randomCard == 1:
        ace = int(input('Would you like your ace to be 1 or 11? '))
        playerCounter = playerCounter + ace
    #if the card is not an ace add the card to your hand
    else:
        playerCounter = playerCounter + randomCard
        
    #generates a random card
    randomCard2 = random.choice(randList)
    
    #if card is an Ace, give the user the option between 1 and 11
    if randomCard2 == 1:
        ace = int(input('Would you like your ace to be 1 or 11? '))
        playerCounter = playerCounter + ace
    #if the card is not an ace add the card to your hand
    else:
        playerCounter = playerCounter + randomCard2
        
    #return the players hand    
    return playerCounter
    
def dealersCards(dealerCounter, randList):
    #generates a random card
    randomCard = random.choice(randList)
    
    #if the card is an Ace
    if randomCard == 1:
        #if the dealer's hand is less than 10, add 11 
        if dealerCounter < 10:
            dealerCounter = dealerCounter + 11
        #if the dealer's hand is greater than 10, add 1
        else:
            dealerCounter = dealerCounter + 1
    #if the card is not an ace add the card to the dealer's hand    
    else:
        dealerCounter = dealerCounter + randomCard        
        #generates a random card
        
    randomCard2 = random.choice(randList)
    
    #if the card is an Ace
    if randomCard2 == 1:
        #if the dealer's hand is less than 10, add 11 
        if dealerCounter < 10:
            dealerCounter = dealerCounter + 11
        #if the dealer's hand is greater than 10, add 1
        else:
            dealerCounter = dealerCounter + 1
    #if the card is not an ace add the card to the dealer's hand    
    else:
        dealerCounter = dealerCounter + randomCard2 
        
    #return the dealer's hand
    return dealerCounter

def addCard(playerCounter, randList):
    #ask the user if he wants another card
    hit = str(input('Hit? (Y/n): ')).upper()
    #while the user does want to hit or his hand is not greater than 21
    while hit == 'Y':
        #check to make sure playerCounter is still less than 21
        if playerCounter < 21:
            #generate a new card
            randomCard = random.choice(randList)
            #if card is an Ace, give the user the option between 1 and 11
            if randomCard == 1:
                ace = int(input('Would you like your ace to be 1 or 11? '))
                playerCounter = playerCounter + ace
                print('You now have:', playerCounter)
            #if the card is not an ace add the card to your hand
            else:
                playerCounter = playerCounter + randomCard
                print('You now have:', playerCounter)
            #check to make sure playerCounter is still less than 21    
            if playerCounter < 21:
                #ask the user if he wants another card
                hit = str(input('Hit? (Y/n): ')).upper() 
            else:
                #if playerCounter is > than 21 then do not allow user to hit
                hit = 'N'
        else:
            #if playerCounter is > than 21 then do not allow user to hit
            hit = 'N'
            
    #return the player's hand    
    return playerCounter
    
def dealerDraws(dealerCounter, randList):
    while dealerCounter < 17:
        #generate a random card
        randomCard = random.choice(randList)
        #if card is an Ace
        if randomCard == 1:
            #if the dealer's hand is less than 10, add 11 
            if dealerCounter <= 10:
                dealerCounter = dealerCounter + 11
            #if the dealer's hand is greater than 10, add 1
            else:
                dealerCounter = dealerCounter + 1
        #if the card is not an ace add the card to the dealer's hand    
        else:
            dealerCounter = dealerCounter + randomCard        
    
    print('Dealer now has:', dealerCounter)
    #return the dealer's hand
    return dealerCounter
    
def winner(dealerCounter, playerCounter, pot, bet):
    #determine which player has the higher score
    if playerCounter <= 21 and dealerCounter <= 21:
        if playerCounter > dealerCounter:
            #if player wins add to his bet to the pot
            pot = pot + bet
            print('You won', bet, 'you now have,', pot)
        elif playerCounter == dealerCounter:
            pot = pot
        else:
            #if player loses take away his bet from the pot
            pot = pot - bet
            print('You lost', bet, 'you now have,', pot)
        
    #return his new pot amount
    return pot
    
def playerBust(playerCounter, pot, bet):
    
    #determine if player's hand has gone over 21
    if playerCounter >= 22:
        #if player busts, take his bet
        pot = pot - bet
        print('You lost', bet, 'you now have,', pot)
    else:
        pot = pot
        
    #return player's new pot amount
    return pot    
    
def dealerBust(dealerCounter, pot, bet):
    
    #determine if dealer's hand has gone over 21
    if dealerCounter >= 22:
        #if dealer busts, give bet to player
        pot = pot + bet
        print('You won', bet, ' you now have,', pot)
    else:
        pot = pot
    
    #return player's new pot amount    
    return pot    
    
def main():
    
    #random list of cards
    randList = [10, 10, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    #do you want to play?
    play = str(input('Would you like to play Blackjack? (Y/n): ')).upper()
    #how much money are you wanting to play with?
    pot = float(input('How much money is in your pot? '))
    
    while play == 'Y':
        
        #player's hand
        playerCounter = 0
        #dealer's hand
        dealerCounter = 0
        
        #how much do you want to bet
        bet = float(input('Place your bet: '))
    
        #give player his starting cards
        playerCounter = playersCards(playerCounter, randList)
        #give dealer his starting cards
        dealerCounter = dealersCards(dealerCounter, randList)
        print('Your first 2 cards add up to: ', playerCounter)
        print("The dealer's first 2 cards add up to: ", dealerCounter)
        
        #if dealer scores 21 immediately, he wins
        if dealerCounter == 21:
            pot = winner(dealerCounter, playerCounter, pot, bet)
            print("Player's score is", playerCounter, "\nDealer's score is", dealerCounter)
            
        else:
            #use the function to see if player wants more cards
            playerCounter = addCard(playerCounter, randList)
            #have the dealer draw his cards
            dealerCounter = dealerDraws(dealerCounter, randList)
            if playerCounter >=22:
                #see if player has busted
                pot = playerBust(playerCounter, pot, bet)
                print("You busted with", playerCounter)
            elif dealerCounter >=22:
                #use the function to have dealer draw cards until he has at least 17
                #check to see if dealer busted
                pot = dealerBust(dealerCounter, pot, bet)
                print("Dealer busted with", dealerCounter)
            elif playerCounter <= 21 and dealerCounter <= 21:
                #check for a winner
                pot = winner(dealerCounter, playerCounter, pot, bet)
                print("Player's score is", playerCounter, "\nDealer's score is", dealerCounter)
            else:
                print('Something went wrong')
                
        #do you want to play again?
        play = str(input('Would you like to play again? (Y/n): ')).upper()
        if play == 'N':
            print('You have left the table with: ', pot)
    
main()

#if 1st dealerCounter = 21 run winner