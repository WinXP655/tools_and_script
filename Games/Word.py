def word_in_word(main_word, sub_word):
    main_word = main_word.lower()
    sub_word = sub_word.lower()
    return sub_word in main_word

main_word = input("Enter a main word: ")
sub_word = input("Enter a sub word: ")

if word_in_word(main_word, sub_word):
    print(f"'{sub_word}' is found in '{main_word}'.")
else:
    print(f"'{sub_word}' is not found in '{main_word}'.")