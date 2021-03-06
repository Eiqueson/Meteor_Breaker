import pygame
from pygame.locals import *
from gamelib import SimpleGame
from elements import Player, Meteor, Bullet, Life
import random

class MeteorGame(SimpleGame):
	BLACK = pygame.Color('black')
	WHITE = pygame.Color('white')
	COLOR = [pygame.Color('red'), pygame.Color('green'), pygame.Color('blue'), pygame.Color('yellow')]
	YELLOW = pygame.Color('yellow')
	RED = pygame.Color('red')
	SPEED = [100, 150, 200, 250, 300]
	
	def __init__(self):
		super(MeteorGame, self).__init__('Meteor Breaker', MeteorGame.BLACK)
		self.player = Player(color=MeteorGame.WHITE,pos=(self.window_size[0]/2, self.window_size[1]-24))
		self.meteors = [Meteor(radius=24, color=random.choice(MeteorGame.COLOR), pos=(random.randrange(24,456),-24), speed=(0, random.choice(MeteorGame.SPEED)), hp=3)]
		self.bullets = []
		self.lives = [Life(radius=5, color=MeteorGame.RED, pos=(160,20)), Life(radius=5, color=MeteorGame.RED, pos=(140,20)), \
						Life(radius=5, color=MeteorGame.RED, pos=(120,20)), Life(radius=5, color=MeteorGame.RED, pos=(100,20)), \
						Life(radius=5, color=MeteorGame.RED, pos=(80,20))]
		self.score = 0
		self.life = 5
	
	def init(self):
		super(MeteorGame, self).init()
		self.render_score()
		self.render_life()

	def render(self, display):
		self.player.render(display)
		
		for meteor in self.meteors:
			meteor.render(display)

		for bullet in self.bullets:
			bullet.render(display)

		for life in self.lives:
			life.render(display)

		display.blit(self.score_image, (360,10))
		display.blit(self.life_image, (10,10))

	def update(self):
		if self.is_key_pressed(K_LEFT):
			self.player.move_left()
		if self.is_key_pressed(K_RIGHT):
			self.player.move_right()
		if self.is_key_pressed(K_SPACE) and pygame.time.get_ticks()%3 == 0 :
			self.newBullet = Bullet(pos=(self.player.x, self.player.y-24), color=MeteorGame.YELLOW, speed=(0,500))
			self.bullets.append(self.newBullet)

		for meteor in self.meteors:
			meteor.move(1./self.fps)

		for bullet in self.bullets:
			bullet.move(1./self.fps, self.player)

		if pygame.time.get_ticks() <= 30000:
			if pygame.time.get_ticks()%self.fps == 0:
				self.newMeteor = Meteor(radius=24, color=random.choice(MeteorGame.COLOR), pos=(random.randrange(24,456),-24), speed=(0, random.choice(MeteorGame.SPEED)), hp=10)
				self.meteors.append(self.newMeteor)
		elif pygame.time.get_ticks() <= 60000:
			if pygame.time.get_ticks()%(self.fps/2) == 0:
				self.newMeteor = Meteor(radius=24, color=random.choice(MeteorGame.COLOR), pos=(random.randrange(24,456),-24), speed=(0, random.choice(MeteorGame.SPEED)), hp=10)
				self.meteors.append(self.newMeteor)
		else:
			if pygame.time.get_ticks()%(self.fps/4) == 0:
				self.newMeteor = Meteor(radius=24, color=random.choice(MeteorGame.COLOR), pos=(random.randrange(24,456),-24), speed=(0, random.choice(MeteorGame.SPEED)), hp=10)
				self.meteors.append(self.newMeteor)

		for meteor in self.meteors:
			if (meteor.y > self.window_size[1]) or (((meteor.y+24 > self.player.y-24) and (self.player.y+24 > meteor.y-24))and  (self.player.x-24 < meteor.x < self.player.x+24)):
				self.meteors.remove(meteor)
				self.life -= 1
				self.render_life()
				self.lives.remove(self.lives[0])
				if (self.life == 0):
					print 'Game Over!'
					print 'Your score = %d' % self.score
					self.terminate()
			for bullet in self.bullets:
				if (meteor.y-24 < bullet.y < meteor.y+24) and (meteor.x-24 < bullet.x < meteor.x+24):
					self.bullets.remove(bullet)
					meteor.hp -= 1
					if (meteor.hp == 0):
						self.meteors.remove(meteor)
						self.score += 1
						self.render_score()

	def render_score(self):
		self.score_image = self.font.render("Score = %d" % self.score, 1, MeteorGame.WHITE)

	def render_life(self):
		self.life_image = self.font.render("Life :", 0, MeteorGame.WHITE)

def main():
	game = MeteorGame()
	game.run()

if __name__ == '__main__':
	main()