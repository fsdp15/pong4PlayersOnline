import pygame
import game
import time
import ball
import settings
import player
import random

def drawScreen(screen, playersList, gameBall):
	screen.fill((0, 0, 0))
	for myPlayer in playersList:
		if (myPlayer.getPlayerNumber() == 1 or myPlayer.getPlayerNumber() == 2):
			pygame.draw.rect(screen, myPlayer.getPlayerColor(), pygame.Rect(myPlayer.getX(), myPlayer.getY(), settings.V_PADDLE_WIDTH, settings.V_PADDLE_HEIGTH))
		else:
			pygame.draw.rect(screen, myPlayer.getPlayerColor(), pygame.Rect(myPlayer.getX(), myPlayer.getY(), settings.H_PADDLE_WIDTH, settings.H_PADDLE_HEIGTH))
	pygame.draw.rect(screen, settings.WHITE, pygame.Rect(gameBall.getX(), gameBall.getY(), settings.BALL_WIDTH, settings.BALL_HEIGTH))
	pygame.display.flip()

def checkBallPosition(gameBall, playersList):
	for myPlayer in playersList:
		if (myPlayer.getPlayerNumber() == 1):
			if (gameBall.getX() <= settings.V_PADDLE_WIDTH and gameBall.getX() >= 0):
				if (gameBall.getY() >= myPlayer.getY() - 10 and gameBall.getY() <= myPlayer.getY() + settings.V_PADDLE_HEIGTH + 10):
					gameBall.setXDirection(gameBall.getXDirection() * -1)
					gameBall.setX(gameBall.getX() + gameBall.getXDirection())
				else:
					gameBall.setX(settings.SCREEN_WIDTH / 2)
					gameBall.setY(settings.SCREEN_HEIGTH / 2)

		elif (myPlayer.getPlayerNumber() == 2):
			if (gameBall.getX() >= (settings.SCREEN_WIDTH - settings.V_PADDLE_WIDTH) and (gameBall.getX() <= settings.SCREEN_WIDTH)):
				if (gameBall.getY() >= myPlayer.getY() - 10 and gameBall.getY() <= myPlayer.getY() + settings.V_PADDLE_HEIGTH + 10):
					gameBall.setXDirection(gameBall.getXDirection() * -1)
					gameBall.setX(gameBall.getX() + gameBall.getXDirection())
				else:
					gameBall.setX(settings.SCREEN_WIDTH / 2)
					gameBall.setY(settings.SCREEN_HEIGTH / 2)

		elif (myPlayer.getPlayerNumber() == 3):
			if (gameBall.getY() < settings.H_PADDLE_HEIGTH and gameBall.getY() >= 0):
				if (gameBall.getX() >= myPlayer.getX() - 10 and gameBall.getX() <= myPlayer.getX() + settings.H_PADDLE_WIDTH + 10):
					gameBall.setYDirection(gameBall.getYDirection() * -1)
					gameBall.setY(gameBall.getY() + gameBall.getYDirection())
				else:
					gameBall.setX(settings.SCREEN_WIDTH / 2)
					gameBall.setY(settings.SCREEN_HEIGTH / 2)

		elif (myPlayer.getPlayerNumber() == 4):
			if (gameBall.getY() >= (settings.SCREEN_HEIGTH - settings.H_PADDLE_HEIGTH) and (gameBall.getY() <= settings.SCREEN_HEIGTH)):
				if (gameBall.getX() >= myPlayer.getX() - 10 and gameBall.getX() <= myPlayer.getX() + settings.H_PADDLE_WIDTH + 10):
					gameBall.setYDirection(gameBall.getYDirection() * -1)
					gameBall.setY(gameBall.getY() + gameBall.getYDirection())
				else:
					gameBall.setX(settings.SCREEN_WIDTH / 2)
					gameBall.setY(settings.SCREEN_HEIGTH / 2)