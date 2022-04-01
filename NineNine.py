print("Welcome the the Brooklyn Nine Nine Challenge")
username = input("What is your name? ")
if username:
    print("Hello" + ' ' + username)
else:
    print(" Hello user")

playing = input("Do you want to play? ").lower()
if playing == "yes":
    print("Okay! Let's play! This game can be very tricky. The details are very important with regards to answers")
else:
    quit()

count = 0

answer = input("Where is the show set? ").lower()
if answer == "new york city":
    print("Correct :)!")
    count += 1
else:
    print("Sorry that is incorrect :(.")
    count -= 1

answer = input("How many seasons does the show have? ").lower()
if answer == "8 seasons":
    print("Correct :)!")
    count += 1
else:
    print("Sorry that is incorrect :(.")
    count -= 1


answer = input("Who is the commanding officer of the precinct? ").lower()
if answer == "captain raymond holt":
    print("Correct :)!")
    count += 1
else:
    print("Sorry that is incorrect :(.")
    count -= 1

answer = input("How many female detectives are on the main cast? ").lower()
if answer == "2 female detectives":
    print("Correct :)!")
    count += 1
else:
    print("Sorry that is incorrect :(.")
    count -= 1

answer = input("How many detectives form the squad? ").lower()
if answer == "8 detectives":
    print("Correct :)!")
    count += 1
else:
    print("Sorry that is incorrect :(.")
    count -= 1

answer = input("Who are the oldest detectives on the squad? ").lower()
if answer == "detectives norm scully and micheal hitchcock":
    print("Correct :)!")
    count *= 2
else:
    print("Sorry that is incorrect :(.")
    count -= 1


answer = input("What is the name of the civillian administrator? ").lower()
if answer == "gina linetti":
    print("Correct :)!")
    count += 1
else:
    print("Sorry that is incorrect :(.")
    count -= 1

answer = input("Who won the sixth heist? ").lower()
if answer == " lieutenant terry jeffords":
    print("Correct :)!")
    count += 1
else:
    print("Sorry that is incorrect :(.")
    count -= 1

answer = input("What is the name of Charles's doppleganger? ").lower()
if answer == "bill":
    print("Correct :)!")
    count += 1
else:
    print("Sorry that is incorrect :(.")
    count -= 1

final_score = count/10 * 100

if final_score >= 80:
    print("You are a Nine Nine Rockstar")
elif final_score >= 70:
    print("Noice! You are close to rockstar status")
elif final_score >= 60:
    print("Nice try! You still need more work to reach rockstar status")
elif final_score >= 50:
    print("Whew! Tough road to rockstar status")
else: 
    print("Do you even watch the show at all?")












