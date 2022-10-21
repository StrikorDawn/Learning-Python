ride = False
golden_pass_1 = False

age1 = int(input("How old are you? "))
height1 = int(input("How many inches tall are you? "))

if age1 >= 12 and age1 < 18:
    golden_pass_1 = input('Do you have a Golden Passport (yes/no)? ').lower()
    if golden_pass_1 == 'yes':
        golden_pass_1 = True
    else:
        golden_pass_1 = False

riders = input("Are there 2 riders? ").lower()

if riders == 'yes':
    print("Please input the second riders information.")
    age2 = int(input("How old are you? "))
    height2 = int(input("How many inches tall are you? "))
    if age2 >= 12 and age2 < 18:
        golden_pass_2 = input("Do you have a Golden Passport (yes/no)? ")
    
    if height1 < 36 or height2 < 36:
        ride = False
    else:

        if age1 >= 18 or age2 >= 18 or golden_pass_1 or golden_pass_2:
            ride = True
        else:

            if age1 >= 12 and height1 >= 52 and age2 >= 12 and height2 >= 52:
                ride = True
            elif (age1 >= 16 and age2 >=14) or (age1 >= 14 and age2 >=16):
                ride = True
            else:
                ride = False
else:
    if (age1 >= 18 or golden_pass_1) and height1 >=62:
        ride = True
    else:
        ride = False

if ride:
    print("Welcome aboard! Enjoy the ride!!!")

else:
    print("Sorry, you cannot ride.")