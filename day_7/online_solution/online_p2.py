from typing import List
from collections import Counter

from online_p1 import Hand, compare_hands, solve as solve_pt1


def compare_hand_points(hand_1: Hand, hand_2: Hand):
    def replace_js(hand: Hand) -> str:
        if hand.cards == 'JJJJJ':
            return hand.cards
        card_to_replace = list(
            map(
                lambda occurrences: occurrences[0],
                filter(
                    lambda occurrences: occurrences[0] != "J",
                    Counter(hand.cards).most_common(),
                ),
            )
        )[0]
        new_hand = hand.cards.replace("J", card_to_replace)
        # print(f"Old Hand: {hand}  | New Hand {new_hand}")
        return new_hand

    c_1 = Counter(replace_js(hand_1))
    c_2 = Counter(replace_js(hand_2))
    mc_1 = c_1.most_common()
    mc_2 = c_2.most_common()
    for i in range(min(len(mc_1), len(mc_2))):
        if mc_1[i][1] > mc_2[i][1]:
            return 1
        if mc_1[i][1] < mc_2[i][1]:
            return -1
    return 0


def compare_hands_pt2(hand_1: Hand, hand_2: Hand) -> int:
    return compare_hands(
        hand_1,
        hand_2,
        card_points_comparator=compare_hand_points,
        card_priorities="AKQT98765432J",
    )


def solve(input_lines: List[str]) -> int:
    return solve_pt1(input_lines, hands_comparator=compare_hands_pt2)


if __name__ == "__main__":
    with open("../input.txt", "r") as reader:
        solution = solve(reader.readlines())
        print(f"result: {solution}")