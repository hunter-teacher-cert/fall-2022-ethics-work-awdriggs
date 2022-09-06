# nim.py 
# Adam Driggers 
# CSCI 77800 Fall 2022
# collaborators: 
# consulted: https://en.wikipedia.org/wiki/Nim

stones = 12
stonesTaken = None 
playing = True

print("Let's play the Game of Nim. There is a bag with 12 stones. Your goal is to take the last one.")
 
while(playing):
    print("%s stones remaining" % stones)
    stonesTaken = int(input("How many stones do you wish to take? Take 1-3 stones: "))

    if stonesTaken > 0 and stonesTaken <= 3 and stonesTaken <= stones:
        stones -= stonesTaken
    else:
        print("Invalid move. Try again")
        continue

    if stones == 0:
        print("You win!")
        playing = False;
        break

    if stones % 4 == 1:
        stonesTaken = 1
    elif stones % 4 == 2:
        stonesTaken = 2
    elif stones % 4 == 3:
        stonesTaken = 3
    else:
        stonesTaken = 1

    print("Computer takes %s stones " % stonesTaken)
    stones -= stonesTaken

    if stones == 0:
        print("Computer wins!")
        playing = False

print("Game Over!")
