from enum import IntEnum

part = 2

class HandType(IntEnum):
    NONE = -1
    HIGH_CARD = 0
    ONE_PAIR = 1
    TWO_PAIR = 2
    THREE_OF_A_KIND = 3
    FULL_HOUSE = 4
    FOUR_OF_A_KIND = 5
    FIVE_OF_A_KIND = 6

def determine_hand_from_joker(card, hand):
    if part == 1:
        return hand
    else:
        return hand.replace('J', card)

def determine_five_of_a_kind(hand):
    for card in set(hand):
        test_hand = determine_hand_from_joker(card, hand)
        if test_hand == len(test_hand) * card:
            return True
    return False

def determine_four_of_a_kind(hand):
    for card in set(hand):
        test_hand = determine_hand_from_joker(card, hand)
        if test_hand.count(card) == 4:
            return True
    return False

def determine_full_house(hand):
    for test_card in set(hand):
        test_hand = determine_hand_from_joker(test_card, hand)
        has_found_three_pair = False
        has_found_two_pair = False
        for card in set(test_hand):
            if test_hand.count(card) == 3:
                has_found_three_pair = True
            if test_hand.count(card) == 2:
                has_found_two_pair = True
        if has_found_three_pair and has_found_two_pair:
            return True
        if part == 1:
            break
    return False

def determine_three_of_a_kind(hand):
    for test_card in set(hand):
        test_hand = determine_hand_from_joker(test_card, hand)
        has_found_three_pair = False
        has_found_two_pair = False
        for card in set(test_hand):
            if test_hand.count(card) == 3:
                has_found_three_pair = True
            if test_hand.count(card) == 2:
                has_found_two_pair = True
        if has_found_three_pair and not has_found_two_pair:
            return True
        if part == 1:
            break
    return False

def determine_two_pair(hand):
    for test_card in set(hand):
        test_hand = determine_hand_from_joker(test_card, hand)
        two_pair_count = 0
        for card in set(test_hand):
            if test_hand.count(card) == 2:
                two_pair_count += 1
        if two_pair_count == 2:
            return True
        if part == 1:
            break
    return False

def determine_one_pair(hand):
    for test_card in set(hand):
        test_hand = determine_hand_from_joker(test_card, hand)
        two_pair_count = 0
        unique_count = 0
        for card in set(test_hand):
            if test_hand.count(card) == 2:
                two_pair_count += 1
            if test_hand.count(card) == 1:
                unique_count += 1
        if two_pair_count == 1 and unique_count == 3:
            return True
        if part == 1:
            break
    return False

def determine_high_card(hand):
    if part == 1:
        test_hand = hand
    else:
        test_hand = hand.replace('J', '')
    for card in set(test_hand):
        if test_hand.count(card) != 1:
            return False
    return True

def determine_hand_type(hand):
    if determine_five_of_a_kind(hand):
        return HandType.FIVE_OF_A_KIND
    if determine_four_of_a_kind(hand):
        return HandType.FOUR_OF_A_KIND
    if determine_full_house(hand):
        return HandType.FULL_HOUSE
    if determine_three_of_a_kind(hand):
        return HandType.THREE_OF_A_KIND
    if determine_two_pair(hand):
        return HandType.TWO_PAIR
    if determine_one_pair(hand):
        return HandType.ONE_PAIR
    if determine_high_card(hand):
        return HandType.HIGH_CARD
    return HandType.NONE

def determine_card_value(card):
    if card.isnumeric():
        return int(card)
    match card:
        case 'T':
            return 10
        case 'J':
            if part == 1:
                return 11
            return 1
        case 'Q':
            return 12
        case 'K':
            return 13
        case 'A':
            return 14
    return -1

def determine_card_value_for_hand(hand):
    hand_values = []
    for card in hand:
        hand_values.append(determine_card_value(card))
    return tuple(hand_values)

def execute_day():
    if part != 1 and part != 2:
        pass
    file = open("Data/Input/Day07.txt")
    data = [line.rstrip() for line in file]

    hands = []
    for entry in data:
        hand, bid = entry.split(" ")
        bid = int(bid)
        hands.append((hand, bid))
    
    for idx, hand_bid_pair in enumerate(hands):
        hand, bid = hand_bid_pair
        hand_type = determine_hand_type(hand)
        hands[idx] = (hand, bid, hand_type)
    
    hands.sort(key=lambda x: (x[2], determine_card_value_for_hand(x[0])))

    sum_of_rankings = 0
    for idx, hand_bid__type_pair in enumerate(hands):
        rank = idx + 1
        hand, bid, type = hand_bid__type_pair
        print(hand_bid__type_pair, " ", bid * rank)
        sum_of_rankings += bid * rank
    print(sum_of_rankings)

execute_day()