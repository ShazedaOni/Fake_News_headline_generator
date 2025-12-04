import random
from datetime import datetime

# ===============================
# 📌 DATA FOR CATEGORIES
# ===============================

categories = {
    "bollywood": {
        "subjects": ["Shahrukh Khan", "Salman Khan", "Alia Bhatt", "Deepika Padukone"],
        "actions": ["dances with", "launches", "rejects", "celebrates with"],
        "places": ["at Film City", "on movie set", "during award show", "at Bandra"],
    },
    "politics": {
        "subjects": ["Prime Minister Modi", "Rahul Gandhi", "A Delhi Minister", "Nirmala Sitharaman"],
        "actions": ["declares", "cancels", "orders", "announces"],
        "places": ["in Parliament", "at Red Fort", "during a rally", "at India Gate"],
    },
    "sports": {
        "subjects": ["Virat Kohli", "MS Dhoni", "Rohit Sharma", "Kapil Dev"],
        "actions": ["hits", "celebrates", "shocks everyone with", "refuses"],
        "places": ["during IPL match", "at Wankhede Stadium", "in the dressing room", "at practice session"],
    },
    "animals": {
        "subjects": ["A Mumbai Cat", "A Group of Monkeys", "A Lazy Panda", "A Talking Parrot"],
        "actions": ["steals", "eats", "dances with", "runs away with"],
        "places": ["at zoo", "near Ganga ghat", "inside a shop", "on the street"],
    },
    "random": {
        "subjects": [
            "Auto Rickshaw Driver from Delhi",
            "A Social Media Influencer",
            "A College Student",
            "A Tech YouTuber"
        ],
        "actions": ["creates", "destroys", "reacts to", "vlogs about"],
        "places": ["outside metro station", "during livestream", "at a cafe", "in a traffic jam"],
    }
}

# 🎉 Fun emojis
emojis = ["😂", "🤣", "😱", "🔥", "🙈", "🇮🇳", "🎉", "✨", "😳", "🐒", "😜"]

# File name for saving headlines
file_name = "headlines_pro.txt"


# ===============================
# 📌 FUNCTION TO GENERATE HEADLINE
# ===============================
def generate_headline(category):
    data = categories[category]

    subject = random.choice(data["subjects"])
    action = random.choice(data["actions"])
    place = random.choice(data["places"])

    timestamp = datetime.now().strftime("%Y-%m-%d %I:%M %p")

    emoji_string = "".join(random.sample(emojis, k=random.randint(1, 3)))

    headline = f"[{timestamp}] Breaking News: {subject} {action} {place}! {emoji_string}"

    return headline


# ===============================
# 📌 MAIN MENU LOOP
# ===============================
def main():
    print("\n🎉 Welcome to Fake News Headline Generator🎉")

    while True:
        print("\n----------------------------------")
        print("1. Generate ONE headline")
        print("2. Generate MULTIPLE headlines")
        print("3. Choose CATEGORY for headline")
        print("4. Exit")
        print("----------------------------------")

        choice = input("\nEnter your choice (1/2/3/4): ").strip()

        if choice == "1":
            headline = generate_headline("random")
            print("\n" + headline)
            save_to_file(headline)

        elif choice == "2":
            count = int(input("How many headlines do you want? "))
            for _ in range(count):
                headline = generate_headline("random")
                print(headline)
                save_to_file(headline)

        elif choice == "3":
            print("\nAvailable categories:")
            for c in categories.keys():
                print(" -", c)

            selected = input("\nEnter category name: ").strip().lower()

            if selected in categories:
                h = generate_headline(selected)
                print("\n" + h)
                save_to_file(h)
            else:
                print("❌ Invalid category!")

        elif choice == "4":
            print("\nThanks for using Fake News Generator! 😄")
            break

        else:
            print("❌ Invalid choice! Please try again.")


# ===============================
# 📌 SAVE HEADLINE TO FILE
# ===============================
def save_to_file(headline):
    with open(file_name, "a", encoding="utf-8") as f:
        f.write(headline + "\n")


# ===============================
# 📌 RUN THE PROGRAM
# ===============================
if __name__ == "__main__":
    main()
