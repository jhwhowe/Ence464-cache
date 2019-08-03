import matplotlib.pyplot as plt
import numpy as np

nThreads = [0, 2, 4, 6, 8, 10]

time101 = [2.656276, 1.3932416, 0.7481118, 0.8798662, 0.813178, 0.7978198]
time201 = [20.2149656, 10.4269054, 5.4204668, 6.7564338, 5.4303318, 5.7950024]
time301 = [67.932727, 35.3069764, 18.4517898, 21.177749, 18.003667, 19.6035778]
time401 = [161.353186, 81.6959886, 44.3054114, 46.9901438, 45.9307746, 44.6789344]


optimisedtimes = [2.216943, 14.361816, 48.402107, 129.95256, 278.212708, 498.594696, 824.667297, 1191.333008, 1781.603882]

threadoptimise = [1.964027, 11.302202, 51.13633, 131.664246, 260.18457, 449.216034, 694.188782, 1021.312073, 1454.10144]

sizes = [101, 201, 301, 401, 501, 601, 701, 801, 901]

plt.figure()
plt.plot(nThreads, time101, 'o-', label='Size 101')
plt.plot(nThreads, time201, 'o-', label='Size 201')
plt.plot(nThreads, time301, 'o-', label='Size 301')
plt.plot(nThreads, time401, 'o-', label='Size 401')
plt.ylabel("Time (s)")
plt.xlabel("Number of threads")
plt.title("Effect of threading on execution time")
plt.legend(loc="best")

plt.figure()
plt.plot(sizes, optimisedtimes, 'o-',label="no threads")
plt.plot(sizes, threadoptimise, 'o-',label="threads")
plt.ylabel("Time (s)")
plt.xlabel("Cube size")
plt.title("Effect of cube size on execution time")
plt.legend(loc="best")


plt.show()
