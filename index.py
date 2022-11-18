#Global Variables
score = 0

print("Welcome to my pop quiz!")

playing=(input("Would you like to play? "))

if  playing.lower() != "yes":
    quit()

print("Lets Play!")

answer = input("In which movie would you hear the song 'Hakuna Matata'?\n")
if answer.lower() == "Lion King".lower():
    print("Correct!")
    score += 1
else:
    print("incorrect!")

answer = input("What is the orange part of an egg called?\n")
if answer.lower() == "Yolk".lower():
    print("Correct!")
    score += 1
else:
    print("incorrect!")

answer = input("What is the closest planet to the Sun?\n")
if answer.lower() == "Mercury".lower():
    print("Correct!")
    score += 1
else:
    print("incorrect!")

answer = input("How many days are there in a year?\n")
if answer.lower() == "365".lower():
    print("Correct!")
    score += 1
else:
    print("incorrect!")

answer = input("Where do polar bears live?\n")
if answer.lower() == "The Arctic".lower():
    print("Correct!")
    score += 1
else:
    print("incorrect!")

answer = input("What is the name of the tallest mountain on earth?\n")
if answer.lower() == "Mount Everest".lower():
    print("Correct!")
    score += 1
else:
    print("incorrect!")

answer = input("My mothers mother is my…what?\n")
if answer.lower() == "Grandmother".lower():
    print("Correct!")
    score += 1
else:
    print("incorrect!")

answer = input("Which animal lays the largest eggs?\n")
if answer.lower() == "Ostrich".lower():
    print("Correct!")
    score += 1
else:
    print("incorrect!")

answer = input("How many zeros are in ten thousand?\n")
if answer.lower() == "Four Zeros".lower():
    print("Correct!")
    score += 1
else:
    print("incorrect!")

answer = input("What is a baby kangaroo called?\n")
if answer.lower() == "Joey".lower():
    print("Correct!")
    score += 1
else:
    print("incorrect!")

print("You got " + str(score) + " questions correct!")