# Eight Queens Problem Optimization with Genetic Algorithm approach

*Cognizant Data Science Summit 2020*
*Author - Joyjit Chowdhury* 


## Problem Statement
Find a solution of the Eight Queens problem with optimization using Genetic Algorithm.

Following are sample configurations - 

![Alt Text](/boards_examples.png)

## Problem Formulation
The arrangement of the Eight Queens on a chessboard is a list of 8 integers, all between 0 and 7 both inclusive.
The arragement is called Board in this implementation:

Board = [q0 q1 q2 q3 q4 q5 q6 q7] 

Each index ( 0 to 7 ) in this list represents a column of the chess board.
Each value in the list q[i]  at index [i]  represents the row in the chessboard where queen q[i] is placed in column [i]

Examples of board represenations in the figure shown above : 

Index : 0  --> Board: 2,4,7,3,0,6,1,5 --> Attacking Queens Count: 0
Index : 1  --> Board: 6,7,4,1,5,0,2,3 --> Attacking Queens Count: 5
Index : 2  --> Board: 0,6,2,7,1,4,3,5 --> Attacking Queens Count: 5
Index : 3  --> Board: 3,6,4,5,1,0,2,7 --> Attacking Queens Count: 5
Index : 4  --> Board: 6,5,2,1,7,4,0,3 --> Attacking Queens Count: 5

## Implementation

### Entity representations in the context of Genetic Algorithm

1. **Board

   An arrangement of 8 queens on a board. This is equivalent to an Individual (or a Gene) in Genetic Algorithm 
    
   Attributes: 
        positions  --> the representation list as mentioned above implemented as a List.        
        attackingqueens --> list of positions of queens which are attacking  implemented as a List.        
        attackcount --> the number of queens that are attacking another queens. This will serve as a fitness indicator. For any solution of the problem, the attackcount = 0.

2. **Population
    
   A Population is a list of arrangements (Boards).  This is equivalent to Population in Genetic Algorithm . Implemented as a list of Board objects.

   Attributes: 
        size -->  number of boards in the population
        population --> a collection of boards, each board representing an arrangement of eight queens
        fitnessscore --> an overall fitness score of the population - implemented as the minimum value of the number of attacking queens among all the boards


3. **Generation

   Generation is a driver class which runs the steps of the Genetic Algorithm Flow 
              This class has the methods for each step in a Genetic Algorithm
              Step 1 - Initialize a random population of a given size. This is the first generation. 
              Step 2 - Generate fitness score of the population for the current generation
              Step 3 - Until the desired fitness score of the generation is reached (which is Zero for this implementation)
                       Execute steps 4 through 7. If desired fitness score is reached, the topmost board is the solution,
              Step 4 - SELECTION - pick the fittest individuals (boards) - this would be the top two boards in the population
              Step 5 - CROSSOVER - pick and swap a subset of positions between two fittest individuals (parent boards) 
                       to produce two children. The subset can be controlled by a crossover point index. 
              Step 6 - MUTATION - do a random swap of positions within each children based on a probability of number
                       of positions that flips
              Step 7 - EVOLVE - update the weakest individuals (last two boards) with the two children generated in step 6
                       if the fitness score (attackscore) of the children are better (lower) than the weakest individuals
              
   Attributes:  
      genpopulation - A population of the generation
      generation - A state of the population in the genetic algorithm cycle. Represented as a number. Initial gen = 1
                    attacking queens among all the boards. If a fitnessscore = 0 for a population, it implies at 
                    least one solution is found
      fittestparent1 - a Board object in the population which has the lowest value of attack score. Considered to be fittest parent
      fittestparent2 - a Board object in the population which has the 2nd lowest value of attack score. Considered to be second fittest parent
        

### Logic of determining attacks using native Numpy Matrix Operations ( WITHOUT USING FOR LOOPS )

   Basic logic :  Any two queens q[i] and q[j] in positions i and j  (q[i] != q[j], meaning they are not on same row) attack each other if 
                       abs(q[i] - q[j]) = abs (i - j)   where abs is the absolute value function
                  In other words, two queens attack each other if the difference in their row positions is same as the difference in their column positions.
    
   The for loop way:
   
      for i in 0:7
         for j in 0:7
            attack[i,j] = 1 if abs(q[i] - q[j]) = abs (i - j) and i!=j else 0
            
    
   Use of numpy native matrix multiplication to determine attacking queens:
   
      rowdist = abs(np.tile(q,(8,1)) - np.tile(q).transpose())   # row distances of queens from each other
      indexdist = abs(np.tile(range(8),(8,1)) - np.tile(range(8),(8,1)).transpose())  # column distances of queens from each other
      attackmatrix = (rowdist == indexdist)   # attack is true when rowdist = columndist
      attackmatrix = attackmatrix.astype(int) * np.invert(np.identity(8,dtype = bool)).astype(int)   # ignore attack on itself 
      attackvector = np.dot(attackmatrix,np.ones(8, dtype = int))
      
  Example of the matrix multiplication apprach on q = [0,6,3,7,1,4,2,5]
  
      ![Alt Text](/attack_logic.png)
      
      
## Evolution Process

   The evolution process executes all the steps of the genetic algorithm and returns a generation object for which a solution is found ie. the fittest parent has score 0.
   
            initializegeneration()
            while True:                
                selectfittest()
                crossover(crosspoint = crosspoint)
                mutate(mutationrate = mutationrate)
                merge()
                if population.fitnessscore == 0:  
                    # solution is found, return the current generation
                    selectfittest()
                    return self               
                if generation == maxgenerations:
                    # No solution is found in the maximum allowed generations
                    return None   
                    
                    
## Assumptions

1. The population initialization is not entirely random but a permutation of integers between 0 to 7. No numbers are repeated.
2. Fitness of a generation is done using rank based on number of attacking queens. The board with the lowest number of attacking queens gets the highest rank.
3. Crossover point, mutation rate, population size and number of maximum generations are inputs to the problem. 
