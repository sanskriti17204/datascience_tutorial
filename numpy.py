import numpy as np

ar = np.array([(1,2),(4,5)])
print(ar)
print(ar.shape) #shape of matrix
print(type(ar)) #type of array
arr = np.array([(1,2),(4,5)],dtype=float)  #converts elements into float
print(arr)
print(type(arr))
print(ar*arr)   #multiplication of 2 matrices
print(np.where(ar>2))  #tells on which position are elements greater than 2 placed
print(np.count_nonzero(ar))   #tells the number of non zero elements
print(ar.flat) 
for item in ar.flat:   #flat means not in matrix form
  print(item)
  
  
  
  zeroes = np.zeros((4,5)) #matrix containg all elemts as 0
on_es = np.ones((2,3))  #matrix containg all elemts as 1
identity=np.eye(4)  #identity matrrix
same_el=np.full((5,4),2, dtype=float)  #array of a particular value and dtype to convert into float
print(zeroes)
print(on_es)
print(identity)
print(same_el)


a=np.random.random((2,3))  #generating a random matrix of 2 rows 3 coloumns
print(a)



c=np.random.randint(10,100,(4,5))   #generating a random matrix of 2 rows 3 coloumns consisting of only integers
print(c)
print(c.ndim) #print dimension of matrix
print(c.size)  #prints total number of elements
print(c.dtype)  #prints data type



c.max() #max element in the mtrix
c.min() #min element in the mtrix
c.argmax() #max element is at which place
c.argmin()   #min element is at which place
c.argsort()
c.nbytes
np.sqrt(c)  #takes sqroot of all elements of matrix c
c.sum() #sums all the elements of the matrix


lin_space= np.linspace(1,10,5)   #5 characters between 1 and 10
print(lin_space)

arr_nge= np.arange(1,10,5)  #elements between 1 and 10 with evenly spaced
print(arr_nge)

#diff btw adding 2 lists and 2 np arrays is that in list the 2 lists gets concatenated and in arrays consecutive elements gets add
list1=[1,4,9,8,7]
list2=[1,2,3,9,8,7]
print(list1 + list2)
np_list=np.asarray(list2)    #converting list into  numpy array
print(np_list)
arr1=np.array([(1,2,3),(4,5,6),(7,8,9)])
arr2=np.array([(6,4,3),(1,7,2),(4,9,10)])
print(arr1+arr2)  #add respective elements 
print(arr1-arr2)
print(arr1*arr2)
print(arr1/arr2)
print(np.divide(arr1,arr2))  #another method
trans=np.transpose(arr1)  #to take out transpose
print(trans)
print(arr1.T)   #another method to take out transpose



arr3=np.random.randint(10,30,(2,3))
#print(arr3)
b=arr3.reshape(3,2)   #reshaping a matrix
print(b)



arr3=np.random.randint(10,30,(7,8))
print(arr3)
#axis=0 are the coloumns
#axis=1 are the rows
print(arr3.max(axis=0))  #generates a array containing the maximum elements of each coloumn, same could be done for axis=1
print(arr3.argmax(axis=0))  #generates an array containing the position of the maximum elements of each coloumn, same for rows axis=1
print(arr3.sum(axis=1))  #sums all elements of row-vise
print(arr3.ravel())  #simplifies the matrix



