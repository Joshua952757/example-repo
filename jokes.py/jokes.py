import random

jokes = [
    ("Why don't scientists trust atoms?", "Because they make up everything!"),
    ("Why did the scarecrow win an award?", "Because he was outstanding in his field!"),
    ("What do you call fake spaghetti?", "An impasta!"),
    ("Why couldn't the bicycle stand up by itself?", "It was two-tired!"),
    ("What did one ocean say to the other ocean?", "Nothing, they just waved!")
]

joke, punchline = random.choice(jokes)
print(joke)
input("Press Enter for the punchline...")
print(punchline)
