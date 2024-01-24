def word_counter():
    text = input("Enter something:")
    word_count = len(text.split())
    print("Word count:", word_count)

def word_reverse():
    text = input("Enter a word:")
    reversed_text = text[::-1]
    print("Reversed text:", reversed_text)

def vowel_count():
    word = input("Enter a word:")
    vowel_count = sum(1 for char in word if char.lower() in "aeiou")
    print("Anzahl Vokale:", vowel_count)

def char_frequency():
    text = input("Gib einen Text ein: ")
    char_frequency = {char: text.count(char) for char in set(text)}
    print("Zeichenfrequenzen:", char_frequency)

word_counter()
word_reverse()
vowel_count()
char_frequency()