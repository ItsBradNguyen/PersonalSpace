Mystery_Word = "Flabbergasted"
User_Guess = ""
User_GuessCount = 0
Max_GuessCount = 5
Out_Of_Guesses = False

while User_Guess != Mystery_Word and not Out_Of_Guesses:
    if User_GuessCount < Max_GuessCount:
        User_Guess = input("Please enter your guess: ")
        User_GuessCount += 1
    else:
        Out_Of_Guesses = True

if not Out_Of_Guesses:
    print("You have guessed correctly with " + str(User_GuessCount) + " attempts! Congratulations!")
else:
    print("You have run out of guesses! Better luck next time!")