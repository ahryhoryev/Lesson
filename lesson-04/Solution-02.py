sentence = input("Enter text: ")

if sentence == sentence[::-1]:
    print(f'This is palindrome: {sentence}')
else:
    print(f'This is not palindrome: {sentence}')
