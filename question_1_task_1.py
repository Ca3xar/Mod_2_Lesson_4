import random

moods = ["happy","sad","energetic","calm"]
days_of_the_week = ["sunday","monday","tuesday","wednesday","thursday","friday","saturday"]

for day in days_of_the_week:
    mood = random.choice(moods)
    print(f"on {day}, you were feeling {mood}")
