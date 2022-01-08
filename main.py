from turtle import Screen
from snake import Snake
from food import Food
from score import ScoreBoard

# sets up screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)


def replay():
    re_play = screen.textinput("Game Over", "Play Again? \n\nYes or No ").lower()
    if re_play == "y" or replay == "yes":
        screen.reset()
        score_board.save_high_score()
        score_board.new_game()
        snake.new_snake(screen)
        food.reset_pos()


    else:
        score_board.save_high_score()
        screen.bye()


snake = Snake(screen)
food = Food()
score_board = ScoreBoard()

game_is_on = True
while game_is_on:
    snake.set_speed(score_board.score)
    screen.onkey(snake.up, "w")
    screen.onkey(snake.left, "a")
    screen.onkey(snake.down, "s")
    screen.onkey(snake.right, "d")
    snake.move()
    snake.hit_tail(replay)
    screen.update()

    if snake.head.distance(food) < 15:
        snake.new_tail()
        food.reset_pos()
        score_board.add()

    if snake.head.xcor() >= 300 or snake.head.xcor() <= -300\
            or snake.head.ycor() >= 300 or snake.head.ycor() <= -300:
        replay()

    screen.listen()
screen.exitonclick()


