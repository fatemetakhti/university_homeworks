a = input("Enter your score > ")

if int(a) > 90:
    b = "Perfect"
elif int(a) > 70:
    b = "Good"
elif int(a) > 50:
    b = "Intermediate"
else:
    b = "Failed"

print(b)