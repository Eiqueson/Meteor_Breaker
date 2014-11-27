import pygame
from pygame.locals import *
from gamelib import SimpleGame
from elements import Player
import random

class MeteorGame(SimpleGame):
	BLACK = pygame.Color('black')
	WHITE = pygame.Color('white')
	COLOR = [pygame.Color('red'), pygame.Color('green'), pygame.Color('blue')]
	YELLOW = pygame.Color('yellow')
	SPEED = [100, 150, 200, 250, 300]
	
	def __init__(self):
		super(MeteorGame, self).__init__('Meteor Breaker', MeteorGame.BLACK)
		self.player = Player(color=MeteorGame.WHITE,pos=(self.window_size[0]/2, self.window_size[1]-24))
	
	def init(self):
		super(MeteorGame, self).init()

	def render(self, display):
		self.player.render(display)

def main():
	game = MeteorGame()
	game.run()

if __name__ == '__main__':
	main()