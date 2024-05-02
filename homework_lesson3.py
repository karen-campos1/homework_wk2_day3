#Python List Transforamtion
#Task1
grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
grades.sort(reverse=True)
print(grades)


#Task2
grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
print(sum(grades)/len(grades))


#Advanced list methods and identify operators
#Task1
submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]

good_students = []
for student in submitted:
    if student in attended:
        good_students.append(student)
print(f"The good students are {good_students}") #had to move the print statement out of loop to print Alice once



#Advanced Slicing Techniques
#Task1
temperatures = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 
                94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]

#Extract the temperatures for the second week (7 days) of the month (index 7 to index 14)
second_week = temperatures[7:14]
print(second_week)


#Task2
temperatures = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 
                94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]
hot_temp = []
for temp in temperatures:
    if temp > 100:
        hot_temp.append(temp)
print(f"These are the temps exceeding 100 {hot_temp}")