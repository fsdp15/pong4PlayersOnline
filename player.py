import settings

class Player(object):
	def __init__(self, playerNumber):
		self.setPlayerNumber(playerNumber)
		if (playerNumber == 1):
			self.setX(0)
			self.setY((settings.SCREEN_HEIGTH / 2) - (settings.V_PADDLE_HEIGTH / 2))
			self.setPlayerColor(settings.BLUE)
		elif (playerNumber == 2):
			self.setX(settings.SCREEN_WIDTH - settings.V_PADDLE_WIDTH)
			self.setY((settings.SCREEN_HEIGTH / 2) - (settings.V_PADDLE_HEIGTH / 2))
			self.setPlayerColor(settings.RED)
		elif (playerNumber == 3):
			self.setX((settings.SCREEN_WIDTH / 2) - (settings.H_PADDLE_WIDTH / 2))
			self.setY(0)
			self.setPlayerColor(settings.GREEN)
		elif (playerNumber == 4):
			self.setX((settings.SCREEN_WIDTH / 2) - (settings.H_PADDLE_WIDTH / 2))
			self.setY(settings.SCREEN_HEIGTH - settings.H_PADDLE_HEIGTH)
			self.setPlayerColor(settings.YELLOW)

	def movePlayerUp(self):
		self.setY(self.getY() - settings.DEFAULT_PADDLE_DESLOCATION)

	def movePlayerDown(self):
		self.setY(self.getY() + settings.DEFAULT_PADDLE_DESLOCATION)

	def movePlayerLeft(self):
		self.setX(self.getX() - settings.DEFAULT_PADDLE_DESLOCATION)

	def movePlayerRight(self):
		self.setX(self.getX() + settings.DEFAULT_PADDLE_DESLOCATION)

	def getX(self):
		return self.x

	def setX(self, x):
		self.x = x

	def getY(self):
		return self.y

	def setY(self, y):
		self.y = y

	def getPlayerNumber(self):
		return self.playerNumber

	def setPlayerNumber(self, playerNumber):
		self.playerNumber = playerNumber

	def getPlayerColor(self):
		return self.playerColor

	def setPlayerColor(self, playerColor):
		self.playerColor = playerColor