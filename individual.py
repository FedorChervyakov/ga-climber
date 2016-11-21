import random
import math

class Individual:

	x = 0
	y = 0
	maxxy = (0,0)
	solution = (0,0)

	fitness = 0
	adjusted_fitn = 0

	mutation_rate = 0

	def __init__(self, solution=(0,0), max_size=(0,0), rate=0, x_new=0, y_new=0):
		self.x = x_new
		self.y = y_new
		self.calc_fitness()
		self.mutation_rate = rate 
		self.maxxy = max_size
		self.solution = solution

	def init(self, max_size, rate, sol):
		self.x = random.randint(0,max_size[0])
		self.y = random.randint(0,max_size[1])
		self.fitness = self.calc_fitness()
		self.maxxy = (0,0)
		self.mutation_rate = rate
		self.solution = sol

	def calc_fitness(self):
		fitn = math.sqrt(math.pow(self.maxxy[0],2) + math.pow(self.maxxy[1],2)) - math.sqrt(math.pow(self.x - self.solution[0],2) + math.pow(self.y - self.solution[1], 2))
		self.fitness = fitn
		return fitn

	def mutate(self):
		dist = random.randint(0,50)
		if random.random() <= self.mutation_rate:
			if random.random() <= 0.5:
				if random.random() <= 0.5:
					self.x += dist
				else:
					self.x -= dist
				if self.x >= self.maxxy[0]: self.x = self.maxxy[0]	
			else:
				if random.random() <= 0.5:
					self.y += dist
				else:
					self.y -= dist
				if self.y >= self.maxxy[1]: self.y = self.maxxy[1]


def main():
	individ = Individual()
	individ.init((320,640))
	print('x: %f y: %f fitness: %f' % (individ.x, individ.y, individ.fitness))

if __name__ == '__main__':
	main()

