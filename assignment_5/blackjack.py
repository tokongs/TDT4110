import random
cards = ['E', 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
dealer_hand = []
player_hand = []


def findHandValue(hand):
    result = 0
    for card in hand:
        result += card
    
    return result

def dealCard(hand):
    card = cards[random.randint(0, 12)]
    if(card == 'E'):
        hand_value = findHandValue(hand)
        if(hand_value + 11 > 21):
            hand.insert(0, 1)
        else:
            hand.insert(0, 11)
    else:
        hand.insert(0, card)

    return hand


win = 1
cont = 0
loss = -1

def checkWinCondition(player, dealer):
    player_value = findHandValue(player)
    dealer_value = findHandValue(dealer)
    if player_value == 21 and 21 > dealer_value:
        return win

    return cont
def checkLossCondition(player, dealer):
    player_value = findHandValue(player)
    dealer_value = findHandValue(dealer)
    if(dealer_value == 21):
        return loss
    if player_value > 21:
        return loss

    return cont
    
    

dealer_hand = dealCard(dealer_hand)
dealer_hand = dealCard(dealer_hand)

player_hand = dealCard(player_hand)
player_and = dealCard(player_hand)

print("Dealers cards are", dealer_hand[0], "and ?")
print("Your score is:", player_hand[0]+player_hand[1])
while checkLossCondition(player_hand, dealer_hand) == cont:
    if(checkWinCondition(player_hand, dealer_hand) == win):
        break
    new_card = input("Do you want another card? (J/N) ").lower()
    if new_card == "j":
        player_hand = dealCard(player_hand)
        print("Your score is:", findHandValue(player_hand))
    else:
        break

print("Dealers score is:", findHandValue(dealer_hand))
print("Your score is:", findHandValue(player_hand))

if checkLossCondition(player_hand, dealer_hand) != loss:
    print("You won!")
else:
    print("Your lost")