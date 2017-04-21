from Prac07.guitar import Guitar


def main():
    guitars = []
    while True:
        name = input("Guitar name: ")
        if name == "":
            break
        year = int(input("Year made: "))
        cost = float(input("Cost: "))
        guitars.append(Guitar(name,year,cost))
    for guitar in guitars:
        print(guitar)
main()