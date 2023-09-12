print("----------------------")
print("   WELCOME TO QUIZ !!!   ")
print("----------------------")

questions = ("How many Bits are in a Single-Byte?: ",
                       "What was the Code Name for Windows Vista?: ",
                       "What Type of Format is HTML?: ",
                       "Which Technology is used in a CD Drive: ",
                       "What is the Name of the First Microprocessor: ")

options = (("A. 11", "B. 7", "C. 8", "D. 9"),
                   ("A.  Longhorn", "B. Daytona", "C. Razzle", "D. Janus"),
                   ("A. Document Text Format", "B. Document File Format", "C. Document Format", "D. Document read Format"),
                   ("A. optic mirror", "B. optical lence", "C. optical fiber", "D. Optical Laser"),
                   ("A. Intel 4004", "B. 8088", "C. 8081", "D. Intel 8085"))

answers = ("C", "A", "B", "D", "A")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("----------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT!")
    else:
        print("INCORRECT!")
        print(f"{answers[question_num]} is the correct answer")
    question_num += 1
    print("----------------------")
print("       RESULTS        ")
print("----------------------")

print("answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score / len(questions) * 100)
print(f"Your score is: {score}%")