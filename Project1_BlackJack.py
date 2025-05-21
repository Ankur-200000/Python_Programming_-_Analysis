from art import logo
import random
print(logo)

cards = {
    "A": [1, 11],
    "K": 10,
    "J": 10,
    "Q": 10,
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10
}

def start_game():
    random_card = ""
    random_card2 = ""
    computer_card = ""
    card_value = 0
    card_value2 = 0
    computer_value = 0
    random_card = random.choice(list(cards.keys()))
    random_card2 = random.choice(list(cards.keys()))
    computer_card = random.choice(list(cards.keys()))
    card_value = cards[random_card]
    card_value2 = cards[random_card2]

    your_hand = [random_card, random_card2]
    your_hand_values = []
    computer_hand = [computer_card]
    computer_hand_values = []

    if computer_card == "A":
        computer_hand_values.append(11)
    else:
        computer_value = cards[computer_card]
        computer_hand_values.append(computer_value)

    if random_card == "A" and random_card2 == "A":
        print("You drew 2 Aces. One of them will be worth 1 point while the other will be worth 11.\n")
        your_hand_values.extend([1, 11])

    elif random_card == "A":
        your_hand_values.append(card_value2)
        user_correct = False
        while not user_correct:
            user_ace_value_str = input("You drew an Ace. Type '0' to give it 1 point of value, or type '1' to give it 11 points of value.\n")
            try:
                user_ace_value = int(user_ace_value_str)
                if user_ace_value == 0:
                    your_hand_values.append(1)
                    user_correct = True
                elif user_ace_value == 1:
                    your_hand_values.append(11)
                    user_correct = True
                else:
                    print(f"You typed {user_ace_value_str}. Please type either '0' or '1'.")
            except ValueError:
                print("Please put valid inputs.")

    elif random_card2 == "A":
        your_hand_values.append(card_value)
        user_correct2 = False
        while not user_correct2:
            user_ace_value_str2 = input("You drew an Ace. Type '0' to give it 1 point of value, or type '1' to give it 11 points of value.\n")
            try:
                user_ace_value2 = int(user_ace_value_str2)
                if user_ace_value2 == 0:
                    your_hand_values.append(1)
                    user_correct2 = True
                elif user_ace_value2 == 1:
                    your_hand_values.append(11)
                    user_correct2 = True
                else:
                    print(f"You typed {user_ace_value_str2}. Please type either '0' or '1'.")
            except ValueError:
                print("Please put valid inputs.")

    else:
        your_hand_values.extend([card_value, card_value2])

    print(f"Your cards are: {your_hand}. Your current score is: {sum(your_hand_values)}")
    print(f"Computer's first card: {computer_hand}. Computer score is: {computer_hand_values}")

    if sum(your_hand_values) == 21:
        print("You win with Black Jack!")
    else:
        keep_hitting = True
        while keep_hitting:
            hit = input("Type 'y' to get another card. type 'n' to pass.\n").lower()
            random_card_new = ""
            random_card_new_value = 0

            if hit == 'y':
                random_card_new = random.choice(list(cards.keys()))

                if random_card_new == "A":
                    user_correct3 = False
                    while not user_correct3:
                        user_ace_value_str3 = input("You drew an Ace. Type '0' to give it 1 point of value, or type '1' to give it 11 points of value.\n")
                        try:
                            user_ace_value3 = int(user_ace_value_str3)
                            if user_ace_value3 == 0:
                                your_hand.append("A")
                                your_hand_values.append(1)
                                user_correct3 = True
                            elif user_ace_value3 == 1:
                                your_hand.append("A")
                                your_hand_values.append(11)
                                user_correct3 = True
                            else:
                                print(f"You typed {user_ace_value_str3}. Please type either '0' or '1'.")
                        except ValueError:
                            print("Please put valid inputs.")
                else:
                    random_card_new_value = cards[random_card_new]
                    your_hand.append(random_card_new)
                    your_hand_values.append(random_card_new_value)
                    while sum(your_hand_values) > 21 and 11 in your_hand_values:
                        your_hand_values[your_hand_values.index(11)] = 1  # Change an 11 to a 1

                print(f"Your cards are: {your_hand}. Your score is {sum(your_hand_values)}.")
                print(f"Computer's first card: [{computer_card}]. Computer's score is: {computer_value}")
                if sum(your_hand_values) > 21:
                    print(f"Your final hand: {your_hand}. Your final score: {sum(your_hand_values)}.\nComputer's final hand: {computer_hand}. Computer's final score: {computer_hand_values}.\nYou went over the limit, you lose!")
                    keep_hitting = False
                if sum(your_hand_values) == 21:
                    print(f"Your final hand: {your_hand}. Your final score: {sum(your_hand_values)}.\nComputer's final hand: {computer_hand}. Computer's final score: {computer_hand_values}.\nYou win with Black Jack!")
                    keep_hitting = False

            elif hit == 'n':
                keep_hitting = False
                print(f"Your final hand: {your_hand}. Your final score: {sum(your_hand_values)}.")
                computer_turn = True
                while computer_turn and sum(computer_hand_values) <= 17: #just to give the computer some intelligence
                    computer_card_new = ""
                    computer_card_new_value = 0
                    computer_card_new = random.choice(list(cards.keys()))

                    if computer_card_new == "A":
                        if sum(computer_hand_values) <= 10:
                            computer_hand.append("A")
                            computer_hand_values.append(11)
                            if sum(computer_hand_values) == 21:
                                print(f"Computer's final hand: {computer_hand}. Computer's final score: {sum(computer_hand_values)}.\nYour opponent won with Black Jack. You lose!")
                                computer_turn = False
                            elif sum(computer_hand_values) > sum(your_hand_values):
                                print(f"Computer's final hand: {computer_hand}. Computer's final score: {sum(computer_hand_values)}.\nYour opponent won!")
                                computer_turn = False

                        elif sum(computer_hand_values) > 10:
                            computer_hand.append("A")
                            computer_hand_values.append(1)
                            if sum(computer_hand_values) == 21:
                                print(f"Computer's final hand: {computer_hand}. Computer's final score: {sum(computer_hand_values)}.\nYour opponent won with Black Jack. You lose!")
                                computer_turn = False
                            elif sum(computer_hand_values) > sum(your_hand_values):
                                print(f"Computer's final hand: {computer_hand}. Computer's final score: {sum(computer_hand_values)}.\nYour opponent won!")
                                computer_turn = False

                    else:
                        computer_hand.append(computer_card_new)
                        computer_card_new_value = cards[computer_card_new]
                        computer_hand_values.append(computer_card_new_value)
                        while sum(computer_hand_values) > 21 and 11 in computer_hand_values:
                            computer_hand_values[computer_hand_values.index(11)] = 1  # Change an 11 to a 1

                        if sum(computer_hand_values) > 21:
                            print(f"Computer's final hand: {computer_hand}. Computer's final score: {sum(computer_hand_values)}.\nYour opponent went over. You win!")
                            computer_turn = False
                        elif sum(computer_hand_values) == 21:
                            print(f"Computer's final hand: {computer_hand}. Computer's final score: {sum(computer_hand_values)}.\nYour opponent won with Black Jack. You lose!")
                            computer_turn = False
                        elif sum(computer_hand_values) > sum(your_hand_values):
                            print(f"Computer's final hand: {computer_hand}. Computer's final score: {sum(computer_hand_values)}.\nYour opponent won!")
                            computer_turn = False

                if sum(computer_hand_values) == sum(your_hand_values):
                    print(f"Computer's final hand: {computer_hand}. Computer's final score: {sum(computer_hand_values)}.\nYou draw!")
                elif sum(computer_hand_values) < sum(your_hand_values):
                    print(f"Computer's final hand: {computer_hand}. Computer's final score: {sum(computer_hand_values)}.\nYou won!")

            else:
                print(f"You typed {hit}. Please type either 'y' or 'n'.")

should_continue = True
while should_continue:
    play = input("Do you want to play a game of Black Jack? Type 'y' or 'n'.\n").lower()

    if play == 'y':
        print("\n" * 100)
        print(logo)
        start_game()
    elif play == 'n':
        should_continue = False
    else:
        print("Please type a valid input. Please type 'y' or 'n'.")

