
def cardsGame(card_amount, cards):
    '''
    Function that returns the total of Sereja and Dima
    '''
    sereja = 0
    dima = 0
    i = 0
    j = card_amount - 1
    turn = 0
    result = []
    while i <= j and turn <= card_amount:
        if turn % 2 == 0:
            if cards[i] < cards[j]:
                sereja += cards[j]
                j -= 1
                turn += 1
            else:
                sereja += cards[i]
                i += 1
                turn += 1
        else:
            if cards[i] < cards[j]:
                dima += cards[j]
                j -= 1
                turn += 1
            else:
                dima += cards[i]
                i += 1
                turn += 1
    return sereja, dima


def main():
    '''
    Main function
    '''
    # number of cards
    card_amount = int(input())     
    # enter the array 
    cards = list(map(int, 
input().strip().split()))[:card_amount]
    # result
    sereja, dima = cardsGame(card_amount, cards)
    print(f'{sereja} {dima}')

main()
	    	  	  		 					 	    		 	 	