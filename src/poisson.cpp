/// Solve Poisson's equation for a rectangular box with Dirichlet
/// boundary conditions on each face.
/// \param source is a pointer to a flattened 3-D array for the source function
/// \param potential is a pointer to a flattened 3-D array for the calculated potential
/// \param xsize is the number of elements in the x-direction
/// \param ysize is the number of elements in the y-direction
/// \param zsize is the number of elements in the z-direction
/// \param delta is the voxel spacing in all directions
/// \param numiters is the number of iterations to perform
/// \param numcores is the number of CPU cores to use.  If 0, an optimal number is chosen
/// \return 0 on success.

#include <stdio.h>
#include <stdlib.h>
#include <thread>
#include <vector>
#include <time.h>


int calc_index(int i, int j, int k, int xsize, int ysize) {
	// source[i, j, k] is accessed with source[((k * ysize) + j) * xsize + i]
	
	return ((k * ysize) + j) * xsize + i;
}
	

int poisson_iterate (double * __restrict__ source, double *__restrict__ potential,
                       unsigned int xsize,  unsigned int ysize, unsigned int zsize,
                       double delta, double* __restrict__ new_potential, unsigned int start, unsigned int end)
{
	int index, k, j, i;
	double tmp1,tmp2,tmp3,tmp4,tmp5,tmp6;
	double deltaSquared = delta * delta;
	
		for (k = start; k < end; k++) {
			for (j = 1; j < ysize - 1; j++) {
				for (i = 1; i < xsize - 1; i++) {
													
					tmp1 = potential[calc_index(i+1, j, k, xsize, ysize)];
	
					tmp2 = potential[calc_index(i-1, j, k, xsize, ysize)];

					tmp3 = potential[calc_index(i, j+1, k, xsize, ysize)];

					tmp4 = potential[calc_index(i, j-1, k, xsize, ysize)];

					tmp5 = potential[calc_index(i, j, k+1, xsize, ysize)];

					tmp6 = potential[calc_index(i, j, k-1, xsize, ysize)];
					
					index = calc_index(i, j, k, xsize, ysize);
					new_potential[index] = (tmp1 + tmp2 + tmp3 + tmp4 + tmp5 + tmp6 - deltaSquared * source[index]) * 1.6666667;
					//printf("%d, %d, %d, %f\n", i, j, k, potential[((k * ysize) + j) * xsize + i]);
				}			
			}
		}
}


int poisson_dirichlet (double * __restrict__ source, double *__restrict__ potential,
                       unsigned int xsize,  unsigned int ysize, unsigned int zsize,
                       double delta, unsigned int numiters, unsigned int numcores)
{
	struct timespec tp_i;
	struct timespec tp_f;

	int n, i;
	
	//~ int start1 = 1;
	//~ int start2 = (xsize / 4) + 1;
	//~ int start3 = (xsize / 2) + 1;
	//~ int start4 = (3 * xsize / 4) + 1;
	//~ int end1 = (xsize / 4);
	//~ int end2 = (xsize / 2) ;
	//~ int end3 = (3 * xsize / 4);
	//~ int end4 = xsize - 1;

	//double deltaSquared = delta * delta;
	
	if(numcores == 0){
		numcores = 1; //The number that I got running nproc in terminal :)
	}
	
	double* new_potential = (double *)calloc(xsize * ysize * zsize, sizeof(*potential));
	//~ prev_potential = potential;
	
	clock_gettime ( CLOCK_REALTIME, &tp_i );
	
	for (n = 0; n < numiters; n++) {
		//~ printf("iteration %d\n", n + 1);
		
		std::vector<std::thread> threads;
		
		for (i = 0; i < numcores; ++i) {
			int start = (i * xsize / numcores) + 1;
			int end = (i + 1) * xsize / numcores - 1;
			threads.push_back(std::thread(poisson_iterate, source, potential, xsize, ysize, zsize, delta,
							  new_potential, start, end));
		}
		
		for (auto& thread : threads) {
			thread.join();
		}
		
		//~ std::thread thread1(poisson_iterate, source, potential, xsize, ysize, zsize, delta,
                       //~ new_potential, start1, end1);	
 		//~ std::thread thread2(poisson_iterate, source, potential, xsize, ysize, zsize, delta,
                       //~ new_potential, start2, end2);
        //~ std::thread thread3(poisson_iterate, source, potential, xsize, ysize, zsize, delta,
                       //~ new_potential, start3, end3);	
 		//~ std::thread thread4(poisson_iterate, source, potential, xsize, ysize, zsize, delta,
                       //~ new_potential, start4, end4);
                       
        //~ thread1.join();
        //~ thread2.join();                	
        //~ thread3.join();
        //~ thread4.join();
			
			
			//~ for (j = 1; j < ysize - 1; j++) {
				//~ for (i = 1; i < xsize - 1; i++) {
													
					//~ tmp1 = potential[calc_index(i+1, j, k, xsize, ysize)];
	
					//~ tmp2 = potential[calc_index(i-1, j, k, xsize, ysize)];

					//~ tmp3 = potential[calc_index(i, j+1, k, xsize, ysize)];

					//~ tmp4 = potential[calc_index(i, j-1, k, xsize, ysize)];

					//~ tmp5 = potential[calc_index(i, j, k+1, xsize, ysize)];

					//~ tmp6 = potential[calc_index(i, j, k-1, xsize, ysize)];
					
					//~ index = calc_index(i, j, k, xsize, ysize);
					//~ new_potential[index] = (tmp1 + tmp2 + tmp3 + tmp4 + tmp5 + tmp6 - deltaSquared * source[index]) * 0.166666667;
					// printf("%d, %d, %d, %f\n", i, j, k, potential[((k * ysize) + j) * xsize + i]);
				//~ }			
			//~ }
		//}
		
		//swap the pointers of the first and second array;
		double* temp = new_potential;
		new_potential = potential;
		potential = temp;
	
	}
	
	clock_gettime ( CLOCK_REALTIME, &tp_f );
	
	long seconds = tp_f.tv_sec - tp_i.tv_sec;
	long nanoseconds = tp_f.tv_nsec - tp_i.tv_nsec;
	float sec_f = (float) seconds;
	float nano_f = (float) nanoseconds;
	nano_f = nano_f / 1000000000;
	float sec_nano_f = sec_f + nano_f;
	
	printf("%f,",sec_nano_f);
	
	free(new_potential);

    return 0;
}
