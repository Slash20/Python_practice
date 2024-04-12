def count_words(text):
    word_counts = {}
    for word in text.lower().split():
        word_counts[word] = word_counts.get(word, 0) + 1
    print(word_counts)
    return word_counts


def sort_key(item):
    return -item[1], item[0]


text = input()
word_counts = count_words(text)
sorted_words = sorted(word_counts.items(), key=sort_key)
for word, count in sorted_words:
    print(word)
