#Snake Water Game
import random
import emoji
Computer=random.choice([-1,1,0])
your_turn=input("Enter your choice: ")
choice={"SNAKE":1,"WATER":-1,"GUN":0}
reverseDict={1:"SNAKE",-1:"WATER",0:"GUN"}
You=choice[your_turn]
print(f"Computer choice is {reverseDict[Computer]}\nYour Choice is {reverseDict[You]}")
if(Computer==You):
    print(emoji.emojize("It's a Draw:repeat:",language="alias"))
elif(Computer==-1 and You==0):
    print(emoji.emojize("You Lose:cry:",language="alias"))
elif (Computer == -1 and You==1):
    print(emoji.emojize("CONGRATS!! You Won the Game:snake:,:droplet::gun:,",language="alias"))
elif (Computer == 1 and You == -1):
    print(emoji.emojize("You Lose:cry:",language="alias"))
elif (Computer == 1 and You == 0):
    print(emoji.emojize("CONGRATS!! You Won the Game:snake::droplet::gun:",language="alias"))
elif (Computer == 0 and You == -1):
    print(emoji.emojize("CONGRATS!! You Won the Game:snake:,:droplet::gun:,",language="alias"))
elif(Computer==0 and You==1):
    print(emoji.emojize("You Lose:cry:",language="alias"))
else:
    print("Try again")
