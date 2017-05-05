from Prac08.taxi import Taxi
from Prac08.taxi import UnreliableCar
from Prac08.taxi import SilverServiceTaxi

def main():
    prius_one = Taxi("Prius 1", 100)
    prius_one.start_fare()
    prius_one.drive(40)
    prius_one.get_fare()
    print(prius_one)
    prius_one.start_fare()
    prius_one.add_fuel(100)
    prius_one.drive(100)
    print(prius_one)
    ute = UnreliableCar("Clunker", 100, 50)
    ute.drive(10)
    print(ute)
    hummer = SilverServiceTaxi("Hummer", 100, 2)
    hummer.drive(10)
    print(hummer)
    print(hummer.get_fare())
main()