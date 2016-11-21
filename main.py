import sys
import pygame
from population import Population
from individual import Individual
pygame.init()

mutation_rate = 0.1
size = (960,960)
WHITE = (255,255,255)
BLACK = (0,0,0)
GREEN = (0,255,0)

pop_size = 250
screen = pygame.display.set_mode(size)

solution = (0,0)

def main():
	pane = pygame.Surface(size)
	done = False
	while not done:
		for event in pygame.event.get():
			if event.type == pygame.MOUSEBUTTONDOWN:
				solution = pygame.mouse.get_pos()
				done = True

	pop = Population(pop_size,size,mutation_rate,solution)
	done = False
	while not done:
		for event in pygame.event.get():
			if event.type == pygame.QUIT: sys.exit()
			if event.type == pygame.MOUSEBUTTONDOWN:
				solution = pygame.mouse.get_pos()
				pop = Population(pop_size,size,mutation_rate,solution)
		pygame.time.Clock().tick(30)
		screen.fill(WHITE)
		pygame.display.update()
		pane.fill(WHITE)
		pygame.draw.circle(pane, GREEN, solution, 4)
		for individ in pop.population:
			pygame.draw.circle(pane, BLACK, (individ.x,individ.y), 4)
			if (solution[0] == individ.x) and (solution[1] == individ.y): 
				done = True
		screen.blit(pane, (0,0))
		pygame.display.flip()
		pop.evolve()

if __name__ == '__main__':
	main()
