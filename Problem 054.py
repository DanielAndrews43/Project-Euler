file = open('p054_poker.txt', 'r')
hands = file.read().split('\n')

convert = {'T':10, 'J':11, 'Q':12, 'K':13, 'A':14}

# returns (type, val1, val2, high)
# type: 0=High Card, 1=Pair, 2=Two Pair, 3=Three of kind, 4=Straight, 5=Flush
#      6=Full House, 7=Four of a kind, 8=Straight Flush, 9=Royal Flush
# val1: highest card in the type (e.g value of single pair, triple in full house, end of straight)
# val2: second highest card in type (e.g. pair in full house, 0 for single pair, lower value of two pair)
# high: high card if not all cards are used (e.g 9 in hand 33229)
def is_straight(vals):
    return all(x+1 == y for x, y in zip(vals, vals[1:]))

def is_flush(suits):
    return len(set(suits)) == 1

def get_card_counts(vals):
    counts = {}
    for val in vals:
        counts[val] = counts.get(val, 0) + 1
    return counts

def rank(vals, suits):
    vals.sort()

    card_counts = get_card_counts(vals)

    card_1 = 0
    card_2 = 0
    quad = False
    triple = False
    num_doubles = 0
    singles = []
    for value, count in card_counts.items():
        if count == 4:
            quad = True
            card_1 = value
        elif count == 3:
            triple = True
            if card_1:
                card_2 = card_1
            card_1 = value
        elif count == 2:
            num_doubles += 1
            if not card_1:
                card_1 = value
            else:
                card_2 = value
            if num_doubles == 2:
                card_1, card_2 = max(card_1, card_2), min(card_1, card_2)
        else:
            singles.append(value)

    singles.sort()
    singles = singles[::-1]
    highest_card = 0
    if singles:
        highest_card = singles[0]

    straight = is_straight(vals)
    flush = is_flush(suits)

    if straight and flush:
        return (8,highest_card,0,0)

    if quad:
        return (7, card_1, 0, singles)

    if triple and num_doubles == 1:
        return (6, card_1, card_2, singles)

    if flush:
        return (5, 0, 0, singles)

    if straight:
        return (4, 0, 0, singles)

    if triple:
        return (3, card_1, 0, singles)

    if num_doubles == 2:
        return (2, card_1, card_2, singles)

    if num_doubles == 1:
        return (1, card_1, 0, singles)

    return (0, 0, 0, singles)

win_count = 0
for hand in hands:
    cards = hand.split(' ')

    values = []
    suits = []
    for i, card in enumerate(cards):
        value,suit = list(card)

        values.append(int(convert.get(value, value)))
        suits.append(suit)

    a = rank(values[:5], suits[:5])
    b = rank(values[5:], suits[5:])

    # Check rank of hand
    if a[0] > b[0]:
        win_count += 1
        continue
    elif a[0] < b[0]:
        continue

    # Check rank of card_1
    if a[1] > b[1]:
        win_count += 1
        continue
    elif a[1] < b[1]:
        continue

    # Check rank of card_2
    if a[2] > b[2]:
        win_count += 1
        continue
    elif a[2] < b[2]:
        continue

    # Check singles
    a_singles = a[3]
    b_singles = b[3]

    for i in range(len(a_singles)):
        if a_singles[i] > b_singles[i]:
            win_count += 1
            break
        if b_singles[i] > a_singles[i]:
            break

print(win_count)