
def words_tokens(text: str):
    my_words = {}
    splited_text = text.split()
    print(splited_text)
    for word in splited_text:
        if word in my_words:
            my_words[word] += 1
        else:
            my_words[word] = 1
    print(my_words)

words_tokens("A dictionary where keys are words from the text and values are their corresponding frequencies.")