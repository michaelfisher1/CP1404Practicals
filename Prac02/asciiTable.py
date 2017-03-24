def get_number():
    valid_input = False
    while not valid_input:
        try:
            user_number = int(input("Enter a number: "))
            while user_number < 33 or user_number > 127:
                print("You must enter a valid number between 33 and 127")
                user_number = int(input("Enter a number: "))
            valid_input = True
            return user_number
        except ValueError:
                print("You must enter a valid number")

def main():
    user_number = get_number()
    user_char = input("Enter a character: ")
    print("The ASCII code for ",user_char,"is",ord(user_char))
    print("The character for",user_number,"is",chr(user_number))

    for i in range(33,127):
        print("{:5} {:>2}".format(i,chr(i)))
main()

