'''
Programmer: Baadshah Verma

This program draws a cartesian plane using tkinter and plots different
mathematical functions on the plane.

'''

from tkinter import *
from math import *

CANV_WIDTH = 750
CANV_HEIGHT = 250

def draw_axes(scale, tick_length):
    """Draws a horizontal line across the middle of the canvas, and a vertical
    line down the centre of the canvas using tkinter's default line thickness
    and colour.
    """
    # Draw the x axis
    width = w.winfo_width()
    w.create_line(get_x(-width//2),get_y(0),get_x(width//2),get_y(0))
    
    # Draw the y axis
    height = w.winfo_height()
    w.create_line(get_x(0),get_y(-height//2),get_x(0),get_y(height//2))

    #ticks on x axis
    for i in range(get_x(-width), get_x(width+1), scale):
        w.create_line(get_x(i), get_y(0), get_x(i), get_y(-1 * tick_length))

    #ticks on y axis
    for i in range(get_y(height), get_y(-height+1), scale):
        w.create_line(get_x(0), get_y(i), get_x(-1*tick_length), get_y(i))

def get_x(x_val):
    """Maps a Cartesian-style x coordinate (where x is 0 at the window's
    horizontal centre) onto the tkinter canvas (where x is 0 is at the left
    edge). x_val is the Cartesian x coordinate. The units of measurerment
    are pixels.
    """

    #converts the coordinates and returns x coordinate
    width = w.winfo_width()
    x = x_val + (width//2)
    return x   

def get_y(y_val):
    """Maps a Cartesian-style y coordinate (where y is 0 at the window's
    vertical centre, and in which y grows in value upwards) onto the tkinter
    canvas (where y is 0 is at the top edge, and y grows in value downwards).
    y_val is the Cartesian y coordinate. The returned value is the
    corresponding tkinter canvas x coordinate. The units of measurerment are
    pixels.
    """

    #converts the coordinates and returns the y coordinate
    height = w.winfo_height()
    y = y_val - (height//2)
    return - y   

def plot_point(x,y,colour='red'):
    """Draws a single pixel "dot" at Cartesian coordinates (x,y).
    The optional colour parameter determines the colour of the dot.
    """

    #plots a single dot at (x,y) using create_oval in red
    w.create_oval(get_x(x), get_y(y), get_x(x), get_y(y), outline=colour)

#This acts as the range method, but allows for a step that is a float number
def seq(start, stop, step=1):
    n = int(round((stop - start)/float(step)))
    if n > 1:
        return([start + step*i for i in range(n+1)])
    elif n == 1:
        return([start])
    else:
        return([])

def plot_fn(fn,start_x,end_x,scale=20,colour='black'):

    #runs the start and end values through a for loop, skipping by the scale and plots the function using create_oval
    for i in seq(start_x, end_x + 1, 1/scale):
        w.create_oval(get_x(i*scale), get_y(fn(i)*scale), get_x(i*scale), get_y(fn(i)*scale), outline=colour)
        
    """Plots a function, y = fn(x), onto the canvas.

    Parameters:

    * fn is a function that takes a single number parameter and returns a
      number.
	  
    * start_x is the left-most x value to be passed to fn.

    * end_x is the right-most x value to be passed to fn.
	
    * scale (optional) is used as a multiplier in both the x and y directions
      to "zoom in" on the plot. It is also used to increase the number of x
      coordinates "fed" to the fn function, to fill in all the horizontal gaps
      that would otherwise appear between the plotted points. scale is
      particularly useful for showing detail that would be otherwise be lost.

    * colour (optional) determines the colour of the plotted function.
	
    Note: nothing bad happens if start_x, end_x, or any y value computed from
    fn(x) is off the canvas. Those points simply will not be displayed.
    (Note to the student programmer: This happens automatically. You don't
    have to program it.)
    """
    
def square(x):
    """Returns the square of x"""
    return x * x

def func_1(x):
    """A quadratic polynomial function (for testing)."""
    return -3 * square(x) + 2 * x + 1
    
def func_2(x):
    """Your choice of a function"""
    return x**2 + 3 # replace this line
    
def func_3(x):
    """Your choice of a function"""
    return x ** 3 # replace this line

master = Tk()
master.title('Plot THIS!')
w = Canvas(master,
           width=CANV_WIDTH,
           height=CANV_HEIGHT)
w.pack(expand=YES, fill=BOTH)
w.update() # makes w.winfo_width() and w.winfo_height() meaningful

def main():
    draw_axes(40, 4)
    #draw_axes(40, -4)
    plot_point(0,0)
    plot_fn(sin,-20,20,40,'green') # sin() is defined in the math module
    plot_fn(cos,-20,20,40,'blue')  # cos() is defined in the math module
    plot_fn(square,-20,20,40,'red')
    plot_fn(func_1,-20,20,40,'purple')
    plot_fn(func_2,-20,20,20,'brown') #adjusted scale to show full function
    plot_fn(func_3,-20,20,40,'cyan')
main()

mainloop()
