# +-------------+
# Text Analyzer |
# +-------------+
import string

def text_analyzer(text):
    char_count = 0
    sentence_count = 0
    uppercase_count = 0
    lowercase_count = 0
    digit_count = 0
    vowel_count = 0
    special_char_count = 0

    words = text.split()
    word_count = len(words)

    vowels = "aeiouAEIOU"
    sentence_ends = ".?!"
    special_chars = string.punctuation

    for char in text:
        char_count += 1
        if char.isupper(): uppercase_count += 1
        elif char.islower(): lowercase_count += 1
        if char.isdigit(): digit_count += 1
        if char in vowels: vowel_count += 1
        if char in sentence_ends: sentence_count += 1
        if char in special_chars: special_char_count += 1

    print("TEXT ANALYSIS RESULTS")
    print("Total Characters: ", char_count)
    print("Total Words: ", word_count)
    print("Total Sentences: ", sentence_count)
    print("Uppercase Letters: ", uppercase_count)
    print("Lowercase Letters: ", lowercase_count)
    print("Total Vowels: ", vowel_count)
    print("Total Digits: ", digit_count)
    print("Total Special Characters Count: ", special_char_count)


user_input = input("Enter some text for analysis: ")
text_analyzer(user_input)