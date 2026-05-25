#! Random Module
import random

#? 1. "random.random()": Generates a random float between 0.0 and 1.0
# print(random.random())

#? 2. random.randint(a, b) — Generates a random integer between a and b, including both.
# print(random.randint(5, 10))

#? 3. random.randrange(n) — Generates a random integer from 0 to n-1.
# print(random.randrange(8, 10)) # 0, 9

#? 4. random.uniform(a, b) — Generates a random float between a and b.
# print(random.uniform(5, 10))

#? 5. random.choice(seq) — Picks one random item from a sequence.
# print(random.choice(["a", "b", "c"]))

#? 6. random.choices(seq, k=n) — Picks multiple random items, allowing repeats.
# print(random.choices(["a", "b", "c"], k = 2))

#? 7. random.sample(seq, k=n) — Picks multiple unique random items, without repeats.
# print(random.sample(["a", "b", "c"], 2))

#? 8. random.shuffle(list) — Randomly changes the order of items in the original list.
# lst = ["a", "b", "c"]
# random.shuffle(lst)
# print(lst)
#
# print(random.shuffle([1, 2, 3]))  #! None - Don't use this!


#! Reproducibility

# random.seed(42)
# print(random.random())
# print(random.randint(1, 10))


#! Security
import secrets

#? secrets.randbelow(n): Secure random int in [0, n)
print(secrets.randbelow(10))

#? secrets.choice(seq): Secure random values from sequence
print(secrets.choice([1, 2, 3]))

#? secrets.token_hex(n): Generates a secure random token in hexadecimal format
print(secrets.token_hex(4))

#? secrets.token_urlsafe(n): Generates a secure random token that is safe to use in URLs
print(secrets.token_urlsafe(16))














