# Student Grade Calculator

name = input("Enter your name: ")

a = int(input("Enter your first subject marks: "))
b = int(input("Enter your second subject marks: "))
c = int(input("Enter your third subject marks: "))

total = a + b + c
percentage = (total / 300) * 100

if percentage >= 90:
    grade = "A"
elif percentage >= 80:
    grade = "B"
elif percentage >= 70:
    grade = "C"
else:
    grade = "D"

print("\n--- Student Result ---")
print("Name:", name)
print("Total Marks:", total)
print("Percentage:", percentage)
print("Grade:", grade)

Output:
Enter your name: Sayli
Enter your first subject marks: 98
Enter your second subject marks: 97
Enter your third subject marks: 95

--- Student Result ---
Name: Sayli
Total Marks: 290
Percentage: 96.66666666666667
Grade: A
