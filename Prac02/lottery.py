import random
lower = 1
upper = 45
def main():
    number_of_picks = int(input("How many quick picks do you want?"))
    for i in range(1,number_of_picks+1):
        quick_pick = []
        for pick in range(1,7):
            random_number = random.randint(lower,upper)
            while random_number in quick_pick:
                random_number = random.randint(lower,upper)
            quick_pick.append(random_number)
        print(quick_pick)
main()
