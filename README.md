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
        `positions  --> the representation list as mentioned above implemented as a List.`
        
        `attackingqueens --> list of positions of queens which are attacking  implemented as a List.`
        
        `attackcount --> the number of queens that are attacking another queens. This will serve as a fitness indicator. For any solution of the problem, the attackcount = 0.`

2. **Population
    
   A Population is a list of arrangements (Boards).  This is equivalent to Population in Genetic Algorithm . Implemented as a list of Board objects.

   Attributes: 
        `size -->  number of boards in the population`
        `population --> a collection of boards, each board representing an arrangement of eight queens`
        `fitnessscore --> an overall fitness score of the population - implemented as the minimum value of the number of attacking queens among all the boards`


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
      `genpopulation - A population of the generation`
      `generation - A state of the population in the genetic algorithm cycle. Represented as a number. Initial gen = 1
                    attacking queens among all the boards. If a fitnessscore = 0 for a population, it implies at 
                    least one solution is found`
      `fittestparent1 - a Board object in the population which has the lowest value of attack score. Considered to be fittest parent`
      `fittestparent2 - a Board object in the population which has the 2nd lowest value of attack score. Considered to be second fittest parent`
        
        
