# sea battle 1d
# 5 positions to check for boot
# random number generator for position boot
# while loop for guessing
# option display guess positions

import random

# boot position generator
random_number = random.randint(0, 4)
position_boot = [0, 0, 0, 0, 0]
position_boot[random_number] = 1
print(position_boot) # is for debug

# hit display
bam_hit = """
        ||||||||||||
       ||888**888888||
      ||8888*8888888*888||
        ||8888*88*88*888||
           |88**8888|
            |88*88*8|
           |888*88|
            || ||    
        \************/
\033[1m BAM \033[0m    \**********/    its a hit"""

# counter for how many try`s are left
counter = 0

# what gamer must do
print("guess the position of the boat. between  1 and 5:")
# tracking of guessed positions
guessed_position =[1, 2, 3, 4, 5]

while counter < 6:  # after 6 try`s while loop will break
    print(guessed_position)
    guess_position = int(input("make a choise: " )) - 1
    if guess_position > 5:
        print("wrong number")
        continue
    guessed_position[guess_position] = "*"
    if position_boot[guess_position] == 1:
        print(bam_hit)  # show bam
        break
    if position_boot[guess_position] != 1:
            print("you mist, just", (5 - counter), "bom`s left")
    counter = counter + 1
else:
    print("no more ammo")

