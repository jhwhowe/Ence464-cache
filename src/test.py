import matplotlib.pyplot as plt
import matplotlib
import numpy as np

nThreads = [0, 2, 4, 6, 8]

time101 = [2.656276, 1.3932416, 0.7481118, 0.8798662, 0.813178]
time201 = [20.2149656, 10.4269054, 5.4204668, 6.7564338, 5.4303318]
time301 = [67.932727, 35.3069764, 18.4517898, 21.177749, 18.003667]
time401 = [161.353186, 81.6959886, 44.3054114, 46.9901438, 45.9307746]


optimisedtimes = [2.216943, 14.361816, 48.402107, 129.95256, 278.212708, 498.594696, 824.667297, 1191.333008, 1781.603882]

threadoptimise = [1.964027, 11.302202, 51.13633, 131.664246, 260.18457, 449.216034, 694.188782, 1021.312073, 1454.10144]

thread1 = [ 2.1418764, 14.0593, 47.951964, 128.6859802, 273.6942322, 483.3055174, 818.3408692, 1192.478589, 1749.057129]
thread2 = [1.609387, 11.1848558, 44.499961, 122.8863558, 259.7989382, 440.7762208, 712.0825074, 1060.164722, 1536.995947]
thread4 = [1.4315054, 11.0602304, 48.4697358, 129.5165192, 247.133496, 423.1864382, 672.9911134, 1000.00614, 1435.53501]
thread6 = [1.455802, 12.7038388, 53.1954834, 129.8481292, 249.5247316, 427.1749148, 679.7364014, 1011.294067, 1442.198681]
thread8 = [1.517945, 13.301106, 53.9337874, 127.1313416, 246.73432, 422.9521056, 675.4720582, 1007.544409, 1448.303272]

opttime101 = [0.2109214,0.1583094,0.145771,0.1433592,0.1430774]
opttime201 = [1.418513,1.1736586,1.0964456,1.2703366,1.3480326]
opttime301 = [4.9074688,4.9216358,4.8624202,5.4447304,5.3961298]
opttime401 = [13.8436366,12.878617,12.897038,12.9061578,13.1617158]



sizes = [101, 201, 301, 401, 501, 601, 701, 801, 901]

iterations =[100, 200, 300, 400, 500, 600]

size101 = [0.1442426,0.2888388,0.4309202,0.5709066,0.7166208,0.8746804]
size201 = [1.0980066,2.2003614,3.2960096,4.393494,5.47857,6.5744788]
size301 = [4.8680352,9.7279502,14.5483908,19.4008592,24.2551032,29.1198578]
size401 = [12.8558938,25.80835,38.6792512,51.5978028,64.5431626,77.3968018]
size501 = [24.6001156,49.2287664,73.9169692,98.9655288,123.2188216,148.363452]
size601 = [42.0232764,84.2771302,126.756267,168.8575774,211.4477388,253.0407074]
size701 = [66.9263444,134.115027,201.3260134,268.8158752,336.0677674,403.4390626]
size801 = [99.5501832,199.7652404,299.3759948,399.8915466,499.5221312,600.136487]
size901 = [143.5261108,287.444696,431.4805358,575.493982,719.7678344,864.3755984]


no_opt_4 = [6.598845,51.838608,179.363937,413.470032,827.640076,1437.982666,2278.071533,3514.946289,4837.54236]
opt_4 = [1.4315054, 11.0602304, 48.4697358, 129.5165192, 247.133496, 423.1864382, 672.9911134, 1000.00614, 1435.53501]


plt.figure(figsize=(13,6))
plt.suptitle("Effect of threading on execution time")
plt.subplot(121)
plt.plot(nThreads, time101, 'o-', label='Size 101',linewidth='2')
plt.plot(nThreads, time201, 'o-', label='Size 201',linewidth='2')
plt.plot(nThreads, time301, 'o-', label='Size 301',linewidth='2')
plt.plot(nThreads, time401, 'o-', label='Size 401',linewidth='2')
plt.ylabel("Time (s)")
plt.xlabel("Number of threads")
plt.title("No compiler optimisations")
plt.legend(loc="best")

plt.subplot(122)
plt.plot(nThreads, opttime101, 'o-',linewidth='2')
plt.plot(nThreads, opttime201, 'o-',linewidth='2')
plt.plot(nThreads, opttime301, 'o-',linewidth='2')
plt.plot(nThreads, opttime401, 'o-',linewidth='2')
plt.ylim(0,180)
plt.ylabel("Time (s)")
plt.xlabel("Number of threads")
plt.title("With compiler optimisations")

plt.figure()
plt.plot(sizes, thread1, 'o-',label="No threads")
#plt.plot(sizes, thread2, 'o-',label="2 threads")
#plt.plot(sizes, thread4, 'o-',label="4 threads")
#plt.plot(sizes, thread6, 'o-',label="6 threads")
plt.plot(sizes, thread4, 'o-',label="8 threads")
plt.ylabel("Time (s)")
plt.xlabel("Cube size")
plt.title("Effect of cube size on execution time")
plt.legend(loc="best")

plt.figure()
plt.plot(sizes, no_opt_4, 'o-',label="No optimisations",linewidth='2')
plt.plot(sizes, opt_4, 'o-',label="Compiler -O3",linewidth='2')
plt.ylabel("Time (s)")
plt.xlabel("Cube size")
plt.title("Effect of compiler optimisation on execution time")
plt.legend(loc="best")


plt.figure()
plt.plot(iterations, size101, 'o-',label="101 cube")
#~ plt.plot(iterations, size201, 'o-',label="201 cube")
plt.plot(iterations, size301, 'o-',label="301 cube")
#~ plt.plot(iterations, size401, 'o-',label="401 cube")
plt.plot(iterations, size501, 'o-',label="501 cube")
#~ plt.plot(iterations, size601, 'o-',label="601 cube")
plt.plot(iterations, size701, 'o-',label="701 cube")
#~ plt.plot(iterations, size801, 'o-',label="801 cube")
plt.plot(iterations, size901, 'o-',label="901 cube")
plt.ylabel("Time (s)")
plt.xlabel("Number of iterations")
plt.title("Effect of the number of iterations on execution time")
plt.legend(loc="best")

stddevs = [0.0069369381,0.0593522175,0.1252721714,0.3589601958,0.3363265838,0.7912358312,0.9578294679,1.1984273054,1.277520836]
means = [1.4315054,11.0602304,48.4697358,129.5165192,247.133496,423.1864382,672.9911134,1000.00614,1435.5350096]

plt.figure()
plt.errorbar(sizes, means, xerr=0, yerr=stddevs)

plt.show()
