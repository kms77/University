import matplotlib.pyplot as plt
import numpy as np
import time

print('Vectorization')

"""

"Vectorization is the art of getting rid of for loops in your code." (Andrew Ng)

numpy provides a series of functions that allow the programmer to perform mathematical 
computations on the elements of the array without having to explicitly loop over the 
array elements; these functions are much more efficient as python delegates these tasks 
to compiled and optimized C code.

A formal definition of vectorization is: "In the context of high-level languages like 
Python, Matlab, and R, the term vectorization describes the use of optimized, pre-compiled 
code written in a low-level language (e.g. C) to perform mathematical operations 
over a sequence of data. This is done in place of an explicit iteration written in the 
native language code." (check this tutorial for details: 
https://www.pythonlikeyoumeanit.com/Module3_IntroducingNumpy/VectorizedOperations.html)

Using for loops to access array elements (when dealing with large data) is highly 
inefficient, as demonstrated in the examples below. Therefore, especially for 
this course, when we'll deal with a lot of training data and large neural network architectures, 
you should always use vectorization when writing your code. Otherwise, it will take a 
very very very :) long time to get your model to perform a single iteration over your training data.

"""

a1 = np.random.rand(1000000)
a2 = np.random.rand(1000000)

t1 = time.time()
dp_vectorized = a1.dot(a2)
time_vectorized = time.time() - t1

t1 = time.time()
dp_loops = 0
for i in range(0, a1.shape[0]):
    dp_loops += a1[i]*a2[i]
time_loops = time.time() - t1

print("dp_vectorized: ", dp_vectorized)
print("dp_loops: ", dp_loops)

print('Time to compute dot product using loops: ', time_loops, 'milliseconds')
print('Time to compute dot product using vectorization: ', time_vectorized, 'milliseconds')
print('Speedup ', time_loops/time_vectorized)

arr_size = []
arr_time_vectorized = []
arr_time_loops = []

for sz in range(100, 1000000, 10000):
    t1 = time.time()
    a1 = np.random.rand(sz)
    a2 = np.random.rand(sz)
    dp_vectorized = a1.dot(a2)
    time_vectorized = time.time() - t1

    t1 = time.time()
    dp_loops = 0
    for i in range(0, a1.shape[0]):
        dp_loops += a1[i]*a2[i]
    time_loops = time.time() - t1
    arr_size.append(sz)

    arr_time_vectorized.append(time_vectorized)
    arr_time_loops.append(time_loops)

plt.plot(arr_size, arr_time_vectorized, label = 'vectorized')
plt.plot(arr_size, arr_time_loops, label='using loops')
plt.legend()
plt.xlabel('array size')
plt.ylabel('execution time (ms)')
plt.show()
