import random

#generates players first 2 cards
def playersCard1(playerCounter, randList):
    #generates a random card
    randomCard = random.choice(randList)
    
    #if card is an Ace, give the user the option between 1 and 11
    if randomCard == 1:
        ace = int(input('Would you like your ace to be 1 or 11? '))
        playerCounter = playerCounter + ace
    #if the card is not an ace add the card to your hand
    else:
        playerCounter = playerCounter + randomCard
        
    return playerCounter

def playersCard2(playerCounter, randList):
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
    
def dealersCard1(dealerCounter, randList):
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
        
    return dealerCounter

def dealerCard2(dealerCounter, randList):

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
    
def split(card1, card2, randList, splitBet, bet):
    #if both of player's cards are the same, ask if he wants to split
    if card1 == card2:
        #create a bet for the split deck
        splitBet = bet
        #store hands and bets here
        cardList = []
        #append players first original card
        cardList.append(card1)
        #generates a random card
        randomCard1 = random.choice(randList)
        #if card is an Ace, give the user the option between 1 and 11
        if randomCard1 == 1:
            ace = int(input("Would you like your first hand's ace to be 1 or 11? "))
            #append players new first hand card to deck
            cardList.append(ace)
        #if the card is not an ace add the card to your hand
        else:
            #append players new first hand card to deck
            cardList.append(randomCard1)
        #store player's second original card    
        cardList.append(card2)
        #generates a random card
        randomCard2 = random.choice(randList)
        #if card is an Ace, give the user the option between 1 and 11
        if randomCard2 == 1:
            ace = int(input("Would you like your second hand's ace to be 1 or 11? "))
            #append players new second hand card to deck
            cardList.append(ace)
        #if the card is not an ace add the card to your hand
        else:
            #append players new second hand card to deck
            cardList.append(randomCard2)     
        #store the bet    
        cardList.append(splitBet)
        
        #return our list of information
        return cardList
    
def insurance(dealerCard, dealerCard2, bet, pot):
    #total up dealers cards
    dealersCards = dealerCard + dealerCard2
    #ask user if they would like to insure their hand
    insurances = input('The dealer has an Ace, would you like to insure your hand? (Y/n): ').upper()
    #if player does want insurance
    if insurances == 'Y':
        #player gives dealer half of bet
        pot -= bet/2
        #if dealer does have 21
        if dealersCards == 21:
            #player gets bet back
            pot += bet
        else:
            #if dealer does not have 21, the player continues to play with the bet he put down
            pot = pot
    #if player does not get insurance, no money is taken and they play with their original bet
    else:
        pot = pot
        
    return pot

def addCard(playerCounter, randList):
    #ask the user if he wants another card
    hitCounter = 0
    hit = str(input('Hit? *If you split, this is your first hand* (Y/n) : ')).upper()
    #while the user does want to hit or his hand is not greater than 21
    while hit == 'Y':
        #keep count of how many cards are drawn
        hitCounter += 1
        #if player has 5 cards
        if hitCounter == 3:
            #player wins
            playerCounter = 21
            print('Congratulations! You got a Five Card Charlie! You automatically win.')
        else:
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
    
def addSplitCard(splitCounter, randList):
    #ask the user if he wants another card
    hitCounter = 0
    hit = str(input('Hit? *If you split, this is your second hand* (Y/n): ')).upper()
    #while the user does want to hit or his hand is not greater than 21
    while hit == 'Y':
        #keep count of how many cards are drawn
        hitCounter += 1
        #if player has 5 cards
        if hitCounter == 3:
            #player wins
            splitCounter = 21
            print('Congratulations! You got a Five Card Charlie! You automatically win.')
        else:
            #check to make sure playerCounter is still less than 21
            if splitCounter < 21:
                #generate a new card
                randomCard = random.choice(randList)
                #if card is an Ace, give the user the option between 1 and 11
                if randomCard == 1:
                    ace = int(input('Would you like your ace to be 1 or 11? '))
                    splitCounter = splitCounter + ace
                    print('You now have:', splitCounter)
                #if the card is not an ace add the card to your hand
                else:
                    splitCounter = splitCounter + randomCard
                    print('You now have:', splitCounter)
                #check to make sure playerCounter is still less than 21    
                if splitCounter < 21:
                    #ask the user if he wants another card
                    hit = str(input('Hit? (Y/n): ')).upper() 
                else:
                    #if playerCounter is > than 21 then do not allow user to hit
                    hit = 'N'
            else:
                #if playerCounter is > than 21 then do not allow user to hit
                hit = 'N'
                
    #return the player's hand    
    return splitCounter
    
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
            print("Dealer and Player's hands are tied. Your pot is still,", pot)
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
        print('You won', bet, 'you now have,', pot)
    else:
        pot = pot
    
    #return player's new pot amount    
    return pot    
    
