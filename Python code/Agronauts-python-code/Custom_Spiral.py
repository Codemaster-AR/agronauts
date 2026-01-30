import os
import time
import turtle

def clear_terminal():
    """Clears the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def custom_spiral():
    try:
        print("Welcome to the Custom Spiral Drawer!")
        time.sleep(1)
        ans_1 = int(input("Angle: "))
        ans_2 = int(input("Speed: "))
        ans_3 = str(input("Shape (turtle/circle/square/triangle):"))

        print ("Now you will choose 6 colours.")
        color_1 = str(input("1st colour: "))
        color_2 = str(input("2nd colour: "))
        color_3 = str(input("3rd colour: "))
        color_4 = str(input("4th colour: "))
        color_5 = str(input("5th colour: "))
        color_6 = str(input("6th colour: "))
        print ("Check your new spiral window!")
        time.sleep(1)

        # Turtle setup #
        screen = turtle.Screen()
        a = turtle.Turtle()
        colors = [color_1, color_2, color_3, color_4, color_5, color_6]
        for x in range(360):
            a.pencolor(colors[x % 6])
            a.forward(x)
            a.left(ans_1)
            a.speed(ans_2)
            a.shape(ans_3)
        turtle.done()
        return 
    except Exception as e:
        print("An error occurred:", e)
        print("Check spelling and extra spaces, then try again.")
        return
    return
# Run the custom spiral function
clear_terminal() #Clear the terminal 
custom_spiral() # Start the spiral drawing process after asking user.