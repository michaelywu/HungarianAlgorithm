class node:

#Construct a node object
    def __init__(self, cost = 0):
        self.__cost = cost
        self.__row_crossed = False
        self.__column_crossed = False

#Set Functions
    def setCost(self, cost):
        self.__cost = cost

    def setRow(self, row_crossed):
        self.__row_crossed = row_crossed

    def setColumn(self, column_crossed):
        self.__column_crossed = column_crossed

#Get Functions
    
    def getCost(self):
        return self.__cost

    def getRow(self):
        return self.__row_crossed

    def getColumn(self):
        return self.__column_crossed
