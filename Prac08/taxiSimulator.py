from Prac08.taxi import Taxi
from Prac08.taxi import SilverServiceTaxi

MENU = "(q)uit, (c)hoose taxi, (d)rive"


def main():
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    bill_to_date = 0
    print("Let's Drive!")
    print(MENU)
    menu_choice = input(">>>")
    while menu_choice != "q":
        if menu_choice == "c":
            for i, taxi in enumerate(taxis):
                print(i,taxi)
            taxi_choice = int(input("Choose taxi:"))
            taxis[taxi_choice].start_fare()
            print("Bill to date: ${:.2f}".format(bill_to_date))
            print(MENU)
            menu_choice = input(">>>")
        if menu_choice == "d":
            distance = int(input("Drive how far: "))
            taxis[taxi_choice].drive(distance)
            print("Your {} trip cost you ${:.2f}".format(taxis[taxi_choice].name, taxis[taxi_choice].get_fare()))
            bill_to_date += taxis[taxi_choice].get_fare()
            print("Bill to date: ${:.2f}".format(bill_to_date))
            print(MENU)
            menu_choice = input(">>>")
    print("Total trip cost: ${:.2f}".format(bill_to_date))
    print("Taxis are now: ")
    for i, taxi in enumerate(taxis):
        print(i, taxi)
main()
