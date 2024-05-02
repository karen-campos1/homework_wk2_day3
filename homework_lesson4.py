# Python loop statements
#Task1


import random
#Create list for day of the week
day = ["Sunday", "Monday", "Tuesday", "Thursday", "Friday", "Saturday"]
#create list for moods
mood = ["happy", "sad", "energetic", "calm", "stressed"]
#loop function and range 
for i in range(len(day)):
    print(f"On {day[i]} you felt {random.choice(mood)}")
  
    
#Double scoop with nested loops
#Task1
weekday = ["Sunday", "Monday", "Tuesday", "Thursday", "Friday", "Saturday"]
time_of_day = ["morning", "afternoon", "evening"]
for day in weekday:
    for time in time_of_day:
        print(f"This {day} during the {time} I felt {random.choice(mood)}")
        