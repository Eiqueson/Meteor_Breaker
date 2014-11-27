import pygame
from pygame.locals import *
from gamelib import SimpleGame

class MeteorGame(SimpleGame):
	
	def init(self):
		super(MeteorGame, self).init()

def main():
	game = MeteorGame('Meteor Breaker')
	game.run()

if __name__ == '__main__':
	main()