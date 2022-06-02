import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

# creates a figure with a black background
fig = plt.figure(figsize=(8, 6), facecolor='black')

# adds an axis to the figure
ax = plt.axes(xlim=(0, 2.5), ylim=(-3, 3), frameon=False)

line1, = ax.plot([], [], linewidth=4, markersize=20)
line2, = ax.plot([], [], linewidth=3, markersize=20)
line3, = ax.plot([], [], linewidth=2, markersize=20)
line4, = ax.plot([], [], linewidth=1, markersize=40)


# init called at the beginning, and whenever the animation repeates
# this re-initializes the animation to its original state
def init():
    
    line1.set_data([], [])
    line2.set_data([], [])
    line3.set_data([], [])
    line4.set_data([], [])
    
    line1.set_alpha(0.85)
    line2.set_alpha(0.65)
    line3.set_alpha(0.65)
    line4.set_alpha(0.65)
 
    return line1, line2, line3, line4

# animate is called everytime a new frame needs to be generated
def animate(i):
    
    # initial x, y, time, and offset where i=time and d=offset
    xa = np.linspace(0.5, 2.0, 1000)
    ya = 2 * np.pi * (xa - .01 * i)
    d = .015
    
    # line1 data  (min  max  num)
    x1 = (xa + (xa * 3 * d))
    y1 = np.sin(ya)
    
    # line2 data
    x2 = (x1 + 1 / (x1 * d * i))
    y2 = np.sin(ya) * 0.95

    # line3 data
    x3 = (x2 + 1 / (x2 * d * i))
    y3 = np.sin(ya) * 0.90
    
    # line4 data
    x4 = (x3 + 1 / (x3 * d * i))
    y4 = np.sin(ya) * 0.85

    # the function to adjust color smoothly
    rr = int(abs(35 + (40 * np.sin(i/150))))
    gg = int(abs(105 + (50 * np.sin(i/150))))
    bb = int(abs(175 + (50 * np.sin(i/150))))

    new_color = '#%02X%02X%02X' % (rr, gg, bb)

    line1.set_color(new_color)
    line2.set_color(new_color)
    line3.set_color(new_color)
    line4.set_color(new_color)
    
    # if the gif loop is close to ending, smoothly fade out the 3 extra waves
    if 800 < i <= 1200:
        
        al = 1 - ((i - 800)/400)
        line2.set_alpha(al)
        line3.set_alpha(al)
        line4.set_alpha(al)
        
    line1.set_data(x1, y1)
    line2.set_data(x2, y2)
    line3.set_data(x3, y3)
    line4.set_data(x4, y4)
    
    return line1, line2, line3, line4

# run the animation
anim = FuncAnimation(fig, animate, init_func=init, frames=1200, interval=17, blit=True)

plt.show()
