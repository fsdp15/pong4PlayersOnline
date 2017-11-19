import random
import settings

class Ball(object):
	def __init__(self):
		self.setX(settings.SCREEN_WIDTH / 2)
		self.setY(settings.SCREEN_HEIGTH / 2)
		#if (random.random() < 0.5): #Defining the first direction that the ball must go
		#	self.setXDirection(settings.DEFAULT_BALL_DESLOCATION)
		#else:
		#	self.setXDirection(settings.DEFAULT_BALL_DESLOCATION * -1)
		#if (random.random() < 0.5):
		#	self.setYDirection(settings.DEFAULT_BALL_DESLOCATION)
	#	else: 
		#	self.setYDirection(settings.DEFAULT_BALL_DESLOCATION * -1)
		self.setXDirection(settings.DEFAULT_BALL_DESLOCATION)
		self.setYDirection(settings.DEFAULT_BALL_DESLOCATION)

	def moveBall(self):
		if ((self.getX() + self.getXDirection()) > 0 and (self.getX() + self.getXDirection()) < settings.SCREEN_WIDTH):
			if (self.getXDirection() > 0):
				self.setX(self.getX() + self.getXDirection() + 1.2)
			else: self.setX(self.getX() + self.getXDirection() - 1.2)
		else:
			self.setXDirection(self.getXDirection() * -1)
			self.setX(self.getX() + self.getXDirection())
		if ((self.getY() + self.getYDirection()) > 0 and (self.getY() + self.getYDirection()) < settings.SCREEN_HEIGTH):
			if (self.getYDirection() > 0):
				self.setY(self.getY() + self.getYDirection() + 0.9)
			else: self.setY(self.getY() + self.getYDirection() - 0.9)
		else:
			self.setYDirection(self.getYDirection() * -1)
			self.setY(self.getY() + self.getYDirection())		

	def getX(self):
		return self.x

	def setX(self, x):
		self.x = x

	def getY(self):
		return self.y

	def setY(self, y):
		self.y = y

	def getXDirection(self):
		return self.xDirection

	def setXDirection(self, xDirection):
		self.xDirection = xDirection

	def getYDirection(self):
		return self.yDirection

	def setYDirection(self, yDirection):
		self.yDirection = yDirection