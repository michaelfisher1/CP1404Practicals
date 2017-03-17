user_char = input("Enter a character: ")
print("The ASCII code for ",user_char,"is",ord(user_char))
user_number = int(input("Enter a number between 33 and 127: "))
while user_number < 33 or user_number > 127:
    user_number = int(input("Your number must be between 33 and 127, please enter number: "))
print("The character for",user_number,"is",chr(user_number))

for i in range(33,127):
    print("{:5} {:>2}".format(i,chr(i)))

