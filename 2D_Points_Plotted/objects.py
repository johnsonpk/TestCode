class Shape(object):
	def __init__(self, l=1, w=1):
		self.length = l
		self.width = w
	
	def draw(self):
		for i in range(self.width):
			print "* " * self.length


class Rectange(Shape):
	def __init__(self, l, w):
		Shape.__init__(self,l,w)

class Square(Shape):
	def __init__(self,l):
		Shape.__init__(self,l,l)

square1 = Square(3)
square1.draw()
print
rec1 = Rectange(9, 4)
rec1.draw()
