# Import the functions from the Draw 2-D library
# so that they can be used in this program.
import turtle as t
# t.Screen().bgcolor("lightblue")
# t.Screen().screensize(500,500)
# t.Screen().setworldcoordinates(-300,300,300,900)
# t.Screen().tracer(0,0)

from draw2d import \
    start_drawing, draw_line, draw_oval, draw_arc, \
    draw_rectangle, draw_polygon, draw_text, finish_drawing


def main():
    # Width and height of the scene in pixels
    scene_width = 800
    scene_height = 500

    # Call the start_drawing function in the draw2d.py
    # library which will open a window and create a canvas.
    canvas = start_drawing("Scene", scene_width, scene_height)

    # Call your drawing functions such
    # as draw_sky and draw_ground here.

    draw_sky(canvas, scene_width, scene_height)
    draw_ground(canvas, scene_width, scene_height)

    # Call the finish_drawing function
    # in the draw2d.py library.
    finish_drawing(canvas)

def filled_circle(radius, color):
    t.color(color,color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()
    
# Define your functions such as
# draw_sky and draw_ground here.
def draw_sky(canvas, scene_width, scene_height):    
    draw_rectangle(canvas, 0, scene_height / 3,
    scene_width, scene_height, width=0, fill="sky blue")

    # draw the clouds
    draw_cloud(canvas, 400, 400)
    draw_cloud(canvas, 300, 300)

    #draw the sun
    draw_sun(canvas, 500, 150)

def draw_ground(canvas, scene_width, scene_height):    
    draw_rectangle(canvas, 0, 0,
        scene_width, scene_height / 3, width=0, fill="darkGreen")

def draw_cloud(canvas, x, y):
    diameter = 60
    space = 10
    interval = diameter + space

    for i in range(4):
        draw_oval(canvas, x, y, x + diameter, y + diameter, fill="ghostWhite", outline="")
        x += interval

def rainbow(radius=200,interval=10):
    roygbiv=['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet', 'lightblue']

    for r_color in roygbiv:
        filled_circle(radius,r_color)
        radius -= interval

        # Move turtle a up by a little
        t.left(90)
        t.forward(interval)
        t.right(90)

def draw_sun(canvas, x, y):
    diameter = 60
    draw_oval(canvas, x, y, x + diameter, y + diameter, fill="yellow2", outline="")

# Call the main function so that
# this program will start executing.
main()