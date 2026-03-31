import random

TARGET_SCORE = 50

def roll_dice():
    return random.randint(1, 6)

def player_turn():
    turn_score = 0
    while True:
        print("\n🎲 Your Turn")
        print("Current turn score:", turn_score)

        choice = input("Roll or Hold? (r/h): ").lower()

        if choice == 'r':
            dice = roll_dice()
            print("You rolled:", dice)

            if dice == 1:
                print("💥 You got 1! Turn over, no points added.")
                return 0
            else:
                turn_score += dice
        elif choice == 'h':
            print("You chose to hold.")
            return turn_score
        else:
            print("❌ Invalid choice!")

def computer_turn():
    turn_score = 0
    print("\n🤖 Computer's Turn")

    while turn_score < 15:  
        dice = roll_dice()
        print("Computer rolled:", dice)

        if dice == 1:
            print("💥 Computer got 1! No points.")
            return 0
        else:
            turn_score += dice

    print("Computer holds with", turn_score)
    return turn_score

def play_game():
    player_score = 0
    computer_score = 0

    while player_score < TARGET_SCORE and computer_score < TARGET_SCORE:
        print("\n==============================")
        print("Your Score:", player_score)
        print("Computer Score:", computer_score)
        player_score += player_turn()
        if player_score >= TARGET_SCORE:
            break
        computer_score += computer_turn()
    print("\n🏁 GAME OVER")
    print("Final Score - You:", player_score, "| Computer:", computer_score)

    if player_score > computer_score:
        print("🎉 You Win!")
    else:
        print("🤖 Computer Wins!")

def main():
    print("🎲 Welcome to Dice Game (Player vs Computer)")

    while True:
        play_game()
        again = input("\nPlay again? (yes/no): ").lower()
        if again != "yes":
            print("👋 Thanks for playing!")
            break

main()
