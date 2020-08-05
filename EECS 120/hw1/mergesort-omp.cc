/**
 *  \file mergesort.cc
 *
 *  \brief Implement your mergesort in this file.
 *	\Mohammed Haque
 *	\62655407
 *	\4/25/20
 */

#include <assert.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <omp.h>
#include <bits/stdc++.h>
#include <math.h>

#include "sort.hh"

void pmergesort(keytype* A, keytype *tmp, int l, int r, bool alternate);
void mergesort(keytype* A, keytype *tmp, int l, int r, bool alternate);

void pmerge(keytype *A, keytype *tmp, int la, int ra, int lb, int rb, int p);
void merge(keytype *A, keytype *tmp, int la, int ra, int lb, int rb, int p);

int binary_search(keytype* A, int l, int r, int v);

void swap(int &a, int &b);

void
mySort (int N, keytype* A)
{
  /* Lucky you, you get to start from scratch */
	if(N <= 1)	return;
	
	keytype *tmp = newCopy (N, A);

	bool alternate = true;
	// Have to pass this variable because I noticed only half of the array was being sorted
	// and that half was repeated to take up entire array space. Once I made it so that 
	// the merge will actually read from and write to both array A and tmp instead of just
	// array A I saw that the merge was functioning correctly. Have to think of array A as 
	// first half of inputted array and array tmp as the second half.

	// Uncommenting the lines below will make it so that sorting is always faster than quicksort.
	// Right now sorting is only faster for numbers greater than around 500000 and below that is slower
	// most likely because of simply calling pragma omp parallel takes too much time for small 
	// numbers of N. Uncommenting will make sorting purely sequential for N <= 500000

	// const int nlimit = 500000;
	// if(N > nlimit){
	#pragma omp parallel
    {
    	#pragma omp master 
		pmergesort(A, tmp, 0, N-1, alternate);
	}
	// }
	// else{
	// 	mergesort(A, tmp, 0, N-1, alternate);
	// }
}

void pmergesort(keytype* A, keytype *tmp, int l, int r, bool alternate){
	
	const int nlimit = 500000;

	if(r == l){
		if(alternate)	A[l] = tmp[l];
		return;
	}

	if(r - l + 1 <= nlimit){
		mergesort(A,tmp,l,r,alternate);
		return;
	}

    int m = (r+l)/2; 
	#pragma omp task
    pmergesort(A, tmp, l, m, !alternate); 
    pmergesort(A, tmp, m+1, r, !alternate); 
	#pragma omp taskwait

    if(alternate)	pmerge(A, tmp, l, m, m+1, r, l);
    else	pmerge(tmp, A, l, m, m+1, r, l);
}

void mergesort(keytype* A, keytype *tmp, int l, int r, bool alternate){
	
	if (l < r){ 
        int m = (r+l)/2;
        mergesort(A, tmp, l, m, !alternate); 
        mergesort(A, tmp, m+1, r, !alternate); 

        if(alternate)	merge(A, tmp, l, m, m+1, r, l);
        else	merge(tmp, A, l, m, m+1, r, l);
    }
}

void pmerge(keytype *A, keytype *tmp, int la, int ra, int lb, int rb, int p){

	int Na = ra - la + 1;
	int Nb = rb - lb + 1;
	const int nlimit = 500000;

	if(Na + Nb <= nlimit){
		merge(A, tmp, la, ra, lb, rb, p);
		return;
	}

	if(Na < Nb){
		swap(la, lb);
		swap(ra, rb);
		swap(Na, Nb);
	}
	if(Na == 0)	return;

	int v = (la+ra)/2;
	int k = binary_search(tmp, lb, rb, tmp[v]);
	int q = p + (v - la) + (k - lb);

	A[q] = tmp[v];
	#pragma omp task
	pmerge(A, tmp, la, v-1, lb, k-1, p);
	pmerge(A, tmp, v+1, ra, k, rb, q+1);
	#pragma omp taskwait
}

void merge(keytype *A, keytype *tmp, int la, int ra, int lb, int rb, int p){
	
	int q = p + (ra - la) + (rb - lb) + 1;
	for(p; p <= q; ++p){
		if(la > ra)	A[p] = tmp[lb++];
		else if(lb > rb)	A[p] = tmp[la++];
		else	A[p] = (tmp[la] < tmp[lb])	? tmp[la++] : tmp[lb++];
	}
}

int binary_search(keytype* A, int l, int r, int v){

	int low = l;
    int high = (l>r+1) ? l : r+1;

    while(low < high){
        int mid = (low + high) / 2;
        if(v <= A[mid])	high = mid;
        else	low = mid + 1; 
    }
    return high;
}

void swap(int &a, int &b){

	int t = a;
	a = b;
	b = t;
}
/* eof */
