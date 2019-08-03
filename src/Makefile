all: poisson_test

poisson_test: poisson_test.cpp poisson.cpp
	g++ -O3 -std=c++11 -g3 -pthread -o $@ $^
	cp $@ /tmp

clean:
	rm poisson_test

