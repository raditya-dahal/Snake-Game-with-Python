# Import the Turtle Graphics module
import turtle
import random

# Define program constants
WIDTH = 500
HEIGHT = 500
DELAY = 100  # milliseconds
FOOD_SIZE = 10

offsets = {
    "up": (0, 20),
    "down": (0, -20),
    "left": (-20, 0),
    "right": (20, 0)
}

def bind_direction_keys():
    screen.onkey(lambda: set_snake_dir("up"), "Up")
    screen.onkey(lambda: set_snake_dir("down"), "Down")
    screen.onkey(lambda: set_snake_dir("left"), "Left")
    screen.onkey(lambda: set_snake_dir("right"), "Right")

def set_snake_dir(direction):
    global snake_dir
    if direction == "up":

        if snake_dir != "down":
            snake_dir = "up"
    elif direction == "down":
        if snake_dir != "up":
            snake_dir = "down"
    elif direction == "left":
        if snake_dir != "right":
            snake_dir = "left"
    elif direction == "right":
        if snake_dir != "left":
            snake_dir = "right"


def game_loop():
    stamper.clearstamps()

    new_head = snake[-1].copy()
    new_head[0] += offsets[snake_dir][0]
    new_head[1] += offsets[snake_dir][1]

    # Check collisions
    if new_head in snake or new_head[0] < - WIDTH / 2 or new_head[0] > WIDTH / 2 \
        or new_head[1] < - HEIGHT / 2 or new_head[1] > HEIGHT / 2:
        reset()
    else:
        # Add new head
        snake.append(new_head)

        # Check food collision
        if not food_collision():
            # Remove last segment
            snake.pop(0)

        # Draw snake for the first time
        for s in snake:
            stamper.goto(s[0], s[1])
            stamper.stamp()

        # refresh screen
        screen.title(f"Snake Game, Score: {score}")
        screen.update()

        # call func each DELAY time
        turtle.ontimer(game_loop, DELAY)

def food_collision():
    global food_pos, score
    if get_distance(snake[-1], food_pos) < 20:
        score += 1
        food_pos = get_random_food_pos()
        food.goto(food_pos)
        return True
    return False

def get_random_food_pos():
    x = random.randint(- WIDTH / 2 + FOOD_SIZE, WIDTH / 2 - FOOD_SIZE)
    y = random.randint(- HEIGHT / 2 + FOOD_SIZE, HEIGHT / 2 - FOOD_SIZE)
    return (x, y)

def get_distance(pos1, pos2):
    x1, y1 = pos1
    x2, y2 = pos2
    distance = ((y2 - y1) ** 2 + (x2 - x1) ** 2) ** 0.5  # Pythagotas' Theorem
    return distance

def reset():
    global score, snake, snake_dir, food_pos
    score = 0
    snake = [[0, 0], [20, 0], [40, 0], [60, 0]]
    snake_dir = "up"
    food_pos = get_random_food_pos()
    food.goto(food_pos)
    game_loop()

# Create a window where we will do our drawing.
screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)  # Set the dimensions of the Turtle Graphics window.
screen.title("Snake")
screen.bgcolor("pink")
screen.tracer(0)  # turn off automatic animation

# Event handlers
screen.listen()
bind_direction_keys()

# Create a turtle to do your bidding
stamper = turtle.Turtle()
stamper.shape("square")
stamper.penup()


# Food
food = turtle.Turtle()
food.shape("circle")
food.color("red")
food.shapesize(FOOD_SIZE / 20)
food.penup()
food_pos = get_random_food_pos()
food.goto(food_pos)

# Your turtle awaits your command
reset()

# This statement (or an equivalent) is needed at the end of all your turtle programs.
turtle.done()