# Eight Queens Problem Optimization with Genetic Algorithm approach

** Cognizant Data Science Summit 2020 **
** Author - Joyjit Chowdhury ** 


### Problem Statement
Find a solution of the Eight Queens problem with optimization using Genetic Algorithm.

Following are sample configurations - 

![Alt Text](/boards_examples.png)

### Problem Formulation
The arrangement of the Eight Queens on a chessboard is a list of 8 integers, all between 0 and 7 both inclusive.
The arragement is called Board in this implementation:

Board = [q0 q1 q2 q3 q4 q5 q6 q7] 

Each index ( 0 to 7 ) in this list represents a column of the chess board.
Each value in the list q[i]  at index [i]  represents the row in the chessboard where queen q[i] is placed in column [i]

Example: 
For the first board displayed above,  the representation is Board = [7,0,2,6,4,1,5,3] 
For the second board displayed above, the representation is Board = [1,3,5,7,2,0,6,4] 
 
#### Solution Implementation

##### Entity representations in the context of Genetic Algorithm

1. ###### Board

   An arrangement of 8 queens on a board. This is equivalent to an Individual (or a Gene) in Genetic Algorithm 
    
   Attributes: 


2. ###### Population
    
   A Population is a list of arrangements (Boards).  This is equivalent to Population in Genetic Algorithm  

3. ###### Evolution

   Evolution is a driver class which runs the entire Genetic Algorithm Flow 

    Board class has the following attributes:
        
        positions  --> the representation list as mentioned above
        attackcount --> the number of queens that are attacking another queen. This will serve as a fitness indicator. For a solution of the problem, the attackcount = 0.
