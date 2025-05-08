import random

def roll_dice():
    dice_faces = {
        1: ("-------", "|     |", "|  o  |", "|     |", "-------"),
        2: ("-------", "| o   |", "|     |", "|   o |", "-------"),
        3: ("-------", "| o   |", "|  o  |", "|   o |", "-------"),
        4: ("-------", "| o o |", "|     |", "| o o |", "-------"),
        5: ("-------", "| o o |", "|  o  |", "| o o |", "-------"),
        6: ("-------", "| o o |", "| o o |", "| o o |", "-------")
    }
    
    result = random.randint(1, 6)
    print(f"\nYou rolled a {result}!")
    for line in dice_faces[result]:
        print(line)

def main():
    print("🎲 Welcome to the Dice Roller Simulator! 🎲")
    while True:
        roll_dice()
        choice = input("\nRoll again? (y/n): ").lower()
        if choice != 'y':
            print("Thanks for playing! Goodbye.")
            break

# Run the simulator
main()
