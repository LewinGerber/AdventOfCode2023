from typing import List, Generator
from collections import namedtuple, Counter
from functools import cmp_to_key

Hand = namedtuple("Hand", "cards bid")


def parse_input(input_lines: List[str] | Generator) -> List[Hand]:
    hands = []
    for line in input_lines:
        vals = line.strip().split()
        hand = vals[0].strip()
        hands.append(Hand(hand, int(vals[1].strip())))
    return hands


ALPHABET = "AKQJT98765432"


def compare_hand_points(hand_1: Hand, hand_2: Hand):
    c_1 = Counter(hand_1.cards)
    c_2 = Counter(hand_2.cards)
    mc_1 = c_1.most_common()
    mc_2 = c_2.most_common()

    #    print("-"*10)
    #    print(f"Comparing Cards: {hand_1.cards} vs {hand_2.cards}")
    for i in range(min(len(mc_1), len(mc_2))):
        # print(f"Comparing:  {mc_1[i]} vs {mc_2[i]}")
        if mc_1[i][1] > mc_2[i][1]:
            # print("Hand 2 wins")
            return 1
        if mc_1[i][1] < mc_2[i][1]:
            # print("Hand 1 wins")
            return -1
    return 0


def compare_hands(
    hand_1: Hand,
    hand_2: Hand,
    card_points_comparator=compare_hand_points,
    card_priorities=ALPHABET,
) -> int:

    card_points = card_points_comparator(hand_1, hand_2)
    if card_points != 0:
        return card_points

    # print("Same points. Comparing the first different highest card")
    for i in range(len(hand_1.cards)):
        # print(f"Comparing:  {hand_1.cards[i]} vs {hand_2.cards[i]}")
        if card_priorities.index(hand_1.cards[i]) > card_priorities.index(
            hand_2.cards[i]
        ):
            # print("Hand 1 wins")
            return -1
        if card_priorities.index(hand_1.cards[i]) < card_priorities.index(
            hand_2.cards[i]
        ):
            # print("Hand 2 wins")
            return 1
    return 0


def rank_hands(input_hands: List[Hand], hands_comparator=compare_hands) -> List[Hand]:
    return sorted(input_hands, key=cmp_to_key(hands_comparator))


def solve(input_lines: List[str], hands_comparator=compare_hands) -> int:
    hands = parse_input(input_lines)
    ranked_hands = rank_hands(hands, hands_comparator=hands_comparator)
    return sum([(i + 1) * hand.bid for i, hand in enumerate(ranked_hands)])


if __name__ == "__main__":
    with open("../input.txt", "r") as reader:
        solution = solve(reader.readlines())
        print(f"result: {solution}")