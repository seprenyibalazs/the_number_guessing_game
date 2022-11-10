import random


thought = []
numbers = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70,


def think():
    now_think = random.choice(numbers)
    thought.append(now_think)
    print(thought)


def game():
    lives = 0
    choice_level = input("Choose difficulty. Type 'easy' or 'hard'")
    if choice_level == "easy":
        lives += 10
    elif choice_level == "hard":
        lives += 5
    print(lives)


game_round = False
while game_round:
    def ask(thought, lives):

        gamer_gessing = int(input("Make a guess: "))
        if gamer_gessing == thought:
            game_round == True
            print("you win!")

        elif gamer_gessing < thought:

            print("too low")
        elif gamer_gessing > thought:
            print("too hight")


print("Welcome to the Number Guessing Game")
print("I'm thinking a number between 1 to 100")
game()
