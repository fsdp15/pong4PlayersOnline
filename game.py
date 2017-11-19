import pygame
import time
import ball
import settings
import player
import screenMoves
import connection
import csv
import sys
import host
import socket
import message
import threading
import select

MOVEMENT = 0
WAITING = 1
DOWN = 0
UP = 1
NULL = -1
START = 1
playersReady = []
sockList = {}

def main():
	ip = connection.myIpAddress()
	playerNumber = connection.identifyPlayer(hosts, ip)
	port = connection.identififyPort(hosts)
	if (playerNumber < 1 or playerNumber > 4):
		print("The hosts.txt file is incorrect")
		sys.exit()
	print("{}{}".format("I am player ", playerNumber))

	s = createServerSocket(port, ip) # Creating thread to listen for incoming connections
	playersList = []
	numberOfPlayers = len(hosts)
	for i in range(0, numberOfPlayers): # Getting number of players in the game
		playersList.append(player.Player(i + 1))
		playersReady.append(0)

	pygame.init()
	clock = pygame.time.Clock()
	screen = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGTH))
	gameBall = ball.Ball()
	screenMoves.drawScreen(screen, playersList, gameBall)

	createThreads(playerNumber, len(hosts), s, playersList) # Creating threads for pairing hosts and for communication with other players
	i = 0
	playersReady[playerNumber - 1] = 1

	while True: # Syncing the game with other players
		sendMessageForAll(WAITING, NULL, playerNumber, playersList)
		time.sleep(0.5)
		START = 1
		while (i < numberOfPlayers):
			if (playersReady[i] == 0):
				START = 0
			i = i + 1
		if (START == 1):
			break
		i = 0

	while True: # Game loop
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				break

		gameBall.moveBall()
		getDirections(playersList[playerNumber - 1], playerNumber, playersList) # Move my player
		screenMoves.checkBallPosition(gameBall, playersList) # Check if the ball is colliding with a paddle
		screenMoves.drawScreen(screen, playersList, gameBall)
		clock.tick(60) # 60 FPS

	return 1

def readHosts(): # Read hosts.txt file
	f = open("hosts.txt", 'rb')
	reader = csv.reader(f)
	hosts = []
	for row in reader:
		h = host.Host(row) 
		hosts.append(h)
	f.close()
	return hosts

hosts = readHosts()

def createServerSocket(port, ip): # Socket to listen for connection requests
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	s.bind((ip, port))
	s.listen(5)
	return s

def createThreads(playerNumber, numberOfPlayers, s, playersList):
	t1 = threading.Thread(target=listen, args=[s, playerNumber, playersList])
	t2 = threading.Thread(target=pairHosts, args=[playerNumber])

	#Make all threads finish when the main thread ends
	t1.daemon = True
	t2.daemon = True

	t1.start()
	t2.start()

	#Waiting for the hosts to pair
	while True:
		time.sleep(1)
		if not t2.isAlive():
			break

def listen(s, playerNumber, playersList): # Listening for incoming connections
	try:
		while True:
			auxsock, auxaddr = s.accept()
			playerNumberOrigin = connection.identifyPlayer(hosts, auxaddr[0]) #Player number of the player that requested connection
			t = threading.Thread(target=serverHandler, args=[auxsock, playerNumberOrigin, playersList])
			t.start()

	except KeyboardInterrupt:
		s.close()
		sys.exit()

	return 1

def updatePlayer(myPlayer, movement): # Update other players movements
		if (movement == DOWN): #DOWN
			if (myPlayer.getPlayerNumber() == 1 or myPlayer.getPlayerNumber() == 2):
				if (myPlayer.getY() < (settings.SCREEN_HEIGTH - settings.V_PADDLE_HEIGTH)): 
					myPlayer.movePlayerDown()
			else:
				if (myPlayer.getX() > 0): 
					myPlayer.movePlayerLeft()
		elif (movement == UP): #UP
			if (myPlayer.getPlayerNumber() == 1 or myPlayer.getPlayerNumber() == 2):
				if (myPlayer.getY() > 0):
					myPlayer.movePlayerUp()
			else:
				if (myPlayer.getX() < (settings.SCREEN_WIDTH - settings.H_PADDLE_WIDTH)):
					myPlayer.movePlayerRight()

