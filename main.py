import pygame
from pygame.locals import *
from gamelib import SimpleGame
from elements import Player, Meteor
import random

class MeteorGame(SimpleGame):
	BLACK = pygame.Color('black')
	WHITE = pygame.Color('white')
	COLOR = [pygame.Color('red'), pygame.Color('green'), pygame.Color('blue'), pygame.Color('yellow')]
	YELLOW = pygame.Color('yellow')
	SPEED = [100, 150, 200, 250, 300]
	
	def __init__(self):
		super(MeteorGame, self).__init__('Meteor Breaker', MeteorGame.BLACK)
		self.player = Player(color=MeteorGame.WHITE,pos=(self.window_size[0]/2, self.window_size[1]-24))
		self.meteors = [Meteor(radius=24, color=random.choice(MeteorGame.COLOR), pos=(random.randrange(24,456),-24), speed=(0, random.choice(MeteorGame.SPEED)))]
	
	def init(self):
		super(MeteorGame, self).init()

	def render(self, display):
		self.player.render(display)
		
		for meteor in self.meteors:
			meteor.render(display)

	def update(self):
		if self.is_key_pressed(K_LEFT):
			self.player.move_left()
		if self.is_key_pressed(K_RIGHT):
			self.player.move_right()

		for meteor in self.meteors:
			meteor.move(1./self.fps)

		if pygame.time.get_ticks() <= 30000:
			if pygame.time.get_ticks()%self.fps== 0:
				self.newMeteor = Meteor(radius=24, color=random.choice(MeteorGame.COLOR), pos=(random.randrange(24,456),-24), speed=(0, random.choice(MeteorGame.SPEED)))
				self.meteors.append(self.newMeteor)
		elif pygame.time.get_ticks() <= 60000:
			if pygame.time.get_ticks()%(self.fps/2)== 0:
				self.newMeteor = Meteor(radius=24, color=random.choice(MeteorGame.COLOR), pos=(random.randrange(24,456),-24), speed=(0, random.choice(MeteorGame.SPEED)))
				self.meteors.append(self.newMeteor)
		else:
			if pygame.time.get_ticks()%(self.fps/4)== 0:
				self.newMeteor = Meteor(radius=24, color=random.choice(MeteorGame.COLOR), pos=(random.randrange(24,456),-24), speed=(0, random.choice(MeteorGame.SPEED)))
				self.meteors.append(self.newMeteor)

def main():
	game = MeteorGame()
	game.run()

if __name__ == '__main__':
	main()