text = ("Etiam tincidunt neque erat, quis molestie enim imperdiet vel."
        "Integer urna nisl, facilisis vitae semper at, dignissim vitae libero")

words = text.split()
new_words = []

for word in words:
    if word[-1] in [',', '.']:
        punctuation = word[-1]
        base_word = word[:-1]
        new_word = base_word + 'ing' + punctuation
    else:
        new_word = word + 'ing'
    new_words.append(new_word)

result = ' '.join(new_words)

print(result)
