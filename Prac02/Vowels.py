VOWELS = "AaEeIiOoUu"
vowel_count = 0
name = input("Enter your name: ")
for char in name:
    if char in VOWELS:
        vowel_count+=1
print("Out of {} letters, {} has {} vowels.".format(len(name),name,vowel_count))
