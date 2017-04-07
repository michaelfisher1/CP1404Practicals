"""
CP1402 Practical
Hex Colour names in Dictionary
Practice
"""

COLOUR_NAMES = {"BlanchedAlmond": "#ffebcd", "Chocolate": "#d2691e", "LimeGreen": "#32cd32", "NavyBlue": "#000080",
                "OliveDrab": "#6b8e23", "PapayaWhip": "#ffefd5", "tomato1": "#ff6347", "WhiteSmoke": "#f5f5f5",
                "wheat": "#f5deb3", "thistle": "#d8bfd8"}


def main():
    for key, value in COLOUR_NAMES.items():
        print("{:<15} is {}".format(key, value))
    colour = input("Enter a colour to receive the hex code:")
    while colour != "":
        if colour in COLOUR_NAMES:
            print("{} is {}".format(colour, COLOUR_NAMES[colour]))
        else:
            print("Invalid colour, enter carefully.")
        colour = input("Enter a colour to receive the hex code:")


main()
