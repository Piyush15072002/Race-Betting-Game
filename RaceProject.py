# In this project, there will be a turtle race and the user will have to bet on which turtle will win
import random
from turtle import Turtle, Screen
from Assets import allTurtles, colors, startingPostionX, startingPostionY
screen = Screen()
screen.bgcolor("black")

# setting up screen dimensions

screen.setup(width=500, height=400)

# Coordinates details - Since the height and width is defined so if the center is (0,0) then,
# x = 500/2 = 250
# y = 400/2 = 200
# This will help us to move the turtle

# Race
isRace = False

# To draw the finish line
FinishLine = Turtle()
FinishLine.hideturtle()
FinishLine.color("red")
FinishLine.penup()  
FinishLine.goto(230, 120)   # Understand the coordinates of the screen first
FinishLine.pendown()
FinishLine.pensize(5)
FinishLine.right(90)
FinishLine.goto(230,-120)


# taking input from user about the turtle betting

userName = screen.textinput(title="Let's know you!", prompt="What's your name? ")
userBet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? (Enter the color : orange, green, blue, yellow, violet) : ").lower()

print(f'{userName} has bet on the {userBet} turtle.')



for index in range(0,5):    # for 5 turtles
    dbz = Turtle(shape="turtle")
    dbz.color(colors[index])
    dbz.penup()
    dbz.goto(x = -230, y = startingPostionY[index])
    allTurtles.append(dbz)  # new turtle added to list


# after user have entered, we will toggle isRace
# if userBet:
#     isRace = True
if((userBet == "orange") or (userBet == "blue") or (userBet == "green") or (userBet == "yellow") or (userBet == "violet")):
    isRace = True
else:
    print("Please enter correct color for betting!")



# starting race


while isRace:
    # Each turtle can have random pace from 0 to 10
    for turtle in allTurtles:
        # we need a stopping condition also
        if turtle.xcor() >  230:
            isRace = False  # Ending race
            winnerTurtle = turtle.pencolor()  # turtle body color, not path color
            if(userBet.lower() == winnerTurtle.lower()):
                print(f"Congratulations, Your {winnerTurtle} turtle won!!!")
            else:
                print(f"You lost the bet! The {winnerTurtle} turtle won!!!")

        randomDistance = random.randint(0,10)
        turtle.forward(randomDistance)







screen.exitonclick()