# project 1 Quiz Game

print("Welcome to the quiz")

while True:
    playing = input(" Do you want to play ? type 'yes' if you want or 'no' if you don't. ").lower()
    if playing in {"yes","no"}:
        if playing != "yes":
            print("Okay Goodbye ")
            quit()
        else:
            print("okay let's play ")
            break
    else:print(" i didn't get that. Can you re-type? ")

count = 0
wrong = []

Q1 = input("What is sum of 33 + 77? ")
if Q1 == '110':
    count+=1
else: wrong.append("Q1")

Q2 = input("What is the biggest rodent? ").lower()
if Q2 == 'capybara':
    count+=1
else: wrong.append("Q2")

Q3 = input("What is RAM stand for? ").lower()
if Q3 == 'random access memory':
    count+=1
else: wrong.append("Q3")

Q4 = input("What is Marvel first superhero movie? ").lower()
if Q4 == 'ironman':
    count+=1
else: wrong.append("Q4")


print("You got", count, "score.")

if count < 4:
    review = input("type 'show' to see which answer you got wrong or 'pass' to end. ")
    if review == "show":
        print("you got", wrong, "wrong.")
    elif review == "pass":
        quit()
    else:
        print(" i didn't get that. Can you re-type? ")
