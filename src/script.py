import subprocess

def run_iterations(iterations, size, f, numcores, runs):

	size = str(size)
	numcores = str(numcores)
	print("%s cube %s iterations" % (size, iterations))
	f.write("%s," % size)
	for i in range(runs):
		a = subprocess.check_output(["./poisson_test", size, iterations, numcores])
		f.write(a)
		f.flush() 
		print("%d: %s" % (i, a))
	f.write("\n")


f = open("runtimes.csv", "w")

iterations = "100"
runs = 5

numthreads = 4
#~ print("\n Using %d threads \n" % numthreads)
#~ f.write("%d\n" % numthreads)	

#~ run_iterations(iterations, 101, f, numthreads, runs)
#~ run_iterations(iterations, 201, f, numthreads, runs)
#~ run_iterations(iterations, 301, f, numthreads, runs)

for i in range(0, 5):
	numthreads = 2 * i
	print("\n Using %d threads \n" % numthreads)
	f.write("%d\n" % numthreads)

	run_iterations(iterations, 101, f, numthreads, runs)
	run_iterations(iterations, 201, f, numthreads, runs)
	run_iterations(iterations, 301, f, numthreads, runs)
	run_iterations(iterations, 401, f, numthreads, runs)
	#~ run_iterations(iterations, 501, f, numthreads, runs)
	#~ run_iterations(iterations, 601, f, numthreads, runs)
	#~ run_iterations(iterations, 701, f, numthreads, runs)
	#~ run_iterations(iterations, 801, f, numthreads, runs)
	#~ run_iterations(iterations, 901, f, numthreads, runs)
		

		
		
f.close();
