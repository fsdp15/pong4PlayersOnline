import zlib

class Message(object):
	def __init__(self):
		self.setType(0)
		self.setOrigin(0)
		self.setDestination(0)
		self.setMovement(0)

	def __init__ (self, type, origin, destination, movement):
		self.setType(type)
		self.setOrigin(origin)
		self.setDestination(destination)
		self.setMovement(movement)

    #Type
	def getType(self):
		return int(self.type)

	def setType(self, type):
		self.type = type 

	def getOrigin(self):
		return int(self.playerNumber_origin) 

	def setOrigin(self, origin):
		self.playerNumber_origin = origin 

	def getDestination(self):
 		return int(self.playerNumber_origin)

	def setDestination(self, destination):
		self.playerNumber_destination = destination

	def getMovement(self):
		return int(self.movement)

	def setMovement(self, movement):
		self.movement = movement

	def pack(self):
		return str(self.getType()) + str(self.getOrigin()) + str(self.getDestination()) + str(self.getMovement())

	def unpack(self, msg):
		self.setType(msg[0])
		self.setOrigin(msg[1])
		self.setDestination(msg[2])
		self.setMovement(msg[3])
		return self