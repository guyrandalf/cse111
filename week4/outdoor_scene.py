print()
import tkinter as tk
from random import randrange


def main():
    # The width and height of the scene window.
    width = 800
    height = 500

    # Create the Tk root object.
    root = tk.Tk()
    root.geometry(f"{width}x{height}")

    # Create a Frame object.
    frame = tk.Frame(root)
    frame.master.title("Scene")
    frame.pack(fill=tk.BOTH, expand=1)

    # Create a canvas object that will draw into the frame.
    canvas = tk.Canvas(frame)
    canvas.pack(fill=tk.BOTH, expand=1)

    # Call the draw_scene function.
    draw_scene(canvas, 0, 0, width-1, height-1)

    root.mainloop()


def draw_scene(canvas, scene_left, scene_top, scene_right, scene_bottom):
    """Draw a scene in the canvas. scene_left, scene_top,
    scene_right, and scene_bottom contain the extent in
    pixels of the region where the scene should be drawn.
    Parameters
        scene_left: left side of the region; less than scene_right
        scene_top: top of the region; less than scene_bottom
        scene_right: right side of the region
        scene_bottom: bottom of the region
    Return: nothing

    If needed, the width and height of the
    region can be calculated like this:
    scene_width = scene_right - scene_left + 1
    scene_height = scene_bottom - scene_top + 1
    """
    # Call your functions here, such as draw_sky, draw_ground,
    # draw_snowman, draw_tree, draw_shrub, etc.
    tree_center = scene_left + 500
    tree_top = scene_top + 300
    tree_height = 150
    
    draw_sky(canvas)

    draw_ground(canvas)

    draw_clouds(canvas)

    draw_grass(canvas)

    draw_sun(canvas)

    draw_cloud_cluster(canvas)

    draw_pine_tree(canvas, tree_center, tree_top, tree_height)

# Define more functions here, like draw_sky, draw_ground,
# draw_cloud, draw_tree, draw_kite, draw_snowflake, etc.

def draw_sky(canvas):
    canvas.create_rectangle(0, 0, 800, 500, fill="dodgerBlue")

def draw_ground(canvas):
    canvas.create_rectangle(0, 400, 800, 500, fill="tan4")

def draw_clouds(canvas):
    canvas.create_oval(125, 100, 500, 150, outline="ghostWhite", fill="ghostWhite")
    canvas.create_oval(155, 70, 520, 130, outline="ghostWhite", fill="ghostWhite")
    canvas.create_oval(205, 90, 620, 130, outline="ghostWhite", fill="ghostWhite")
    canvas.create_oval(400, 120, 700, 170, outline="ghostWhite", fill="ghostWhite")

def draw_grass(canvas):
    # y1 = randrange(290, 600)
    # y2 = randrange(290, 600)
    # for k in range(0, 800):
    #     x1 = randrange(0, 800)
    #     x2 = randrange(0, 800)
    #     canvas.create_line(x1, y1, x2, y2, fill="dark green", width = 5)
    for i in range(0,4000):
        x1 = randrange(0, 800)
        y1 = randrange(400, 500)
        x2 = randrange(0, 800)
        y2 = randrange(400, 500)
        canvas.create_line(x1, y1, x2, y2, fill="dark green", width = 5)

def draw_sun(canvas):
    canvas.create_oval(10, 10, 60, 60, fill="yellow", outline="yellow")

def draw_pine_tree(canvas, peak_x, peak_y, height):
    """Draw a single pine tree.
    Parameters
        canvas: The tkinter canvas where this
            function will draw a pine tree.
        peak_x, peak_y: The x and y location in pixels where
            this function will draw the top peak of a pine tree.
        height: The height in pixels of the pine tree that
            this function will draw.
    Return: nothing
    """
    trunk_width = height / 10
    trunk_height = height / 8
    trunk_left = peak_x - trunk_width / 2
    trunk_right = peak_x + trunk_width / 2
    trunk_bottom = peak_y + height

    pine_skirt_width = height / 2
    pine_skirt_height = height - trunk_height
    pine_skirt_left = peak_x - pine_skirt_width / 2
    pine_skirt_right = peak_x + pine_skirt_width / 2
    pine_skirt_bottom = peak_y + pine_skirt_height

    # Draw the trunk of the pine tree.
    canvas.create_rectangle(trunk_left, pine_skirt_bottom,
            trunk_right, trunk_bottom,
            outline="gray20", width=1, fill="tan3")

    # Draw the crown (also called pine_skirt) of the pine tree.
    canvas.create_polygon(peak_x, peak_y,
            pine_skirt_right, pine_skirt_bottom,
            pine_skirt_left, pine_skirt_bottom,
            outline="gray20", width=1, fill="green")

def draw_cloud_cluster(canvas):
    for i in range(0,5):
        x1 = randrange(100, 250)
        y1 = randrange(100, 180)
        x2 = randrange(100, 250)
        y2 = randrange(100, 180)
        canvas.create_oval(x1, y1, x2, y2, fill="ghostWhite", outline="ghostWhite")


# Call the main function so that
# this program will start executing.
main()
print()