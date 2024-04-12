def count_word_occurrences(text):
    word_count = {}
    words = text.split()

    for word in words:
        if word in word_count:
            print(word_count[word], end=" ")
        else:
            print("0", end=" ")
        word_count[word] = word_count.get(word, 0) + 1


input_text = input("Введите какой-нибудь текст: ")

count_word_occurrences(input_text)