def getDirections(myPlayer, playerNumber, playersList): # Move my player and send my move to other players
	if (myPlayer.getPlayerNumber() == playerNumber):
		pressed = pygame.key.get_pressed()
		if (myPlayer.getPlayerNumber() == 1 or myPlayer.getPlayerNumber() == 2):
			if (pressed[pygame.K_UP] and myPlayer.getY() > 0):
				sendMessageForAll(MOVEMENT, UP, myPlayer.getPlayerNumber(), playersList) # Send my move to other players
				myPlayer.movePlayerUp()
			if (pressed[pygame.K_DOWN] and myPlayer.getY() < (settings.SCREEN_HEIGTH - settings.V_PADDLE_HEIGTH)):
				sendMessageForAll(MOVEMENT, DOWN, myPlayer.getPlayerNumber(), playersList)
				myPlayer.movePlayerDown()
		else:
			if (pressed[pygame.K_LEFT] and myPlayer.getX() > 0):
				sendMessageForAll(MOVEMENT, DOWN, myPlayer.getPlayerNumber(), playersList)
				myPlayer.movePlayerLeft()
			if (pressed[pygame.K_RIGHT] and myPlayer.getX() < (settings.SCREEN_WIDTH - settings.H_PADDLE_WIDTH)):
				sendMessageForAll(MOVEMENT, UP, myPlayer.getPlayerNumber(), playersList)
				myPlayer.movePlayerRight()

def serverHandler(s, playerNumber, playersList): # Receiving messages from other player
	global playersReady
	try:
		while True:
			r, w, e = select.select((s,), (s,), (s,), 0) # Verifying if there is data to be read on the socket
			if r: # r = read
				msg = s.recv(80)
				if len(msg) == 0: # If the message is empty, it means that the other side closed connection
					s.shutdown(socket.SHUT_RDWR)
					s.close()
					break

				myMessage = message.Message(0,0,0,0)
				myMessage.unpack(msg)

				if(myMessage.getType() == MOVEMENT):
					updatePlayer(playersList[myMessage.getOrigin() - 1], myMessage.getMovement())

				if (myMessage.getType() == WAITING):
					playersReady[myMessage.getOrigin() - 1] = 1

	except KeyboardInterrupt:
		s.shutdown(socket.SHUT_RDWR)
		s.close()
		sys.exit()

	except socket.error:
		s.close()
		return 1

	except socket.timeout:
		s.close()
		return 1
	return 1

def sendMessageForAll(type, movement, playerNumberOrigin, playersList): # Send a message to all other players
	sockets = sockList.itervalues()
	i = 0
	try:
		for s in sockets:
			myMessage = message.Message(type, playerNumberOrigin, i + 1, movement)
			msg = myMessage.pack()
			s.send(msg)
			i += 1

	except socket.error:
		s.close()

def pairHosts(playerNumber):
	validHosts = 1
	#A list to know which players are already connect, preventing new connections requests to them
	connectedHosts = []
	threadsList = []
	while validHosts < len(hosts):
		for h in hosts:
				playerNumberDestination = h.getPlayerNumber()
				if ((playerNumberDestination != playerNumber) and (not(playerNumberDestination in connectedHosts))):
					try:
						time.sleep(0.5)
						s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
						s.connect((h.getIp(), h.getPort())) 
						sockList[playerNumberDestination] = s  
						print("Connected with player " + str(playerNumberDestination))
						connectedHosts.append(playerNumberDestination)
						validHosts = validHosts + 1
					except Exception as e:
						print("Waiting connection with player " + str(playerNumberDestination))
	print("{}{}{}".format("Player ", playerNumber, " made connection with all other players! Starting game"))
	return 0

if __name__ == "__main__":
	main()