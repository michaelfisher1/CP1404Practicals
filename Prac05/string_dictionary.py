def main():
    word_dict = {}
    # sentence = input("Input a sentence to count:").lower()
    sentence = "this is a collection of words of nice words this is a fun thing it is "
    new_sentence = sentence.split()
    for word in new_sentence:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1
    for key, value in word_dict.items():
        print("{} : {}".format(key, value))


main()
