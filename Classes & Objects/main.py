"""
    Learnign about classes and object by building a Sudoku puzzle solver
"""

#Creating a class
class Board:
    #A class constructor allows for the class to instantiate an object to a customized state
    def __init__(self, board): #self is reference to the instance of the class, board is expected when we create an instance of board
        self.board = board
#Creating an instance of the board class
Board()