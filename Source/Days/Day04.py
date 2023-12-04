
def handle_part2_cards(cards):
    cards_won = len(cards)
    processed_cards = cards
    while len(processed_cards) != 0:
        new_cards = []
        for card in processed_cards:
            card_no, winning_cards, our_cards, winnings = card
            for i in range(winnings):
                new_cards.append(cards[card_no+i])
                cards_won += 1
        processed_cards = new_cards
    return cards_won

def execute_day(part):
    if part != 1 and part != 2:
        pass
    file = open("Data/Input/Day04.txt")
    data = [line.rstrip() for line in file]

    cards = []
    total_winnings = 0
    for entry in data:
        sections = entry.split(": ")
        card_no = int(sections[0].removeprefix("Card "))
        lists = sections[1].split(" | ")
        winning_list = [int(value.strip()) for value in lists[0].split(" ") if value.isnumeric()]
        our_list = [int(value.strip()) for value in lists[1].split(" ") if value.isnumeric()]

        winnings = 0
        for number in our_list:
            if number in winning_list:
                if part == 1:
                    winnings = winnings * 2 if winnings != 0 else 1
                else:
                    winnings += 1
        # print(winnings)
        total_winnings += winnings
        
        if part == 2:
            cards.append((card_no, winning_list, our_list, winnings))

    if part == 1:
        print(total_winnings)
    else:
        print(handle_part2_cards(cards))

execute_day(2)
