######################################################################################################################
# Name: Pablo Johnson 
# Date: 4.1.2016
# Description: Code to randomly plot points using the Tkinter Module
######################################################################################################################

from Tkinter import *
from random import randint
from math import sqrt

# the 2D point class
class Point(object):
	# write your code for the point class here (and subsequently remove this comment)
	def __init__(self, x = 0.0, y = 0.0):
		self.x = x
		self.y = y
	
	# getter for x coordinate
	@property
	def x(self):
		return self._x
	
	# setter for x coordinate
	@x.setter
	def x(self, value):
		value = float(value)
		self._x = value
	
	# getter for y coordinate
	@property
	def y(self):
		return self._y
	
	# setter for y coordinate
	@y.setter
	def y(self, value):
		value = float(value)
		self._y = value
	
	# Distance funtion
	def dist(self,other):
		return sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)
	
	# Midpoint function
	def midpt(self, other):
		x1 = ((self.x + other.x) / 2)
		y1 = ((self.y + other.y) / 2)
		return "{}.{})".format(x1,y1)

	# String function
	def __str__(self):
		return "({},{})".format(self.x, self.y)
	

# the coordinate system class: (0,0) is in the top-left corner
# inherits from the Canvas class of Tkinter
class CoordinateSystem(Canvas):
	# write your code for the coordinate system class here (and subsequently remove this comment)
	# define init, inherit from master
	def __init__(self, master):
		# We want to use a canvas on which to plot points, using a white background
		Canvas.__init__(self,master, bg="white")
		
		# we want the canvas to fill the window completely
		self.pack(fill=BOTH, expand=1)

	def plotPoints(self, n):
		for i in range(n):
			x = randint(0, WIDTH - 1)
			y = randint(0, HEIGHT - 1)
			self.plot(x, y)

	def plot(self, x, y):
		color = COLORS[randint(0, len(COLORS) - 1)]
		self.create_oval(x, y, x + POINT_RADIUS * 2,\
			y + POINT_RADIUS * 2, outline=color)

	

##########################################################
# ***DO NOT MODIFY OR REMOVE ANYTHING BELOW THIS POINT!***
# the default size of the canvas is 400x400
WIDTH = 400
HEIGHT = 400
# the default point radius is 0 pixels (i.e., no center to the oval)
POINT_RADIUS = 0
# colors to choose from when plotting points
COLORS = [ "black", "red", "green", "blue", "cyan", "yellow", "magenta" ]
# the number of points to plot
NUM_POINTS = 2500

# create the window
window = Tk()
window.geometry("{}x{}".format(WIDTH, HEIGHT))
window.title("2D Points...Plotted")
# create the coordinate system as a Tkinter canvas inside the window
s = CoordinateSystem(window)
# plot some random points
s.plotPoints(NUM_POINTS)
# wait for the window to close
window.mainloop()
