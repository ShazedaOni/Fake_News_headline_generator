import random


subjects = [
    "Shahrukh khan",
    "Virat kohli",
    "Nirmala",
    "A Mumbai cat",
    "A Group of Monkey",
    "Prime Minister Modi",
    "Auto Rickshaw driver from Delhi"
]

actions = [
    "launches",
    "cancels",
    "dances with",
    "eats",
    "dectares war on",
    "orders",
    "celebrates"
]

places_or_things = [
    "at Red Fort",
    "in Mumbai Local Train",
    "a plate of samosa",
    "inside parliament",
    "at Ganga Ghat",
    "during IPL Match",
    "at India gate"
]

while True:
    subject = random.choice(subjects)
    action = random.choice(actions)
    places = random.choice(places_or_things)

    headline = f"Breaking News: {subject} {action} {places} "

    print("\n" + headline)

    user_input = input("\n do you want another headline? (yes/no)".strip().lower())
    if user_input == "no":
        break

print("\n Thanks for using the Fake News Headline generator for a Fun")