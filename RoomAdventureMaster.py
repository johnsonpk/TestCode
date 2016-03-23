######################################################################
# Name:Matthew Louque
# Date:2/05/2016
# Description:Room adventure text based game
######################################################################
######################################################################
#import the time library
import time
#blueprint for a room
#the room class
class Room(object):
	#constructor
	def __init__(self, name): 
		#rooms have a name, exits (ex south), exit locations
		#ex to the south is room n, items (ex table), 
		#item descriptions (for each item, and grabbables (things that can be taken into inventory)
		self.name = name
		self.exits = []
		self.exitLocations = []
		self.items = []
		self.itemDescriptions= []
		self.grabbables = []
		self.grabbablesDescriptions = []
		self.itemOriginalDescriptions = []
	
	#getters and setters
	#getter
	@property
	def name(self):
		return self._name
	
	#setter
	@name.setter
	def name(self, value):
		self._name = value
	
	@property
	def exits(self):
		return self._exits
	
	@exits.setter
	def exits(self, value):
		self._exits = value
	
	@property
	def exitLocations(self):
		return self._exitLocations
	
	@exitLocations.setter
	def exitLocations(self, value):
		self._exitLocations = value
		
	@property
	def items(self):
		return self._items
		
	@items.setter
	def items(self, value):
		self._items = value
		
	@property
	def itemDescriptions(self):
		return self._itemDescriptions
		
	@itemDescriptions.setter
	def itemDescriptions(self, value):
		self._itemDescriptions = value
		
	@property
	def grabbables(self):
		return self._grabbables
	
	@grabbables.setter
	def grabbables(self, value):
		self._grabbables = value

	@property
	def grabbablesDescriptions(self):
		return self._grabbablesDescriptions
		
	@grabbablesDescriptions.setter
	def grabbablesDescriptions(self, value):
		self._grabbablesDescriptions = value
		
	@property
	def itemOriginalDescriptions(self):
		return self._itemOriginalDescriptions
		
	@itemOriginalDescriptions.setter
	def itemOriginalDescriptions(self, value):
		self._itemOriginalDescriptions = value
		
	# adds an exit to the room
	# the exit is a string (e.g., north)
	# the room is an instance of a room	
	def addExit(self, exit, room):
		self._exits.append(exit)
		self._exitLocations.append(room)
	
	def addItem (self, name, desc, grab = ""):
		self._items.append(name)
		self._itemOriginalDescriptions.append(desc)
		if (grab != ""):
			desc = desc + " There is a {}".format(grab) + " on the {}".format(name)
		self.itemDescriptions.append(desc)
		
	#adds a grabbable to the room, appends to list
	def addGrabbable(self, item, description = ""):
		self._grabbables.append(item)
		self.grabbablesDescriptions.append(description)
		
	# Deletes grabbable, removes grabbable description, fixes item description
	def delGrabbable(self, item):
		# Saves index of grabbable to i
		i = self._grabbables.index(item)
		# removes grabbable and grabbable description from proper lists
		self._grabbables.remove(item)
		del self._grabbablesDescriptions[i]
		# Iterate through itemDescriptions, looking for grabbable. If found, revert item to description
			# that is without the grabbable. 
		for a1 in self._itemDescriptions:
			if (item in a1):
				i = self._itemDescriptions.index(a1)
				self._itemDescriptions[i] = self._itemOriginalDescriptions[i]
				break
	
	#prints a string description of the room	
	def __str__(self):
		#the room name
		s = "You are in {}.\n".format(self.name)
		
		#items in room
		s += "You see: "
		for item in self.items:
			s += item + " "
		s += "\n"
		
		#exits from room
		s += "Exits: "
		for exit in self.exits:
			s += exit + " "
		return s
	
#no longer in class
#**************************************
#**************************************
#**************************************
#**************************************


