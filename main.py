from turtle import Screen, Turtle
import time
import snake
import food
from score import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake_segments = snake.create_snake()
food_item = food.Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(lambda: snake.turn_left(snake_segments), "Left")
screen.onkey(lambda: snake.turn_right(snake_segments), "Right")
screen.onkey(lambda: snake.turn_up(snake_segments), "Up")
screen.onkey(lambda: snake.turn_down(snake_segments), "Down")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move_snake(snake_segments)

    if snake_segments[0].distance(food_item) < 15:
        food_item.refresh()
        snake.grow_snake(snake_segments)
        scoreboard.increase_score()

    head = snake_segments[0]
    if abs(head.xcor()) > 290 or abs(head.ycor()) > 290:
        game_is_on = False

    for segment in snake_segments[1:]:
        if head.distance(segment) < 10:
            game_is_on = False
            break

    if not game_is_on:
        scoreboard.game_over()

screen.exitonclick()


















