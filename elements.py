import pygame
from pygame.locals import *
from gamelib import SimpleGame


class Meteor(object):
	def __init__(self, radius, color, pos, speed):
		(self.x, self.y) = pos
		(self.vx, self.vy) = speed
		self.color = color
		self.radius = radius
		
	def move(self, delta_t):
		self.x += self.vx*delta_t
		self.y += self.vy*delta_t
		
	def render(self, display):
		pos = (int(self.x),int(self.y))
		pygame.draw.circle(display, self.color, pos, self.radius, 5)

###################################
class Player(object):
	THICKNESS = 48
	
	def __init__(self, color, pos, height=48):
		(self.x, self.y) = pos
		self.height = height
		self.color = color

	def move_left(self):
		self.x -= 10
		if self.x < 0:
			self.x = 0

	def move_right(self):
		self.x += 10
		if self.x > 480:
			self.x = 480
		
	def render(self, display):
		pygame.draw.rect(display, self.color, pygame.Rect(self.x-self.THICKNESS/2.0, self.y-self.height/2.0, self.THICKNESS, self.height), 3)

###################################		