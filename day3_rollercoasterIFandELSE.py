print("Welcome to the rollercoaster")
height = int(input("What is your height in cm?"))
if height > 20:
    print("You can ride the rollercoaster")
    age=int(input("Enter your age"))
    if age < 12:
        print("Children ticket costs $5")
    elif age <=18:
        print("Youth ticket costs $7")
    else:
        print("Adult ticket costs $12")
else:
    print("You can't ride the rollercoaster")
    