from NodeClass import node

class HungarianAlgorithm:

    temp_matrix = None
    
    def __init__(self, input_matrix):
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

            temp_matrix = input_matrix
            self.__printMatrix()#print original matrix
            self.__Execute()
            self.__printMatrix()
    def __printMatrix(self):
        print("Matrix: ")
        for row in range(self.__size):
            for column in range(self.__size):
                print(self.__node_matrix[row][column].getCost(), end = ' ')
            print()
    def __printRow(self):
        print("Matrix: ")
        for row in range(self.__size):
            for column in range(self.__size):
                print(self.__node_matrix[row][column].getRow(), end = ' ')
            print()
    def __printColumn(self):
        print("Matrix: ")
        for row in range(self.__size):
            for column in range(self.__size):
                print(self.__node_matrix[row][column].getColumn(), end = ' ')
            print()        
    def __subtractLowestColumn(self,columnNumber):
        minimum = self.__node_matrix[0][columnNumber].getCost()
        for row in range(self.__size):
            if self.__node_matrix[row][columnNumber].getCost() < minimum:
                minimum = self.__node_matrix[row][columnNumber].getCost()
        for row in range(self.__size):
            value = self.__node_matrix[row][columnNumber].getCost()
            value -= minimum
            self.__node_matrix[row][columnNumber].setCost(value)
        #self.__printMatrix()
            
    def __subtractLowestRow(self,rowNumber):
        minimum = self.__node_matrix[rowNumber][0].getCost()
        for column in range(self.__size):
            if self.__node_matrix[rowNumber][column].getCost() < minimum:
                minimum = self.__node_matrix[rowNumber][column].getCost()
        for column in range(self.__size):
            value = self.__node_matrix[rowNumber][column].getCost()
            value -= minimum
            self.__node_matrix[rowNumber][column].setCost(value)
        
    def __ifLineNumber(self):
        
        num_of_zeros = []
        num_of_zeros.append([]) #will load the number of zeroes for each column and row
        num_of_zeros.append([])

        for row in range(self.__size): # clear all the row and column registers to false
            for column in range(self.__size):
                self.__node_matrix[row][column].setRow(False)
                self.__node_matrix[row][column].setColumn(False)
                
        for row in range(self.__size): # counts how many zeros for each column and row
            count_R = 0
            count_C = 0
            for column in range(self.__size):
                if self.__node_matrix[row][column].getCost() == 0:
                    count_R=count_R+1
                if self.__node_matrix[column][row].getCost() == 0:
                    count_C=count_C+1
            num_of_zeros[0].append(count_R)
            num_of_zeros[1].append(count_C)
        #print(num_of_zeros)
           
        #grabs the largest number in the list for the row
        #which represents the row with the most 0s
        maxP=max(num_of_zeros[0])
        state = 0;

        #loop that exits once the rows have no 0s
        while max(num_of_zeros[0])!= 0:
            if state == 0:
                maxP=max(num_of_zeros[0])
                pos = num_of_zeros[0].index(maxP)
                #print (pos, "R")
                for x in range(self.__size):
                    self.__node_matrix[pos][x].setRow(True)
                    if self.__node_matrix[pos][x].getCost() == 0:
                        num_of_zeros[1][x]=num_of_zeros[1][x] - 1
                num_of_zeros[0][pos] = 0
                maxP=max(num_of_zeros[1])
                if max(num_of_zeros[0])== 0:
                    break
                if max(num_of_zeros[0]) > maxP:
                    state = 0
                else:
                    state = 1
                    
            if state == 1:
                maxP=max(num_of_zeros[1])
                pos = num_of_zeros[1].index(maxP)
                #print (pos, "C")
                for x in range(self.__size):
                    self.__node_matrix[x][pos].setColumn(True)
                    if self.__node_matrix[x][pos].getCost() == 0:
                        num_of_zeros[0][x]=num_of_zeros[0][x] - 1
                num_of_zeros[1][pos] = 0
                maxP=max(num_of_zeros[0])
                if max(num_of_zeros[1])== 0:
                    break
                if max(num_of_zeros[1]) > maxP:
                    state = 1
                else:
                    state = 0
        num_of_lines = 0;
        for x in range(self.__size):
            if self.__node_matrix[0][x].getColumn() == True:
                num_of_lines = num_of_lines + 1
            if self.__node_matrix[x][0].getRow() == True:
                num_of_lines = num_of_lines + 1
        if (num_of_lines > self.__size):
            num_of_lines = self.__size
            for row in range(self.__size):
                for col in range(self.__size):
                    self.__node_matrix[row][col].setRow(True)
                    self.__node_matrix[row][col].setColumn(False)
                    
        if num_of_lines == self.__size:
            return True
        else:
            return False
            
    def __SubtractLowestUncoveredRow(self):
        lowestPossibleValues = [] # holds the values that is in uncovered row
        
        for row in range(self.__size): # retrieve the values in the node matrix in uncovered row and 
            for column in range(self.__size):
                if((self.__node_matrix[row][column].getRow() == False) and (self.__node_matrix[row][column].getColumn() == False)):
                    lowestPossibleValues.append(self.__node_matrix[row][column].getCost())
                    #print(self.__node_matrix[row][column].getCost())
                    
        minValue = min(lowestPossibleValues)#smallest value

        for row in range(self.__size): # subtract the minvalue to the uncrossed rows
            for column in range(self.__size):
                if((self.__node_matrix[row][column].getRow() == False)):
                    self.__node_matrix[row][column].setCost(self.__node_matrix[row][column].getCost() - minValue)
        #self.__printMatrix()
        return minValue #return the min value for the AddlowestUncoveredColumn to do         
    def __AddlowestUncoveredColumn(self, minValue = 0):
        
        for row in range(self.__size): # add minimum value to each covered column
            for column in range(self.__size):
                if(self.__node_matrix[row][column].getColumn()):
                    self.__node_matrix[row][column].setCost(self.__node_matrix[row][column].getCost() + minValue)
        #self.__printMatrix()            
    def __Execute(self):

        #Step 1        
        for row in range(self.__size):
            self.__subtractLowestRow(row)
     #Step 2
        for col in range(self.__size):
            self.__subtractLowestColumn(col)
            
        check = True
        while(check):
            #self.__printMatrix()
            ifSameSize = self.__ifLineNumber() #step 3
            #self.__printRow()
           # self.__printColumn()
            if(ifSameSize):# step 4
                check = False #skip step  5 and exit
                #print("Step 5 not passed.")
            else:
                minValue = self.__SubtractLowestUncoveredRow() # step 5 
                self.__AddlowestUncoveredColumn(minValue)
                #self.__printMatrix()
                check = True
        #Algorithm completed

        self.__ParseHungarian()
        
    def __ParseHungarian(self):
        #parses the node matrix to determine the lowest cost

        #determine a combination of zeroes
        #first find all 'solid' zeroes
        col_index = [] # col_index[i] and row_index[i] will hold a location
        row_index = [] # on the matrix where there are zeroes

        num_row_zeros = []
         #will load the number of zeroes for each column and row
        num_col_zeros = []
        
        for row in range(self.__size): # counts how many zeros for each column and row
            count_R = 0
            count_C = 0
            for column in range(self.__size):
                if self.__node_matrix[row][column].getCost() == 0:
                    count_R=count_R+1
                if self.__node_matrix[column][row].getCost() == 0:
                    count_C=count_C+1
            num_row_zeros.append(count_R)
            num_col_zeros.append(count_C)

        print (num_row_zeros)
        print (num_col_zeros)

        #first find all 'solid' zeroes
        #use num_row_zeros and num_row_col to find the 'solid' zeros
        while(max(num_col_zeros) > 1 and max(num_row_zeros) > 1): 
            #finds the locations of 'solid' zeros by row and stores in the col_index and row_index
            for zero in range(len(num_row_zeros)):
                if(num_row_zeros[zero] == 1): # a single zero in this particular row
                    for col in range(self.__size):
                        if(self.__node_matrix[zero][col].getCost() == 0): #for loop searches for that zero
                            row_index.append(zero)
                            col_index.append(col)#hold the location of the zero

                            num_row_zeros[zero] = 0 #erase the zero amount in the index
                            num_col_zeros[col] = 0 #reduce the col zero
            print("Find the row locations")                
            print (num_row_zeros)
            print (num_col_zeros)

            #finds the locations of 'solid' zeros by col and store in the col_index and row_index
            for zero in range(len(num_col_zeros)):
                if(num_col_zeros[zero] == 1): # a single zero in this particular row
                    for row in range(self.__size):
                        if(self.__node_matrix[row][zero].getCost() == 0): #for loop searches for that zero
                            row_index.append(row)
                            col_index.append(zero)#hold the location of the zero

                            num_col_zeros[row] = 0 #erase the zero amount in the index
                            num_row_zeros[zero] = 0#reduce the col zero

            print("Find the col locations")                
            print (num_row_zeros)
            print (num_col_zeros)

        print("Locations")                
        print (row_index)
        print (col_index)
