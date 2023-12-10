import functools

class ScoredHand:
    def __init__(self, score, hand, multiplier, sortable_hand_name):
        self.score = score
        self.hand = hand
        self.multiplier = multiplier
        self.sortable_hand_name = sortable_hand_name

def sorter(obj1: ScoredHand, obj2: ScoredHand) -> int:
    # Compare scores
    if obj1.score < obj2.score:
        return -1
    elif obj1.score > obj2.score:
        return 1

    if obj1.sortable_hand_name < obj2.sortable_hand_name:
        return 1
    elif obj1.sortable_hand_name > obj2.sortable_hand_name:
        return -1

    return 0

def calculate_hand_values():
    with open("input.txt") as input:
        input_lines = input.readlines()

        scored_hands = []
        for line in input_lines:
            hand = line.strip('\n').split()[0]
            multiplier = line.strip('\n').split()[1]
            normalized_hand: list[str] = list(hand)
            score = score_hand(normalized_hand)
            sortable_hand_name = hand.replace("K", "B")
            sortable_hand_name = sortable_hand_name.replace("Q", "C")
            sortable_hand_name = sortable_hand_name.replace("T", "D")
            sortable_hand_name = sortable_hand_name.replace("9", "E")
            sortable_hand_name = sortable_hand_name.replace("8", "F")
            sortable_hand_name = sortable_hand_name.replace("7", "G")
            sortable_hand_name = sortable_hand_name.replace("6", "H")
            sortable_hand_name = sortable_hand_name.replace("5", "I")
            sortable_hand_name = sortable_hand_name.replace("4", "J")
            sortable_hand_name = sortable_hand_name.replace("3", "K")
            sortable_hand_name = sortable_hand_name.replace("2", "L")
            sortable_hand_name = sortable_hand_name.replace("J", "M")
            scored_hands.append(ScoredHand(score, hand, multiplier, sortable_hand_name))

        ranked_hands = sorted(scored_hands, key=lambda scoreHand: (-scoreHand.score, scoreHand.sortable_hand_name), reverse=True)

        for obj in ranked_hands:
            print(f"Score: {obj.score}, Hand Name: {obj.sortable_hand_name}, ")

        total_winnings = 0
        for index in range(len(ranked_hands)):
            #print(ranked_hands[index]['hand'] + " " + str(ranked_hands[index]['score']) + " " + str(index + 1) + " " + str(ranked_hands[index]['multiplier']))
            total_winnings += (index + 1) * int(ranked_hands[index].multiplier)
            #print(str(index+1) + " * " + str(ranked_hands[index]['multiplier']) + " = " + str(total_winnings))
        print(total_winnings)

def score_hand(hand: list[str]):
    # 7 Five of a Kind
    # 6 Four of a Kind
    # 5 Full House of a Kind, 3 pair and 2 pair
    # 4 Three of a kind
    # 3 Two pairs
    # 2 pair
    # 1 all different

    unique_cards = {}
    for card in hand:
        if card in unique_cards:
            unique_cards[card] += 1
        else:
            unique_cards[card] = 1

    if "J" in unique_cards:
        number_of_j = unique_cards["J"]
        unique_cards.pop("J")
        if number_of_j == 5:
            return 6
        if unique_cards is {}:
            return

        key = max(unique_cards, key=unique_cards.get)
        unique_cards[key] += number_of_j

    if len(unique_cards) == 2:
        for card in unique_cards:
            if unique_cards[card] == 4:
                return 6
            if unique_cards[card] == 3:
                return 5

    #print(unique_cards)

    if len(unique_cards) == 3:
        for card in unique_cards:
            if unique_cards[card] == 3:
                return 4

    if len(unique_cards) == 3:
        is_one_pair = False
        for card in unique_cards:
            if unique_cards[card] >= 2:
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
