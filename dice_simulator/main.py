#simulate rolling a pair of dice 
import random

def roll_dice():
    
    dice_drawing = {
        1:(
            "|-------------|",
            "|             |",
            "|      0      |",
            "|             |",
            "|-------------|",
            
            ),
        2:(
            "|-------------|",
            "|    0        |",
            "|             |",
            "|        0    |",
            "|-------------|",
            
            ),
        3:(
            "|-------------|",
            "|   0         |",
            "|      0      |",
            "|        0    |",
            "|-------------|",
            
            ),
        4:(
            "|-------------|",
            "|  0      0   |",
            "|             |",
            "|  0      0   |",
            "|-------------|",
            
            ),
        5:(
            "|-------------|",
            "|  0       0  |",
            "|      0      |",
            "|  0       0  |",
            "|-------------|",
            
            ),
        6:(
            "|-------------|",
            "|  0   0   0  |",
            "|  0   0   0  |",
            "|  0   0   0  |",
            "|-------------|",
            
            )
    }
    
    
    roll = input("Roll Dice(yes/no): ")
    
    while roll.lower() == "Yes".lower() or roll == 'y' or roll == 'Y':
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)
        
        print("dice rolled: {} and {}\n".format(dice1,dice2))
        
        print("\n".join(dice_drawing[dice1]))
        print("\n".join(dice_drawing[dice2]))
        
        roll = input("Roll Again(yes/no): ")


def main():
    roll_dice()

main()