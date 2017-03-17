finished = False
result = 0
while not finished:
    try:
        result = int(input("Enter an Integer: "))
    except ValueError:
        print("Please enter a valid integer.")
    finished = True
print("Valid result is : {}".format(result))


