'''
In this module, we create a matrix in which we can add,
sub,multiply and find the determinant of a matrix.
'''

#Importing random module
from random import randint
import copy

def modify(mat,index):
    
    '''
    This function modify a matrix to find the determinant
    '''
    
    cmat=copy.deepcopy(mat)
    cmat=cmat[1:]
    for row in cmat:
        row.pop(index)
    return cmat

def det(mat):
    
    '''
    This function finds the determinant of a matrix.
    this function takes a matrix as input and returns
    determinant.
    '''
    
    if len(mat)==2:
        return (mat[0][0]*mat[1][1]) - (mat[0][1]*mat[1][0])
    else:
        deta=0
        for index in range(len(mat[0])):
            deta+=((-1)**index)*mat[0][index]*det(modify(mat,index))
        return deta

class Matrix:

    '''
    This class implement a Matrix ADT where the instances of Matrix should be able to store a matrix
    of any size. The ADT takes the number of rows and number of columns as arguments
    a function that multiplies two Matrix objects and returns a Matrix. Also gives the functions
    for Addition,Subtraction,Multiplication,Determinant of two matrices.
    '''
    
    def __init__(self,row,col):     #initialize constructor
        self.r=row
        self.c=col
        self.mat=[]
        for row in range(self.r):
            self.mat.append([0]*self.c)
    
    def __str__(self):              #to display the values of object
        return str(self.mat)
    
    def __len__(self):              #to find len of matrix
        return self.r
    
    def __getitem__(self,index):
        return self.mat[index]
    
    def __eq__(self,other):         #checking wheather matrix are equal
        return self.mat == other.mat

    def __setitem__(self,index,value):      #to assign the items
        self.mat[index] = value

    def random_val(self):            #generate the random values for matrix
        for row in range(self.r):
            for col in range(self.c):
                self.mat[row][col]=randint(0,10)
        
    def __add__(self,other):        #addition of two matrix
        if self.r == other.r and self.c == other.c:
            result=[]
            Row=[]
            for row in range(self.r):
                for col in range(self.c):
                    val=self.mat[row][col] + other[row][col]   
                    Row.append(val)
                result.append(Row)
                Row=[]
            return result
        else:
            raise ValueError("The demension of the matrixes should be same")
        
    def __sub__(self,other):        #subraction of two matrix          
        if self.r == other.r and self.c == other.c:
            result=[]
            Row=[]
            for row in range(self.r):
                for col in range(self.c):
                    val=self.mat[row][col] - other[row][col]   
                    Row.append(val)
                result.append(Row)
                Row=[]
            return result
        else:
            raise ValueError("The demension of the matrixes should be same")

    def __mul__(self,other):            #multiplication of two matrix
        if self.c == other.r:
            result=[]
            Row=[]
            for r1 in range(self.r):
                for c2 in range(other.c):
                    sums=0
                    for c1 in range(self.c):
                        sums+=self.mat[r1][c1] * other.mat[c1][c2]
                    Row.append(sums)
                result.append(Row)
                Row=[]
            return result
        else:
            raise ValueError("""no. of columns of matrix 1 is not equal to
                            no. of rows in second matrix""")

    def det(self):              #to find the determinant of matrix
        return det(self.mat)

#driver code
def main():
    
    '''
    This function is used as the driver code for this module.
    this function can add,subtract and multiply two matrix and also
    finds the determinant of a matrix.
    '''
    
    mat1=Matrix(3,3)
    mat2=Matrix(3,3)
    mat1.random_val()
    mat2.random_val()
    print("Matrix1:",mat1,'\n')
    print("Matrix2:",mat2,'\n')

    print("M1+M2=",mat1+mat2,'\n')
    print("M1-M2=",mat1-mat2,'\n')
    print("M1*M2=",mat1*mat2,'\n')
    print("Determinant of M1:",det(mat1))

if __name__ == '__main__':
    main()
