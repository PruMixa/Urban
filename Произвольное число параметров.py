def single_root_words (root_word, *other_word):

    same_word = []
    root_word_lower = root_word.lower()

    for word in other_word:
        word_lower = word.lower()
        if root_word_lower in word_lower or word_lower in root_word_lower:
            same_word.append(word)

    return same_word

result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)