def main():
    
    #random list of cards
    randDict = {'Ace': 1, 'King': 10, 'Queen': 10, 'Jack': 10, '10': 10, '9': 9, '8': 8, '7': 7, '6': 6, '5': 5, '4': 4, '3': 3, '2': 2}
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
        #split counter
        splitCounter = 0
        
        splitBet = 0
        
        #how much do you want to bet
        bet = float(input('Place your bet: '))
    
        #give player his starting cards
        playerCard1 = playersCard1(playerCounter, randList)
        playerCard2 = playersCard2(playerCounter, randList)
        
        playerCounter = playerCard1 + playerCard2
        
        #give dealer his first card
        firstDealerCard = dealersCard1(dealerCounter, randList)
        print('Your first 2 cards are', playerCard1, 'and', playerCard2, 'which adds to', playerCounter)
        print("The dealer's top card is: ", firstDealerCard)
        
        #give dealer his second card
        secondDealerCard = dealerCard2(dealerCounter, randList)
        
        #add up dealer's cards 
        dealerCounter = firstDealerCard + secondDealerCard
        
        #if player's first two cards are the same see if he wants to split
        if playerCard1 == playerCard2:
            splitting = input('Would you like to split? (Y/n): ').upper()
            if splitting == 'Y':
                # if he does split, get our list of new hand amounts and the new bet
                cardList = split(playerCard1, playerCard2, randList, splitBet, bet)
                #new first hand
                playerCounter = cardList[0] + cardList[1]
                print('You have', playerCounter, 'in your first hand')
                #new second hand
                splitCounter = cardList[2] +cardList[3]
                #bet for second hand
                splitBet = cardList[4]
                
                #if dealer has an 11, ask if player wants insurance
                if firstDealerCard == 11:
                    pot = insurance(firstDealerCard, secondDealerCard, bet, pot)
                    print('Dealer has 21, so your pot returns to', pot)
                    
                else:
                    #if dealer scores 21 immediately, he wins
                    if dealerCounter == 21:
                        pot = winner(dealerCounter, playerCounter, pot, bet)
                        print("Player's score is", playerCounter, "\nDealer's score is", dealerCounter)
                    #if player scores 21 immediately, he wins
                    elif playerCounter == 21:
                        pot = winner(dealerCounter, playerCounter, pot, bet)
                        print("Player's score is", playerCounter, "\nDealer's score is", dealerCounter)
                    #else continue with the game    
                    else:
                        #use the function to see if player wants more cards
                        playerCounter = addCard(playerCounter, randList)
                        
                        #if our second hand has cards
                        if splitCounter > 1:
                            print('You have', splitCounter, 'in your second hand')
                            #ask if player wants to add cards to that hand
                            splitCounter = addSplitCard(splitCounter, randList)
                            #dealer draws his hand
                            dealerCounter = dealerDraws(dealerCounter, randList)
                        else:
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
                            
                        if splitCounter >=22:
                            #see if player has busted
                            pot = playerBust(splitCounter, pot, splitBet)
                            print("You busted with", splitCounter)
                        elif dealerCounter >=22:
                            #use the function to have dealer draw cards until he has at least 17
                            #check to see if dealer busted
                            pot = dealerBust(dealerCounter, pot, splitBet)
                            print("Dealer busted with", dealerCounter)
                        elif splitCounter <= 21 and dealerCounter <= 21:
                            #check for a winner
                            pot = winner(dealerCounter, splitCounter, pot, splitBet)
                            print("Player's score is", splitCounter, "\nDealer's score is", dealerCounter)
                        else:
                            print('Something went wrong')
                            
        else:
            #no splitting is involved
            #ask player if he wants insurance
            if firstDealerCard == 11:
                pot = insurance(firstDealerCard, secondDealerCard, bet, pot)
                print('Dealer has 21, so your pot returns to', pot)
                
            else:
                #if dealer scores 21 immediately, he wins
                if dealerCounter == 21:
                    pot = winner(dealerCounter, playerCounter, pot, bet)
                    print("Player's score is", playerCounter, "\nDealer's score is", dealerCounter)
                #if player scores 21 immediately, he wins
                elif playerCounter == 21:
                    pot = winner(dealerCounter, playerCounter, pot, bet)
                    print("Player's score is", playerCounter, "\nDealer's score is", dealerCounter)
                #else continue with the game    
                else:
                    #use the function to see if player wants more cards
                    playerCounter = addCard(playerCounter, randList)
                    
                    if splitCounter > 1:
                        print('You have', splitCounter, 'in your second hand')
                        splitCounter = addSplitCard(splitCounter, randList)
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