from random import randint,sample,random
import numpy

class Board:
	'''
	Class for a chessboard with an integer number of rows and columns.
	Includes a method to display the board in the console. self.squares
	contains the board as a nested list populated with the integer 0
	'''
	def __init__(self, rows, columns):
		self.rows = rows
		self.columns = columns
		self.squares = [['00'] * columns for i in range(rows)]

	def __repr__(self):
		print('Current board state: ')
		for i in range(self.rows):
			print(self.squares[i])

class Tour:
	'''
	Class for an individual candidate tour. Instantiates a board for the
	tour using the Board class above. Each move is encoded as a 3-bit binary
	string - details of the encoding can be found in the paper for which
	this algorithm was produced - see header.
	Contains methods isLegalMove(), tourFitness() and generateTour()
	'''
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
		'''
		Tests a proposed move to check for several conditions:
		An output of 'legal' means that the square has not been visited and exists on the board
		An output of 'visited' means that the square exists on the board, but has been visited before
		And and ouput of False means the square does not exist on the board.
		'''
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
		'''
		Generates a candidate knight's tour.
		Move selection is based on random choice of one of 8 possible knight's moves,
		filtered by the isLegalMove method to make sure that they exist on the board.
		Allows for repeated visits to squares as this is merely intended to produce an initial
		population upon which selection, mutation and breeding can occur.
		'''
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
		'''
		Fitness function for genetic algorithm
		Calculates an integer value for fitness between 1 and 63 for each tour,
		representing the total number of legal moves in the tour.
		'''
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
		'''
		Takes a tour that has been produced by crossover breeding
		and repairs the visited list to ensure it is still accurate
		to the new tour list
		'''
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
		'''
		Displays the moves in a tour on the board, filled to
		strings of length 2 for readability. Calls Board.__repr__()
		to present the board for user reading.
		'''
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
	'''
	Generates a new population of a given integer size. 
	Returns the population as a list of Tour objects.
	'''
	population = []
	for i in range(size):
		newTour = Tour((1,1))
		newTour.generateTour()
		population.append(newTour)

	return population

def rankTours(population):
	'''
	Ranks a population of tours based on fitness.
	Returns a list of the indexes of tours in the population,
	sorted by the fitness of the tours.
	'''
	fitnessDict = {}
	for i in population:
		fitnessDict[population.index(i)] = i.tourFitness()
	fitness_sorted = sorted(fitnessDict, key=fitnessDict.get, reverse=True)
	return fitness_sorted

def selection(population,eliteSize):
	'''
	First selects the 10 best-performing candidates and guarantees they will be
	selected at least once for populating the mating pool. 
	The remaining mating candidates are selected weighted by fitness from the 
	population. The resulting list, selected, will include a number of tours
	equal to the original population size.
	'''
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
	'''
	Function to take 2 parent tours and apply crossover breeding
	to produce a new child tour. The currently-legal portion of
	tour 1 is sliced from it and combined with the remainder 
	of tour 2.
	'''
	child = Tour((1,1))
	
	part1 = parent1.tour[:parent1.fitness]
	part2 = parent2.tour[parent1.fitness:]
	newRoute = list.__add__(part1,part2)

	child.tour = newRoute
	return child

def breedPop(matingPool,eliteSize):
	'''
	Applies breed() to a the mating pool of individual tours.
	Automatically carries forward elite tours to the next
	generation before breeding occurs.
	'''
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
	'''
	Applies a mutation factor to a tour, which represents the
	probability of each bit in the move list flipping from 1 to
	0 or vice versa.
	'''
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
	'''
	Applies the mutate() function to an entire population.
	'''
	mutatedPop = []

	for tour in population:
		mutated = mutate(tour,rate)
		mutatedPop.append(mutated)

	return mutatedPop

def newGeneration(currentGen, eliteSize, rate):
	'''
	Creates a new generation of tours.
	Takes as arguments the current generation along
	with the desired size of the elite population
	and the rate of mutation.
	'''
	matingPool = selection(currentGen,eliteSize)
	children = breedPop(matingPool,eliteSize)
	nextGen = mutatePop(children,rate)
	return nextGen

def geneticAlgorithm(popSize, eliteSize, mutationRate, generations, population = generatePop(1000)):
	'''
	Executes the genetic algorithm.
	Takes as arguments:
	Desired population size
	Desired elite group size
	Probability of mutation
	Number of generations
	Initial population which defaults
	to the output of generatePop(1000)
	'''
	pop = population
	firstBest = (pop[rankTours(pop)[0]]).fitness
	print("Best tour from generation 0 of length: " + str(firstBest) + " squares")
	(pop[rankTours(pop)[0]]).presentTour()

	for i in range(generations):
		pop = newGeneration(pop, eliteSize, mutationRate)
		for tour in pop:
			tour.repairVisited()
			tour.tourFitness()

	finalBest = (pop[rankTours(pop)[0]]).fitness
	print("Best tour from final generation of length " + str(finalBest) + " squares")
	(pop[rankTours(pop)[0]]).presentTour()

	return finalBest

#adjust arguments as necessary to run
geneticAlgorithm(1000,50,0.01,100)
