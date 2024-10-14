import random

days_of_the_week = ["sunday","monday","tuesday","wednesday","thursday","friday","saturday"]
moods = ["happy","sad","energetic","calm"]
mood_tracker = {}

for day in days_of_the_week:
    mood_tracker[day] = {}

    for time in ["morning", "afternoon","evening"]:
        mood = random.choice(moods)
        mood_tracker[day][time] = mood

for day, moods in mood_tracker.items():
    print(f"on {day}")
    for time, mood in moods.items():
        print(f" {time} you were {mood}")