# displays an appropriate "message" when the player dies
# yes, this is intentionally obfuscated!
def death():
	print " " * 17 + "u" * 7
	print " " * 13 + "u" * 2 + "$" * 11 + "u" * 2
	print " " * 10 + "u" * 2 + "$" * 17 + "u" * 2
	print " " * 9 + "u" + "$" * 21 + "u"
	print " " * 8 + "u" + "$" * 23 + "u"
	print " " * 7 + "u" + "$" * 25 + "u"
	print " " * 7 + "u" + "$" * 25 + "u"
	print " " * 7 + "u" + "$" * 6 + "\"" + " " * 3 + "\"" + "$" * 3 +"\"" + " " * 3 + "\"" + "$" * 6 + "u"
	print " " * 7 + "\"" + "$" * 4 + "\"" + " " * 6 + "u$u" + " " * 7+ "$" * 4 + "\""
	print " " * 8 + "$" * 3 + "u" + " " * 7 + "u$u" + " " * 7 + "u" +"$" * 3
	print " " * 8 + "$" * 3 + "u" + " " * 6 + "u" + "$" * 3 + "u" + "" * 6 + "u" + "$" * 3
	print " " * 9 + "\"" + "$" * 4 + "u" * 2 + "$" * 3 + " " * 3 +"$" * 3 + "u" * 2 + "$" * 4 + "\""
	print " " * 10 + "\"" + "$" * 7 + "\"" + " " * 3 + "\"" + "$" * 7+ "\""
	print " " * 12 + "u" + "$" * 7 + "u" + "$" * 7 + "u"
	print " " * 13 + "u$\"$\"$\"$\"$\"$\"$u"
	print " " * 2 + "u" * 3 + " " * 8 + "$" * 2 + "u$ $ $ $ $u" + "$"* 2 + " " * 7 + "u" * 3
	print " u" + "$" * 4 + " " * 8 + "$" * 5 + "u$u$u" + "$" * 3 + "" * 7 + "u" + "$" * 4
	print " " * 2 + "$" * 5 + "u" * 2 + " " * 6 + "\"" + "$" * 9 +"\"" + " " * 5 + "u" * 2 + "$" * 6
	print "u" + "$" * 11 + "u" * 2 + " " * 4 + "\"" * 5 + " " * 4 +"u" * 4 + "$" * 10
	print "$" * 4 + "\"" * 3 + "$" * 10 + "u" * 3 + " " * 3 + "u" * 2+ "$" * 9 + "\"" * 3 + "$" * 3 + "\""
	print " " + "\"" * 3 + " " * 6 + "\"" * 2 + "$" * 11 + "u" * 2 +" " + "\"" * 2 + "$" + "\"" * 3
	print " " * 11 + "u" * 4 + " \"\"" + "$" * 10 + "u" * 3
	print " " * 2 + "u" + "$" * 3 + "u" * 3 + "$" * 9 + "u" * 2 +" \"\"" + "$" * 11 + "u" * 3 + "$" * 3
	print " " * 2 + "$" * 10 + "\"" * 4 + " " * 11 + "\"\"" + "$" *11 + "\""
	print " " * 3 + "\"" + "$" * 5 + "\"" + " " * 22 + "\"\"" + "$" *4 + "\"\""
	print " " * 5 + "$" * 3 + "\"" + " " * 25 + "$" * 4 + "\""



#creates the rooms
def createRooms():
	global currentRoom
	
	courtyard = Room("Courtyard")
	great_hall = Room("Great Hall")
	west_wing_parlor = Room("West Wing Parlor")
	study = Room("Study")
	laboratory = Room("Laboratory")
	east_wing_parlor = Room("East Wing Parlor")
	dining_hall = Room("Dining Hall")
	kitchen = Room("Kitchen")
	upstairs_BallRoom = Room("BallRoom")
	
	# Courtyard Room Information
	courtyard.addExit("north", great_hall)
	courtyard.addItem("Fountain", "The lady of the mist welcomes you.")
	courtyard.addItem("FrontDoor", "It is a wooden door entrance to the Great Hall.")
	courtyard.addItem("Hedges", "They are overgrown.")
	
	# Great Hall Room Information
	great_hall.addExit("west", west_wing_parlor)
	great_hall.addExit("east", east_wing_parlor)
	great_hall.addExit("up", upstairs_BallRoom)
	great_hall.addItem("Statue", "WATTTT")
	great_hall.addItem("StairCase", "You can go down to the basement but you need all the keys. You can also go upstairs.")
	great_hall.addItem("Chandelier", "WATTTT")
	
	#great_hall.addExit("south", courtyard) 	# DOOR SHUTS BEHIND YOU AS YOU ENTER
	
	
	upstairs_BallRoom.addExit("down", great_hall)
	upstairs_BallRoom.addItem("DanceFloor", "The Dancefloor is empty. You can tell many nobles have danced on this floor.")
	upstairs_BallRoom.addItem("DiscoBall", "You can see the dust that has built up on it. This thing hasn't been used since the '80s")
	upstairs_BallRoom.addItem("DjBooth", "You see DJ Khaled's logo on the booth. The booth is covered in piles of \"jewelry\" and other valueables.\n One of these valuables is a golden key.")
	
	# TO DO --> ADD UPSTAIRS AND DOWNSTAIRS TREASURE CHESTS
	
	# West Wing Parlor Room Information
	# Exits
	west_wing_parlor.addExit("north", study)
	west_wing_parlor.addExit("east", great_hall)
	# Items
	west_wing_parlor.addItem("TV", "The movie the Rise of Kara is playing.")
	west_wing_parlor.addItem("Speakers", "The music is taken from ourgourdandsavior.com.")
	west_wing_parlor.addItem("Lazy Boy", "It is dusty from years of not being cleaned by the lazy maid.")
	
	# Study Room Information
	# Exits
	study.addExit("west", laboratory)
	study.addExit("south", west_wing_parlor)
	# Items 
	study.addItem("BookShelf", "Hollow Books lie there, undisturbed for centuries")
	study.addItem("Globe", "Made during WWII, it shows the glorious ages of the U.S., that is, without Alaska and Hawaii.")
	study.addItem("Phonograph", "Moonlight Sonata is playing gracefully through the room.")
	
	
	# Laboratory Room Information
	laboratory.addExit("east", study)
	laboratory.addItem("Telescope", "It is the same telescope that Gaileo used to disprove geocentrism")
	laboratory.addItem("Chemical Cabinet", "It is unfortunately closed. No explosions...")
	laboratory.addItem("Heavy Metal Operating Table", "An ear rests on the table.")
	laboratory.addGrabbable("Red Key")
	
	# East Wing Parlor Room Information
	east_wing_parlor.addExit("west", great_hall)
	east_wing_parlor.addExit("north", dining_hall)
	east_wing_parlor.addItem("Windows", "Darkness has enveloped the mansion.")
	east_wing_parlor.addItem("Painting", "It is none other than the classic American Gothic.")
	east_wing_parlor.addItem("Couch", "The couch's cushions have been violently cut up.")
	
	
	# Dining Hall Room Information
	dining_hall.addExit("east", kitchen)
	dining_hall.addExit("south", east_wing_parlor)
	dining_hall.addItem("Table", "It has something on it that WATTTT")
	dining_hall.addItem("Chandelier", "It is the same one as the one in the Grand Hall")
	
	# Kitchen Room Information
	kitchen.addExit("west", dining_hall)
	kitchen.addItem("sink", "There are dirty dishes in it that appear to have been there for decades.")
	kitchen.addItem("freezer", "There is a sign that says 'DO NOT OPEN.'")
	kitchen.addItem("Stove", "There is a bowl of jalepeno cheese soup.")
	kitchen.addGrabbable("Orange Key")
	
	
	
	#start in room 1
	currentRoom = courtyard
	
