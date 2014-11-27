import pygame
from pygame.locals import *

class SimpleGame(object):

	def __init__(self, title, window_size=(480,640), fps=60):
		self.title = title
		self.window_size = window_size
		self.fps = fps

	def run(self):
		self.init()
		while True:
			self.update()
			self.render()
			self.clock.tick(self.fps)

	def init(self):
		self.__game_init()

	def update(self):
		pass

	def render(self):
		pass

	def __game_init(self):
		pygame.init()
		self.clock = pygame.time.Clock()
		self.display = pygame.display.set_mode(self.window_size)
		pygame.display.set_caption(self.title)
		self.font = pygame.font.SysFont("monospace", 16)
