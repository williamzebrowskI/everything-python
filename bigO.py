import timeit
import numpy as np
import matplotlib.pyplot as plt
#Big-O Notation Practice

#O(n + 10) => O(n)
#O(100 * n) => O(n)
#O(50) => O(1)
#O(n2 + n3) => O(n3)
#O(n + n + n + n + n) => O(n)

x = [2, 4, 6, 8, 10, 12]

y = [2, 2, 2, 2, 2, 2]

#plt.plot(x, y, 'b')
#plt.xlabel('Inputs')
#plt.ylabel('Steps')
#plt.title('Constant Complexity')
#plt.show()


def linear_algo(items):
    for item in items:
        print(item)

#linear_algo([4, 5, 6, 8])



def linear_algo(items):
    for item in items:
        print(item)

    for item in items:
        print(item)

#linear_algo([4, 5, 6, 8])

def quadratic_algo(items):
    for item in items:
        for item2 in items:
            print(item, ' ' ,item)

quadratic_algo([4, 5, 6, 8])

plt.plot(x, y, 'b')
plt.xlabel('Inputs')
plt.ylabel('Steps')
plt.title('Linear Complexity')
plt.show()