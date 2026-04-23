name = str (input(" Enter your name: "))
subject = str(input(" Enter name of subject: "))
mark = int(input(" Enter mark: "))

if mark > 100:
    print("Invalid mark. Mark should be between 0 and 100")
elif mark >= 75:
    print("Congradulations" + name + "You got an A in" + subject + " ")
elif mark >= 60:
    print("Congradulations" + name + "You got a B in" + subject + " ")
elif mark >= 50:
    print("Fair result" + name + "You got a C in" + subject + " ")
elif mark >= 40:
    print("sorry try next time" + "You got a D in" + subject + " ")
elif mark >= 30:
    print(" You have failed" + "You got an E" + subject + " ")
else:
    print("You\'ve failed" + name + "You got a U in" + subject + " ")
