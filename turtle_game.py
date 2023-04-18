# import turtle module
import turtle
# Import the random module
from random import randint
# Import the sleep function from the time module
from time import sleep
# Import Console for console text printing
from rich.console import Console
# Import Panel for title displays
from rich.panel import Panel

# Range of random numbers
MAX = 6
MIN = 1



# Title and color your drawing window, ie race arena
turtle.title("The Great Turtle Race")
turtle.bgcolor("lavender")

# Call this to be able to change the titlebar icon (like tkinter)
root = turtle.Screen()._root
root.iconbitmap("turtle.ico")

# Initialize rich.console
console = Console()

# TODO Print title
console.print(
    Panel.fit(
    " The Great Turtle Race ",
    style="purple",
    subtitle="By J. F. R. III")          # This is my artist name
)
print()

# Create your turtles
player_one = turtle.Turtle()
player_one.color("light blue")
player_one.pencolor("navy")
player_one.shape("turtle")
player_one.penup()
player_one.goto(-200, 100)
player_one.pensize(5)

player_two = player_one.clone()
player_two.color("purple")
player_two.penup()
player_two.goto(-200,-100)
player_two.pensize(5)

# Create you turtles' homes
player_one.goto(300, 60)
player_one.pendown()
player_one.circle(40)
player_one.penup()
player_one.goto(-200, 100)

player_two.goto(300, -140)
player_two.pendown()
player_two.circle(40)
player_two.penup()
player_two.goto(-200, -100)

print("First turtle to make it home wins!\n")
# Start loop for gameplay
for i in range(20):
    if player_one.pos() >= (280, 100):
        console.print("\n[bold blue]Player One[/bold blue] Wins!")
        break
    elif player_two.pos() >= (280, -100):
        console.print("\n[dark_magenta]Player Two[/dark_magenta] Wins!")
        break
    else: 
        # Have player 1 roll
        player_one_turn = console.input(f"[bold blue]Player One[/bold blue], press 'Enter' to roll the die: ")
        die_outcome = randint(MIN, MAX)
        print("The result of the die roll is: ")
        # Use sleep function to create hardly bearable suspense
        sleep(2.5)
        console.print(f"[red]{die_outcome}[/red]")
        print("Move forward: ")
        console.print(f"[red]{30*die_outcome}[/red] steps.")
        sleep(2.5)
        player_one.fd(30*die_outcome)
        
        # Check if player 1 has 'broken the plane', in NFL parlance
        if player_one.pos() >= (280, 100):
            console.print("\n[bold blue]Player One[/bold blue] Wins!")
            break
        else: 
            # If not, give player 2 a turn
            player_two_turn = console.input("[dark_magenta]\nPlayer Two[/dark_magenta], press 'Enter' to roll the die: ")
            die_outcome = randint(MIN, MAX)
            print("The result of the die roll is: ")
            sleep(2.5)
            console.print(f"[red]{die_outcome}[/red]")
            print("Move forward: ")
            console.print(f"[red]{30*die_outcome}[/red] steps.\n")
            sleep(2.5)
            player_two.fd(30*die_outcome)