'''
In this module we are going to create vector class.
whose data members are dimensions of vector. 
Then we will perform arithmatic operations of vector.
'''
class Vector:

    '''
    This class will perform arithmetic operations over vector
    objects and will make the vector object iterable
    '''

    def __init__(self,lst):     #initialize constructor
        self.dim=len(lst)
        self.vec=lst

    def __str__(self):          #to display the values of object
        return str(self.vec)
    
    def __eq__(self,other):     #checking wheather vectors are equal
        return self.vec == other.vec

    def __len__(self):          #to find len of vectors
        return self.dim

    def __getitem__(self,index):    #to get the items
        return  self.vec[index]
        
    def __setitem__(self,index,value):  #to assign the items
        self.vec[index] = value
    
    def __add__(self,other):        #for addition of two vectors
        if len(self) == len(other):
            result=[]
            for index in range(len(self)):
                val=self.vec[index] + other.vec[index]
                result.append(val)
            return Vector(result)
        else:
            raise ValueError("The length of the vectors should be equal")
    
    def __sub__(self,other):        #for subraction of two vectors
        if len(self) == len(other):
            result=[]
            for index in range(len(self)):
                val=self.vec[index] - other.vec[index]
                result.append(val)
            return Vector(result)
        else:
            raise ValueError("The length of the vectors should be equal")

#driver code
def main():

    """
    This function contains the driver code for this program.
    It adds two vectors and subract two vectors.
    """

    v1=Vector([22,33,44,55])
    v2=Vector([3,4,5,6])
    print("v1:",v1)
    print("v2:",v2)
    v3=v1+v2
    print("v1+v2=",v3)
    print("After iterating vector V3:")
    for num in v3:
        print(num,end=" ")
   
    print("\n")
    
    v3=v1-v2
    print("v1-v2=",v3)
    print("After iterating vector V3:")
    for num in v3:
        print(num,end=" ")

if __name__ == '__main__':
    main()
