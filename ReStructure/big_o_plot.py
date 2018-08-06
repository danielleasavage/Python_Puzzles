import matplotlib.pyplot as plt
import numpy as np
import math


def O1(n):
    return [1] * len(n)


def OlogN(n):
    return np.log(n)


def ONlogN(n):
    return n * np.log(n)


def ON(n):
    return n


def ON2(n):
    return [math.log(num ** 2) for num in n]


def O2N(n):
    return [math.log(2 ** num) for num in n]


x = range(1, 1000)

plt.figure(figsize=(14, 10))
plt.title('Big O Visualized')
plt.ylim(-1, 50)
plt.xlim(1, 25)

plt.plot(x, O1(x), label='O(1)')
plt.plot(x, OlogN(x), label='O(logN)')
plt.plot(x, ONlogN(x), label='O(NlogN)')
plt.plot(x, ON(x), label='O(N)')
plt.plot(x, ON2(x), label='log of O(N^2)')
plt.plot(x, O2N(x), label='log of O(2^N)')

plt.xlabel('Input Size')
plt.ylabel('Run Time')
plt.grid(True)
plt.legend()
plt.savefig("big_o.png")
plt.show()