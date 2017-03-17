out_file = open("name.txt", "w")
name = input("Enter your name: ")
print(name, file=out_file)
out_file.close()

in_file = open("name.txt","r")
user_name = in_file.read().strip()
print("Your name is: ",user_name)
in_file.close()

