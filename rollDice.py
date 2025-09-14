import random

while True:
    choice = input("Roll the Dice? (y/n): ").lower()
    if choice == 'y':
        playerDie1 = random.randint(1, 6)
        playerDie2 = random.randint(1, 6)
        computerDie1 = random.randint(1, 6)
        computerDie2 = random.randint(1, 6)
        if playerDie1 & playerDie2 > computerDie1 & computerDie2:
            print("You Win")
        elif playerDie1 & playerDie2 < computerDie1 & computerDie2:
            print("You Lose")
        elif playerDie1 & playerDie2 == computerDie1 & computerDie2:
            print("Draw")
        print(f'{playerDie1}, {playerDie2}')
        print(f'{computerDie1}, {computerDie2}')
    elif choice == 'n':
        print("Thanks for playing!")
        break
    else:
        print("Invaild Choice")
