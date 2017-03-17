in_file = open("numbers.txt","r")
number_one = int(in_file.readline())
number_two = int(in_file.readline())
print(number_one+number_two)


inf_file = open("numbers.txt","r")
total = 0
for line in in_file:
    number = int(line)
    total += number
print(total)
in_file.close()