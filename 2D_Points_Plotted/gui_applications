from Tkinter import *

class App(Frame):
	def __init__(self, master):
		Frame.__init__(self, master)
		self.button1 = Button(master, text = "MEOW!", \
			fg = "blue", command=self.quit)
		self.button1.pack(side=LEFT)
		self.button2 = Button(master, text = \
			"I am Juan pablo", command=self.say)
		self.button2.pack(side = LEFT)
		self.button3 = Button(master, text = \
			"Polymorphism", bg = "yellow", command = self.meow)
		self.button3.pack(side = BOTTOM)

	def say(self):
		print "Froot Loops!"
	
	def meow(self):
		print ("you clicked me")

window = Tk()
app = App(window)
window.mainloop()
