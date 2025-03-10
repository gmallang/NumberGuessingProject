def numberguess():
    import art
    import random
    print(art.logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100")
    correct = int(random.randint(1,100))
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

    def easy():
        n = 11
        for i in range(0, 10):
            print(f"You have {n - 1} attempts remaining to guess a number.")
            n -= 1
            guess = int(input("Make a guess: "))
            if guess == correct:
                return (print(f"You got it! The answer was {correct}!"))
            elif guess > correct:
                print("Too high!")
                if n == 1:
                    print(f"Sorry, the answer is {correct}")
            elif guess < correct:
                print("Too low")
                if n == 1:
                    print(f"Sorry, the answer is {correct}")
            elif n == 0:
                print(f"Sorry, the number is {correct}")

    def hard():
        n = 6
        for i in range(0, 5):
            print(f"You have {n - 1} attempts remaining to guess a number.")
            n -= 1
            guess = int(input("Make a guess: "))
            if guess == correct:
                return (print(f"You got it! The answer was {correct}!"))
            elif guess > correct:
                print("Too high!")
                if n == 1:
                    print(f"Sorry, the answer is {correct}")
            elif guess < correct:
                print("Too low")
                if n == 1:
                    print(f"Sorry, the answer is {correct}")


    if difficulty == "easy":
        easy()
    elif difficulty == "hard":
        hard()
numberguess()
again = input("Do you want to play again? (yes or no): ").lower()
if again == "yes":
    print("\n" * 20)
    numberguess()
else:
    print("Thank you for playing")
