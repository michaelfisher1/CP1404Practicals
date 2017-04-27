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
    print("These are my guitars:")
    for guitar in guitars:
        i = 0
        print(guitar)
        i += 1
main()