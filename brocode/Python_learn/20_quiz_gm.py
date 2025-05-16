# Python quiz game



questions = (("What is the pH of pure water?"),
           ("Which gas is essential for photosynthesis?"),
           ("What is the SI unit of electric current?"), ("Which metal is the best conductor of electricity?"),
           ("What is the chemical symbol for sodium?"))

options = (("a. 5", "b. 7", "c. 9", "d. 11"), 
           ("a. Oxygen","b. Nitrogen", "c. Carbon dioxide", "d. Hydrogen"),
           ("a. Volt", "b. Ohm", "c. Ampere", "d. Watt"),
           ("a. Copper", "b. Silver", "c. Gold", "d. Aluminum"),
           ("a. S", "b. Na", "c. So", "d. Sn"))

answers = ("b", "c", "c", "b", "b")
guesses = []
score = 0
question_number = 0

for question in questions:
    print("---------------------")
    print(question)
    for option in options[question_number]:
        print(option)
    guess = input("Enter (a, b, c, d): ").lower()
    guesses.append(guess)
    if guess == answers[question_number]:
        score += 1
        print("CORRECT")
    else:
        print("WRONG")
        print(f"{answers[question_number]} is the correct answer")
    question_number += 1

print("---------------------")
print("       RESULTS       ")
print("---------------------")

print("answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

percent = int(score / len(questions) * 100)
print(f"Your score is {score}/{len(questions)} ({percent}%)")