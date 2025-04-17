# +-----------------------+
# ! Random Text Generator *
# +-----------------------+
import random
import string

num_paragraphs = input("Enter number of paragraphs: ")
num_sentences = input("Enter number of sentences per paragraph: ")

letters = string.ascii_lowercase
punctuation = ".?!"

if not num_paragraphs.isdigit() or not num_sentences.isdigit():
    print("ERROR: NON NUMERIC INPUT.")
else:
    num_paragraphs = int(num_paragraphs)
    num_sentences = int(num_sentences)

for _ in range(num_paragraphs):

    for _ in range(num_sentences):
        sentence = ""
        num_words = random.randint(5, 15)

        for _ in range(num_words):
            word = ""
            word_length = random.randint(2, 8)

            for _ in range(word_length):
                word += random.choice(letters)

            sentence += word + " "

        sentence = sentence.strip().capitalize() + random.choice(punctuation)
        print(sentence, end=" ")

    print("\n")












