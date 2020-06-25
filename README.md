## Eight Queens Problem Optimization with Genetic Algorithm approach

### Cognizant Data Science Summit 2020
### Author - Joyjit Chowdhury 


#### Problem Statement
Find a solution of the Eight Queens problem with optimization using Genetic Algorithm.

Following is a sample configuration where we have attacking queens:
![image.png](attachment:image.png)



Following is a sample solution of the problem where no queens are attacking each other:

![image.png](attachment:image.png)

#### Problem Formulation
The arrangement of the Eight Queens on a chessboard is a list of 8 integers, all between 0 and 7 both inclusive.
The arragement is called Board in this implementation:

Board = [q0 q1 q2 q3 q4 q5 q6 q7] 

Each index ( 0 to 7 ) in this list represents a column of the chess board.
Each value in the list q[i]  at index [i]  represents the row in the chessboard where queen q[i] is placed in column [i]

Example: 
For the first board displayed above,  the representation is Board = [7,0,2,6,4,1,5,3] 
For the second board displayed above, the representation is Board = [1,3,5,7,2,0,6,4] 
 
#### Solution Implementation

##### Entity representation in the context of Genetic Algorithm

######1. Individual Members

Each arrangement of the Eight queens in a board is represented by a class called Board 
    Board class has the following attributes:
        
        positions  --> the representation list as mentioned above
        attackcount --> the number of queens that are attacking another queen. This will serve as a fitness indicator. For a solution of the problem, the attackcount = 0.
