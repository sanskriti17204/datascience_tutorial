from time import process_time
import numpy as np
import sys


#to calcuate time taken by a list to process
py_list=[i for i in range(10000)]
start_time=process_time()
py_list=[i+5 for i in py_list]
end_time=process_time()
print(end_time-start_time)


#to calculate time taken by numpy array
np_array= np.array([i for i in range (10000)])
start_time=process_time()
np_array += 5
end_time=process_time()
print(end_time-start_time)


py_arr=[0,4,15,98]
np_arr=np.array(py_arr)
print(sys.getsizeof(1)*len(py_arr))   #112
print(np_arr.itemsize*np_arr.size)   #32
