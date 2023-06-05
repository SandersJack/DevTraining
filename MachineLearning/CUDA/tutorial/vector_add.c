#include <stdlib.h>
#include <stdio.h>

#define N 10000000

void vector_add(float *out, float *a, float *b, int n){
    for(int i = 0; i < n; i++) {
        out[i] = a[i] + b[i];
        //printf("%f \n",out[i]);
    }
}

int main() {
    float *a, *b, *out;

    // Memory Alocation
    a = (float*)malloc(sizeof(float) * N);
    b = (float*)malloc(sizeof(float) * N);
    out = (float*)malloc(sizeof(float) * N);

    // Init vector
    for(int i=0; i < N; i++){
        a[i] = 1.0f; b[i] = 2.0f;
    }

    vector_add(out, a, b, N);

}