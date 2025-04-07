# +-------------------+
# Pig Latin Translator|
# +-------------------+

print("PIG LATIN TRANSLATOR")


def english_to_piglatin(text):
    """
    Rule:
    → If a word starts with a vowel (a,e,i,o,u), add "way" to the end.
        • apple → appleway

    → if a word starts with a consonent, move the first letter to the end and add "ay"
        • hello → ellohay
    """

    vowels = "aeiouAEIOU"
    pig_latin_sentence = ""

    for word in text.split():
        if word[0] in vowels:
            pig_word = word + "way"
        else:
            pig_word = word[1:] + word[0] + "ay"
        pig_latin_sentence += pig_word + " "

    return pig_latin_sentence.strip()


def piglatin_to_english(text):
    """
    Rule:
    → If a word ends with "way", remove "way" to get the original word
        • appleway → apple

    → if a wod ends with "ay" and is longer than 2 letters, move the last consonent from the end back
        • ellohay → hello

    """
    english_sentence = ""
    for word in text.split():
        if word.endswith("way"):
            english_word = word[:-3]
        elif word.endswith("ay") and len(word) > 2:
            english_word = word[-3] + word[:-3]
        else:
            english_word = word
        english_sentence += english_word + " "

    return english_sentence.strip()


while True:
    print("\nMENU:")
    print("1. English to Pig Latin Translator")
    print("2. Pig Latin to English Translator")
    print("3. Quit\n")

    choice = int(input("Enter Your Choice: "))

    match choice:
        case 1:
            sentence = input("Enter a sentence to translate into Pig Latin:\n")
            translation = english_to_piglatin(sentence)
            print("\nPig Latin Translation:")
            print(translation)
        case 2:
            sentence = input("Enter a Pig Latin sentence to translate back to english:\n")
            translation = piglatin_to_english(sentence)
            print("\nEnglish Translation")
            print(translation)
        case 3:
            print("Goodbye!")
            break
        case _:
            print("Invalid Choice. Please choose from 1, 2 and 3.")
