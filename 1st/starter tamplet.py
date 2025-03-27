#Import the Turtlr Graphics Module
import turtle
#Define program constants
WIDTH = 500
HEIGHT = 500

#Create a window where we will do our drawing.
screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT) #Set the dimensions of the Turtle Graphics Window
screen.title("Snake Game in Python")
screen.bgcolor("black")

# Create a turtle to do your bidding
my_turtle = turtle.Turtle()
my_turtle.shape("turtle")
my_turtle.color("red")

# Your turtle awaits your command
my_turtle.forward(100)  # Sample Command

# This statement (or an equivalent) is needed at the end of all your turtle programs.
turtle.done()