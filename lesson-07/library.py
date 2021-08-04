import random


def get_card_sum(used_cards):
    card_values = {
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "10": 10,
        "J": 2,
        "D": 3,
        "K": 4,
        "A": 11
    }
    card_sum = 0
    for card in used_cards:
        key = card.split("-")[-1]
        card_sum += card_values[key]


def get_card(used_cards):
    card_suit_list = ["H", "D", "C", "S"]
    card_list = ["6", "7", "8", "9", "10", "J", "D", "K", "A"]
    while True:
        index = random.randint(0, len(card_suit_list) - 1)
        card_suit = card_suit_list[index]

        index = random.randint(0, len(card_list) - 1)
        card = card_list[index]

        current = f"{card_suit} - {card}"
        if current not in used_cards:
            return current