

def calculate_hand_values():
    with open("input.txt") as input:
        input_lines = input.readlines()

        for line in input_lines:
            normalized_hand: list[str] = list(line.strip('\n').split()[0])
            score = score_hand(normalized_hand)
            print(str(score) + " >>"  + str(normalized_hand))

def score_hand(hand: list[str]):
    #7 Five of a Kind
    #6 Four of a Kind
    #5 Full House of a Kind, 3 pair and 2 pair
    #4 Three of a kind
    #3 Two pairs
    #2 pair
    #1 all different

    unique_cards = {}
    for card in hand:
        if card in unique_cards:
            unique_cards[card] += 1
        else:
            unique_cards[card] = 1

    if len(unique_cards) == 2:
        for card in unique_cards:
            if unique_cards[card] == 4:
                return 6
            if unique_cards[card] == 3:
                return 5

    if len(unique_cards) == 3:
        is_one_pair = False
        for card in unique_cards:
            if unique_cards[card] == 2:
                if is_one_pair:
                    return 3
                is_one_pair = True
        if is_one_pair:
            return 2

    if len(unique_cards) == 4:
        return 2

    if len(unique_cards) == 1:
        return 7
    if len(unique_cards) == 5:
        return 1

calculate_hand_values()
