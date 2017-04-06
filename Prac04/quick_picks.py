import random


def main():
    pick = int(input("How many quick picks do you want?"))
    for count in range(pick):
        quick_picks = []
        for number in range(1, 6):
            random_number = random.randint(1, 45)
            while random_number in quick_picks:
                random_number = random.randint(1, 45)
            quick_picks.append(random_number)
        print("{:4}{:4}{:4}{:4}{:4}".format(quick_picks[0], quick_picks[1], quick_picks[2], quick_picks[3], quick_picks[4]))

main()
