from NodeClass import node

class HungarianAlgorithm:
    
    def __init__(self, n = 1):
        if len(input_matrix)!=len(input_matrix[0]):
            print("Please enter a valid n x n sized matrix")
        else:
            self.__size = len(input_matrix)
            print("You have entered a valid ",self.__size,"x",self.__size,"matrix")
            #create 2d list of nxn nodes
            self.__node_matrix = [[node() for i in range(self.__size)] for j in range(self.__size)]
            #user input of nxn matrix values
            for row in range(self.__size):
                for column in range(self.__size):
                    #cost = eval(input("Enter a value and press Enter: "))
                    self.__node_matrix[row][column].setCost(input_matrix[row][column])
            self.__printMatrix()
    def __printMatrix(self):
        print("Matrix: ")
        for row in range(self.__size):
            for column in range(self.__size):
                print(self.__node_matrix[row][column].getCost(), end = '')
            print()
                
    #def __subtractLowestColumn(self,columnNumber):

    #def __subtractLowestRow(self,rowNumber):

    #def __ifLineNumber(self):

    def __SubtractLowestUncoveredRow(self):
        lowestPossibleValues = [] # holds the values that is in uncovered row
        
        for row in range(self.__size): # retrieve the values in the node matrix in uncovered row and 
            for column in range(self.__size):
                if(!(self.__node_matrix[row][column].getRow) & !(self.__node_matrix[row][column].getColumn)):
                    lowestPossibleValues.append(self.__node_matrix[row][column])
                    
         minValue = min(lowestPossibleValues)#smallest value

         for row in range(self.__size): # subtract the minvalue to the uncrossed rows
            for column in range(self.__size):
                if(!(self.__node_matrix[row][column].getRow)):
                    self.__node_matrix[row][column] = self.__node_matrix[row][column] - minValue

        return minValue #return the min value for the AddlowestUncoveredColumn to do         
    def __AddlowestUncoveredColumn(self, minValue = 0):
        
        for row in range(self.__size): # add minimum value to each covered column
            for column in range(self.__size):
                if(self.__node_matrix[row][column].getColumn):
                    self.__node_matrix[row][column] = self.__node_matrix[row][column] + minValue
                    
    def Execute(self):

        #Step 1
        for col in range(self.__size):
            self.__subtractLowestColumn(col)
        #Step 2        
        for row in range(self.__size):
            self.__subtractLowestRow(row)

        check = True
        while(check):
            ifSameSize = self.__ifLineNumber() #step 3
            if(ifSameSize):# step 4
                check = False #skip step  5 and exit
            else:
                minValue = self.__SubtractLowestUncoveredRow() # step 5 
                self.__AddlowestUncoveredColumn(minValue)
                check = True

        #Algorithm completed

        #parse the node matrix and process the data
        
