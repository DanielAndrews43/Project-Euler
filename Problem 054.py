file = open('p054_poker.txt', 'r')
hands = file.read().split('\n')

convert = {'T':10, 'J':11, 'Q':12, 'K':13, 'A':14}

#returns (type, val1, val2, high)
#type: 0=High Card, 1=Pair, 2=Two Pair, 3=Three of kind, 4=Straight, 5=Flush
#      6=Full House, 7=Four of a kind, 8=Straight Flush, 9=Royal Flush
#val1: highest card in the type (e.g value of single pair, which is triple in full house, wehre straight ends)
#val2: second highest card in type (e.g. pair in full house, 0 for single pair, lower value of two pair)
#high: high card if not all cards are used (e.g 9 in hand 33229)
def rank(hand):
    #sort hand

    #if each value = 1+value of prev and ace is not at end
        #straight

    #check count of each card
        #if count = 2
            #pair
        #if count = 3
            #triple
        #if count = 4
            #four of a kind
    #if two counts = 2
        #two pair
    #if one count = 2 and another count = 3
        #full house

    #high card is largest value not used for pair or two pair or four of a kind

    #suit = first card suit
    #flag = true
    #for each card in hand
        #if suit is not same as first
            #flag = false
    #if flag
        #if type < 4
            #type = 5
        #if type = 4
            #type = 8
            #if high card is 13
                #type = 9


for hand in hands:
    cards = hand.split(' ')
    for c,i in cards:
        num = c[0]
        if convert.get(c[0],0):
            num = convert.get(c[0])
        cards[i] = (int(num), c[1])

    #hands are list of (value, suit) pairs
    hand1 = cards[0:5]
    hand2 = cards[5:]

    a = rank(hand1)
    b = rank(hand2)

    if a[0] > b[0]:

    elif a[1] > b[1]:

    elif a[2] > b[2]:

    elif a[3] > b[3]:

    