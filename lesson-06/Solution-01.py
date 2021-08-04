my_text = input("Enter text: ")
my_text_split = my_text.split()
frequend_word_len = 0

for word in range(len(my_text_split)):
    if len(my_text_split[word]) > len(my_text_split[frequend_word_len]):
        frequend_word_len = word
print("Longest word: ", my_text_split[frequend_word_len])
print("Frequend_word: ", max(set(my_text_split), key=my_text_split.count))