#main part of program
inventory = []
inventoryDescriptions = []
createRooms()
#sets startTime = to the current time.
startTime = time.time()

#play forever
while (True):
	#set the status so the player has situational awareness
	#the status has room and inventory information
	status = "{}\nYou are carrying: {}".format(currentRoom, inventory)
	#calculates the total time since the game started.
	totalTime ="Total Time: {} seconds\n".format(round(time.time()-startTime, 3),)
	if (currentRoom == None ):
		death()
		break
	# display the status
	print "========================================================="
	print status
	#display the time since the game started
	print totalTime
	# prompt for player input
	# the game supports a simple language of <verb> <noun>
	# valid verbs are go, look, and take
	# valid nouns depend on the verb
	# we use raw_input here to treat the input as a string instead of
	# an expression
	action = raw_input("What to do? ")
	# set the user's input to lowercase to make it easier to compare
	# the verb and noun to known values
	action = action.lower()
	# exit the game if the player wants to leave (supports quit,
	# exit, and bye)
	if (action == "quit" or action == "exit" or action == "bye"):
		break

	# set a default response
	response = "I don't understand. Try verb noun. Valid verbs are go, look, and take"
	# split the user input into words (words are separated by spaces)
	# and store the words in a list
	words = action.split()
	# the game only understands two word inputs
	if (len(words) == 2):
		# isolate the verb and noun
		verb = words[0]
		noun = words[1]
		
		# the verb is: go
		if (verb == "go"):
			# set a default response
			response = "Invalid exit."
			
			# check for valid exits in the current room
			for i in range(len(currentRoom.exits)):
				# a valid exit is found
				if (noun == currentRoom.exits[i]):
				# change the current room to the one that is
				# associated with the specified exit
					currentRoom = currentRoom.exitLocations[i]
					# set the response (success)
					response = "Room changed."
					# no need to check any more exits
					break
		# the verb is: look
		elif (verb == "look"):
			# set a default response
			response = "I don't see that item."
			# check for valid items in the current room
			for i in range(len(currentRoom.items)):
				# a valid item is found

				if (noun == currentRoom.items[i].lower()):
					# set the response to the item's description
					response = currentRoom.itemDescriptions[i]

					# no need to check any more items
					break
					# the verb is: take

			for i in range(len(inventory)):
				# a valid item is found
				if (noun == inventory[i]):
					# set the response to the item's description
					response = inventoryDescriptions[i]
					break
					
		elif (verb == "take"):
			# set a default response
			response = "I don't see that item."
			
			# check for valid grabbable items in the current room
			for grabbable in currentRoom.grabbables:
				# a valid grabbable item is found
				if (noun == grabbable):
					# add the grabbable item to the player's
					# inventory
					inventory.append(grabbable)
					i = currentRoom.grabbables.index(grabbable)
					
					inventoryDescriptions.append(currentRoom.grabbablesDescriptions[i])
		
					# remove the grabbable item from the room
					currentRoom.delGrabbable(grabbable)
		
					# set the response (success)
					response = "{} grabbed.".format(grabbable)
		
					# no need to check any more grabbable item
					break
	#display the response 
	print "\n{}".format(response)

