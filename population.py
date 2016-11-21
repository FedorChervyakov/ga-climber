import math
import random
from individual import Individual

class Population:

	max_field = (0,0)
	size = 0
	mutation_rate = 0
	population = []
	solution = (0,0)

	#Initialize random population of size0
	def __init__(self, size0, field_size, mutation, sol):
		self.max_field = field_size
		self.size = size0
		self.mutation_rate = mutation
		self.solution = sol
		#self.population = []
		i = 0
		while i != self.size:
			i += 1
			individ = Individual(self.solution)
			individ.init(field_size,self.mutation_rate,self.solution)
			self.population.append(individ)

	# Perform Selection, crossover and mutation 
	def evolve(self):
		# Swap y's and generate new population (new_pop[])
		candidates = self.roulette_selection()
		new_pop = []
		i = 0 
		while i != self.size:
			cand1 = candidates[random.randint(0,self.size-1)]
			cand2 = candidates[random.randint(0,self.size-1)]
			while cand2 == cand1:
				cand2 = candidates[random.randint(0,self.size-1)]
			pair = self.crossover(cand1,cand2)
			new_pop.append(pair[0])
			new_pop.append(pair[1])
			i += 1
		for individ in self.population:
			self.population.remove(individ)
		# Perform mutation (see individual.mutate())
		for individ in new_pop:
			individ.mutate()
			individ.calc_fitness()
		for individ in new_pop:
			self.population.append(individ)
			#print('x: %5.2f y: %5.2f fitness: %5.2f adjusted fitness: %5.2f' % (individ.x, individ.y, individ.fitness, individ.adjusted_fitn))

	def crossover(self,cand1,cand2):
		res1 = Individual(self.solution,self.max_field, self.mutation_rate, cand1.x,cand2.y)
		res2 = Individual(self.solution,self.max_field, self.mutation_rate,cand2.x,cand1.y)		
		return (res1, res2)

	# Unoptimized roulette selection
	def roulette_selection(self):
		# Sum all fitnesses
		fit_sum = 0
		for individ in self.population:
			fit_sum += individ.fitness
		# Generate adjusted fitnesses; adj = fitn/fit_sum
		for individ in self.population:
			individ.adjusted_fitn = individ.fitness / fit_sum * self.size
		# Create a tuple list of (cumulative fitness + adjusted fitness, individ)
		cumulative = 0
		selection = []
		for individ in self.population:
			cumulative += individ.adjusted_fitn
			selection.append((cumulative,individ))
		# Select individuals using roulette selection
		i = 0
		candidates = []
		while i != self.size:
			# roulette wheel selection (not optimmized)
			j = 0
			done = False
			rand = random.random()*self.size
			while not done :
				if j == 0:
					cuml = 0
				else:
					cuml = selection[j-1][0]
				if (rand <= selection[j][0]) and (rand > cuml):
					candidates.append(selection[j][1])
					done = True
				j += 1
			i += 1
		return candidates

def main():
	pop = Population(10,(320,640),0.1)
	pop.evolve()
	#for individ in pop.population:
		#print('x: %f y: %f fitness: %f' % (individ.x, individ.y, individ.fitness))

if __name__ == '__main__':
	main()

