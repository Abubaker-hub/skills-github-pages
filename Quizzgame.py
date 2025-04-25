print("Let's see kon banega keror pati")
Ask = input("Do you want to play the game? (yes/no): ")


if Ask == "yes":
    print("Let's start the game: ")
else:
    print("bye")


question1 = "When did Pakistan gain independence from India and the British?"
question2 = "Who is the current prime minister of Pakistan?"
question3 = "Who is the captain of the Pakistan cricket team?"

options1 = "A: 1947  B: 1948  C: 1944  D: 1949"
options2 = "A: Imran Khan  B: Benazir Bhutto  C: Shehbaz Sharif  D: Rifat Ishaq Khan"
options3 = "A: Sarfaraz Ahmed  B: Shahid Afridi  C: Mohammad Shami  D: Babar Azam"

correct_answers = {"1": "A", "2": "C", "3": "D"}

print(question1)
print(options1)
answer1 = input("Enter your answer (A/B/C/D): ").strip().upper()
if answer1 == correct_answers["1"]:
    print("Correct!")
else:
    print("Wrong!")

print(question2)
print(options2)
answer2 = input("Enter your answer (A/B/C/D): ").strip().upper()
if answer2 == correct_answers["2"]:
    print("Correct!")
else:
    print("Wrong!")

print(question3)
print(options3)
answer3 = input("Enter your answer (A/B/C/D): ").strip().upper()
if answer3 == correct_answers["3"]:
    print("Correct!")
else:
    print("Wrong!")
