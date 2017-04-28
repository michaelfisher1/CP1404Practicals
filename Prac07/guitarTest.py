from Prac07.guitar import Guitar


def main():
    guitars = []
    name = input("Guitar name: ")
    while name != "":
        year = int(input("Year made: "))
        cost = float(input("Cost: "))
        guitars.append(Guitar(name,year,cost))
        name = input("Guitar name: ")
    print("These are my guitars:")
    for i, guitar in enumerate(guitars):
        if guitar.is_vintage():
            vintage_string = "(vintage)"
        else:
            vintage_string = ""
        print("Guitar {}: {:>20} ({}), worth ${:10,.2f} {}".format(i + 1, guitar.name, guitar.year, guitar.cost,
                                                                   vintage_string))
main()