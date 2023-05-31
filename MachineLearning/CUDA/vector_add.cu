#include <stdlib.h>
#include <stdio.h>

#define N 10000000

__global__ void vector_add(float *out, float *a, float *b, int n){
    for(int i = 0; i < n; i++) {
        out[i] = a[i] + b[i];
        //aprintf("%f",out[i]);
    }
}

int main() {
    float *a, *b, *out;
    float *d_a;

    // Memory Alocation
    a = (float*)malloc(sizeof(float) * N);

    // Allocate device memory
    // cudaMalloc(void **devPtr, size_t count);
    // devPtr -> Device pointer 
    // count -> memory  size
    // cudaMemcpy(void *dst, void *src, size_t count, cudaMemcpyKind kind)
    //

    cudaMalloc((void**)&d_a, sizeof(float)*N);

    // Transfer data from host to device Memory

    cudaMemcpy(d_a, a, sizeof(float) * N, cudaMemcpyHostToDevice);

    vector_add<<<1,1>>>(out, d_a, b, N);

    cudaFree(d_a);
    free(a);
    return 0;
}