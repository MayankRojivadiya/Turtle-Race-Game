from turtle import Turtle,Screen
import random

is_on = False
screen = Screen()
screen.setup(width=500, height=500)
user_bet = screen.textinput(title="Make your bet",prompt="Which Turtle will win the race? among red|orange|yellow|green|blue|purple... Enter a color : ")
is_on = True
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_position = [-150, -90, -30, 30, 90, 150]
all_turtle = []

for i in range(0,6):
    timmy = Turtle(shape="turtle")
    timmy.color(colors[i])
    timmy.penup()
    timmy.goto(x=-240, y=y_position[i])
    all_turtle.append(timmy)

if user_bet:
    is_on = True

while is_on:
    for turtle in all_turtle:
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"Congratulation!!! \nYou won the race. Winner is {winning_color}")
            else:
                print(f"Sorry! \nYou lose the race. Winner is {winning_color}")
            is_on = False
        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)

screen.exitonclick()