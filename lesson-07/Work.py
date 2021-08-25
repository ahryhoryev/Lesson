from library import get_card, get_card_sum


used_cards = []
while True:
    choice = input("Get new card[y/n]: ")
    if choice == "y":
        current = get_card(used_cards)
        used_cards.append(current)
        print(used_cards)

        card_sum = get_card_sum(used_cards)
        if card_sum > 21:
            print("Game Over")
            break
        if card_sum == 21:
            print("You win")
            break
        else:
            card_sum = get_card_sum(used_cards)
            print("Your current rate: ")
            break
