import pygame

pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

x = 10
y = 10

clock = pygame.time.Clock()

def object():
	pygame.draw.rect( screen,(100,200,100), pygame.Rect(x, y, 10, 10))

while True:
	screen.fill((0,0,0))
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
				exit()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
					x += -1.7
			if event.key == pygame.K_RIGHT:
					x += 1.7
	object()
	pygame.display.update()
	clock.tick(60)

