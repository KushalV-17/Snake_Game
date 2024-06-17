from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard



screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake=Snake()
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

food=Food()
score=ScoreBoard()

screen.update()
gameIsOn=True
while(gameIsOn):
    screen.update()
    time.sleep(0.1)
    snake.move()

    #detect food collision
    if snake.head.distance(food) <15:
        food.refresh()
        snake.extend()
        score.increseScore()

    #detect collision with walls
    if snake.head.xcor()>290 or snake.head.xcor()<-290 or snake.head.ycor()<-290 or snake.head.ycor()> 290:
        gameIsOn=False
        score.game_over()

    #Detect tail collision
    for segment in snake.segments[1:]:
        if snake.head.distance(segment)<10:
            gameIsOn=False
            score.game_over()


    
        


screen.exitonclick()


