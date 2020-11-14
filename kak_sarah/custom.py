from random import randint,sample,random
import numpy

class Board:
	
	def __init__(self, rows, columns):
		self.rows = rows
		self.columns = columns
		self.squares = [['00'] * columns for i in range(rows)]

	def __repr__(self):
		print('Step di papan : ')
		for i in range(self.rows):
			print(self.squares[i])

class Tour:
	
	def __init__(self,start):
		self.start = start
		self.pos = start
		self.tour = []
		self.visited = [self.start]
		self.fitness = 0
		
		self.board = Board(8,8)
		(row, column) = self.start
		self.board.squares[column - 1][row - 1] = 1

		#list of knight's moves as tuples
		self.moves = [(1,2), (2,1), (2,-1), (1,-2),
		 (-1,-2), (-2,-1), (-2,1), (-1,2)]

	def isLegalMove(self,move):	
		
		decMove = int(move,2)
		moveTup = self.moves[decMove]

		newPosX = self.pos[0] + moveTup[0]
		newPosY = self.pos[1] + moveTup[1]
		newPos = (newPosX,newPosY)

		if newPosX > 0 and newPosX <= self.board.columns and newPosY > 0 and newPosY <= self.board.rows:
			if newPos not in self.visited:
				return 'legal'
			else:
				return 'visited'
		else:
			return False

	def generateTour(self):
		
		while len(self.tour) < 63:
			nextMove = randint(0,7)
			binMove = bin(nextMove)[2:].zfill(3)
			
			if self.isLegalMove(binMove) == 'legal' or self.isLegalMove(binMove) == 'visited':
				self.tour.append(binMove)
				thisMove = self.moves[nextMove]

				newPosX = self.pos[0] + thisMove[0]
				newPosY = self.pos[1] + thisMove[1]
				newPos = (newPosX,newPosY)

				self.pos = newPos
				self.visited.append(newPos)

			else:
				pass

	def tourFitness(self):
		
		newFitness = 0

		self.pos = self.start
		visited = self.visited
		self.visited = [self.start]

		for move,pos in zip(self.tour,visited):
			self.pos = pos
			if self.isLegalMove(move) == 'legal':
				newFitness += 1
				
				decMove = int(move,2)
				moveTup = self.moves[decMove]
				newPosX = self.pos[0] + moveTup[0]
				newPosY = self.pos[1] + moveTup[1]
				newPos = (newPosX,newPosY)

				self.visited.append(newPos)
			else:
				self.fitness = newFitness
				self.visited = visited
				return self.fitness

		self.visited = visited
		return self.fitness

	def repairVisited(self):
		
		self.pos = self.start
		try:
			self.visited[0] = self.start
		except IndexError:
			self.visited.append(self.start)
		index = 1
		for i in self.tour:
			decMove = int(i,2)
			moveTup = self.moves[decMove]

			newPosX = self.pos[0] + moveTup[0]
			newPosY = self.pos[1] + moveTup[1]
			newPos = (newPosX,newPosY)

			try:
				self.visited[index] = newPos
			except IndexError:
				self.visited.append(newPos)
			
			self.pos = newPos
			index += 1

		return self.visited

	def presentTour(self):
		
		progress = 1
		for i in range(self.fitness):
			thisSquare = self.visited[i]
			(row,column) = thisSquare
			self.board.squares[column - 1][row - 1] = str(progress).zfill(2)
			progress += 1

		print("Board state at end of tour: ")
		self.board.__repr__()
		return None

def generatePop(size):
	
	population = []
	for i in range(size):
		newTour = Tour((1,1))
		newTour.generateTour()
		population.append(newTour)

	return population

def rankTours(population):
	
	fitnessDict = {}
	for i in population:
		fitnessDict[population.index(i)] = i.tourFitness()
	fitness_sorted = sorted(fitnessDict, key=fitnessDict.get, reverse=True)
	return fitness_sorted

def selection(population,eliteSize):
	
	selected = []
	sort_by_fitness = rankTours(population)
	elites = sort_by_fitness[:eliteSize]
	for i in elites:
		selected.append(population[i])

	#produce cumulative sum of fitnesses for calculating weightings
	fitness_sum = 0
	for i in population:
		fitness_sum += i.fitness

	#calculate a list of fitness-based weightings for the population
	weights = []
	for i in population:
		weight = (i.fitness / fitness_sum)
		weights.append(weight)

	#select the remainder of the pool weighted by fitness
	weighted_pool = numpy.random.choice(population,(len(population) - eliteSize), weights)

	for i in weighted_pool:
		selected.append(i)

	return selected

def breed(parent1,parent2):
	
	child = Tour((1,1))
	
	part1 = parent1.tour[:parent1.fitness]
	part2 = parent2.tour[parent1.fitness:]
	newRoute = list.__add__(part1,part2)

	child.tour = newRoute
	return child

def breedPop(matingPool,eliteSize):
	
	newPop = []

	requiredChildren = len(matingPool) - eliteSize
	scrambledPool = sample(matingPool, len(matingPool))

	for i in range(eliteSize):
		newPop.append(matingPool[i])

	for i in range(requiredChildren):
		child = breed(scrambledPool[i], scrambledPool[len(matingPool)-i-1])
		newPop.append(child)

	return newPop

def mutate(tour,rate):
	
	route = tour.tour
	newRoute = []
	for move in route:
		new = []
		for bit in move:
			if random() < rate:
				if bit == '0':
					new.append('1')
				else:
					new.append('0')
			else:
				new.append(bit)
		newMove = ''.join(new)
		newRoute.append(newMove)

	tour.tour = newRoute
	return tour

def mutatePop(population,rate):
	
	mutatedPop = []

	for tour in population:
		mutated = mutate(tour,rate)
		mutatedPop.append(mutated)

	return mutatedPop

def newGeneration(currentGen, eliteSize, rate):
	
	matingPool = selection(currentGen,eliteSize)
	children = breedPop(matingPool,eliteSize)
	nextGen = mutatePop(children,rate)
	return nextGen

def geneticAlgorithm(popSize, eliteSize, mutationRate, generations, population = generatePop(1000)):
	
	pop = population
	firstBest = (pop[rankTours(pop)[0]]).fitness
	print("Jumlah langkah : " + str(firstBest) + " langkah")
	(pop[rankTours(pop)[0]]).presentTour()

	for i in range(generations):
		pop = newGeneration(pop, eliteSize, mutationRate)
		for tour in pop:
			tour.repairVisited()
			tour.tourFitness()

	finalBest = (pop[rankTours(pop)[0]]).fitness
	print("Jumlah langkah : " + str(finalBest) + " langkah")
	(pop[rankTours(pop)[0]]).presentTour()

	return finalBest

#adjust arguments as necessary to run
geneticAlgorithm(1000,50,0.01,100)
