
def point_from_card (card_value):
    '''
    Converts a one-letter card name to a numeric value.
    :param card_value: String to convert to a card value.
    :return:
    '''
    face_cards = ('J', 'Q', 'K')
    if (card_value in face_cards):
        return 10
    return 0 if (card_value == 'A') else int(card_value)

def ace_total(current_total, count_aces):
    '''
    Flexes the recommendation for hitting around the possibility that aces are worth either 1 or 11 points.
     Returns 19 or 20 if possible with a value of 11 for an ace, otherwise returning 1.
    :param current_total: Current numeric total (excluding aces)
    :param count_aces: Number of aces drawn.
    :return:
    '''
    if ( 18 < (current_total + count_aces + 10) < 22):
        return current_total + count_aces + 10
    else:
        return current_total + count_aces

def decision(current_total):
    '''
    Returns a decision string on whether the user should hit or stay.
    :param current_total: Current card total.
    :return:
    '''
    if current_total < 17:
        return "Hit"
    elif current_total < 21:
        return "Stay"
    elif current_total == 21:
        return "Blackjack!"
    else:
        return "Already Busted"

#Main program start: input three cards.
card_one = int(point_from_card( input("Please enter a card: ")))
card_two = int(point_from_card( input("Please enter a second card: ")))
card_three = int(point_from_card( input("Please enter a third card: ")))
#Sum the value of the cards.
basic_sum = card_one + card_two + card_three
#If there are aces, count them.
count_aces = 0
if card_one == 0:
    count_aces = count_aces + 1
if card_two == 0:
    count_aces = count_aces + 1
if card_three == 0:
    count_aces = count_aces + 1

#If the count of aces is greater than zero, decide whether to make them all worth 1 or make one of them worth 11
if (count_aces > 0):
    basic_sum = ace_total(basic_sum, count_aces)

#Call the decision function based upon value of hand.
hit_me = decision(basic_sum)

#Print decision recommendation.
print ("Current Value: " + str(basic_sum) + " Action Recommendation: " + hit_me)
