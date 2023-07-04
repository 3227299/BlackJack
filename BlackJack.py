#BlackJack.python
#G. Li
#7/3/23
#Black Jack Card Game

import random

playerIn= True
dealerIn = True

#total cards in the deck
deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10,
        2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10,
        'K', 'Q', 'J', 'A', 'K', 'Q', 'J', 'A', 'K', 'Q', 'J', 'A'
        'K', 'Q', 'J', 'A']
#player's and delear's hand
playerHand = []
dealerHand = []

#dealing cards
def dealCards(turn):
  card = random.choice(deck)
  turn.append(card)
  deck.remove(card)

#calcaute the total of cards
def totalCards(turn):
    total = 0 
    face = ['K', 'Q', 'J', 'A']
    for card in turn:
        if card in range(1,11):
            total += card
        elif card in face: 
            total += 1
        else:
            if total > 11:
                total += 1
            else:
              total += 11

    return total

#test if it the winner
def revealDealersHand():
    if len(dealerHand) == 2:
        return dealerHand[0]
    elif len(dealerHand) > 2:
        return dealerHand[0], dealerHand[1]

#game loop
for _ in range(2):
    dealCards(dealerHand)
    dealCards(playerHand)

#revealing the hands of the dealer and player
while playerIn or dealerIn:
  print(f"Dealer hand have {revealDealersHand()} and X\n")
  print(f"You have {playerHand} which totals equal {totalCards(playerHand)}\n")
  if playerIn:
    stayOrHit = input("1: Stay\n2:Hit\n")
  if totalCards(dealerHand) > 16:
      dealerIn = False
  else:
      dealCards(dealerHand)
  if stayOrHit == '1':
      playerIn = False
  else:
      dealCards(playerHand)
  if totalCards(playerHand) >= 21:
      break
  elif totalCards(dealerHand) >= 21:
      break

#showing the result of the winning hands
if totalCards(playerHand) == 21:
    print(f"\nYou have {playerHand} for the grand total of {totalCards(playerHand)}
          and the dealer has {dealerHand} and for the grand total of {totalCards(dealerHand)}")
    print("\nBlackJack!!!!!!!!")
elif totalCards(dealerHand) == 21:
    print(f"\nYou have {playerHand} for the grand total of {totalCards(playerHand)}
          and the dealer has {dealerHand} and for the grand total of {totalCards(dealerHand)}")
    print("\nDealer Win Sadly!")
elif totalCards(playerHand) > 21:
    print(f"\nYou have {playerHand} for the grand total of {totalCards(playerHand)}
          and the dealer has {dealerHand} and for the grand total of {totalCards(dealerHand)}")
    print("Bust!")
elif totalCards(dealerHand) > 21:
    print(f"\nYou have {playerHand} for the grand total of {totalCards(playerHand)}
          and the dealer has {dealerHand} and for the grand total of {totalCards(dealerHand)}")
    print("Dealer Bust!")
elif 21 - totalCards(dealerHand) < 21 - totalCards(playerHand):
    print(f"\nYou have {playerHand} for the grand total of {totalCards(playerHand)}
          and the dealer has {dealerHand} and for the grand total of {totalCards(dealerHand)}")
    print("Dealer Wins!!")
elif 21 - totalCards(dealerHand) > 21 - totalCards(playerHand):
    print(f"\nYou have {playerHand} for the grand total of {totalCards(playerHand)}
          and the dealer has {dealerHand} and for the grand total of {totalCards(dealerHand)}")
    print("Win!!")