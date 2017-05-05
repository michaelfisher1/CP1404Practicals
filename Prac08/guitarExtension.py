from Prac07.guitar import Guitar


def main():
    guitars = []
    in_file = open("guitars.csv", "r")
    for line in in_file:
        parts = line.strip().split(",")
        guitar = (parts[0], parts[1], parts[2])
        guitars.append(guitar)
    in_file.close()
    for guitar in guitars:
        print(guitar)
    guitar_objects = []
    in_file = open("guitars.csv", "r")
    for line in in_file:
        parts = line.strip().split(",")
        guitar_object = Guitar(parts[0], int(parts[1]),float(parts[2]))
        guitar_objects.append(guitar_object)
    for guitar_object in guitar_objects:
        print(guitar_object)
    in_file.close()
    print("Sorted by year")
    guitar_objects.sort()
    for guitar_object in guitar_objects:
        print(guitar_object)
    print("Adding New Guitars")
    name = input("Guitar name: ")
    while name != "":
        year = int(input("Year made: "))
        cost = float(input("Cost: "))
        guitar_objects.append(Guitar(name, year, cost))
        name = input("Guitar name: ")
    out_file = open("guitars.csv", "w")
    for guitar_object in guitar_objects:
        out_file.write("{},{},{}\n".format(guitar_object.name,guitar_object.year,guitar_object.cost))
    out_file.close()
main()