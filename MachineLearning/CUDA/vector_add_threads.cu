#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#include <assert.h>
#include <cuda.h>
#include <cuda_runtime.h>

#define N 10000000
#define MAX_ERR 1e-6


__global__ void vector_add(float *out, float *a, float *b, int n){
    int index = threadIdx.x;
    int stride = blockDim.x;
    for(int i = index; i < n; i += stride) {
        out[i] = a[i] + b[i];
        //aprintf("%f",out[i]);
    }
}

int main() {
    float *a, *b, *out;
    float *d_a, *d_b, *d_out;

    // Memory Alocation
    a = (float*)malloc(sizeof(float) * N);
    b   = (float*)malloc(sizeof(float) * N);
    out = (float*)malloc(sizeof(float) * N);

    for(int i = 0; i < N; i++){
        a[i] = 1.0f;
        b[i] = 2.0f;
    }

    // Allocate device memory
    // cudaMalloc(void **devPtr, size_t count);
    // devPtr -> Device pointer 
    // count -> memory  size
    // cudaMemcpy(void *dst, void *src, size_t count, cudaMemcpyKind kind)
    //

    cudaMalloc((void**)&d_a, sizeof(float)*N);
    cudaMalloc((void**)&d_b, sizeof(float)*N);
    cudaMalloc((void**)&d_out, sizeof(float)*N);


    // Transfer data from host to device Memory

    cudaMemcpy(d_a, a, sizeof(float) * N, cudaMemcpyHostToDevice);
    cudaMemcpy(d_b, b, sizeof(float) * N, cudaMemcpyHostToDevice);

    vector_add<<<1,256>>>(d_out, d_a, d_b, N);

    cudaMemcpy(out, d_out, sizeof(float) * N, cudaMemcpyDeviceToHost);

    for(int i = 0; i < N; i++){
        assert(fabs(out[i] - a[i] - b[i]) < MAX_ERR);
    }

    printf("PASSED\n");

    cudaFree(d_a);
    cudaFree(d_b);
    cudaFree(d_out);

    free(a); 
    free(b); 
    free(out);

    return 0;
}