#include "BCECost.hh"
#include "Exception.hh"

#include <math.h>
#include <assert.h>

__global__ void binaryCrossEntropyCost(float* predictions, float* target, int size, float* cost){
    int index = blockIdx.x * blockDim.x + threadIdx.x;

    if(index < size) {
        float partial_cost = target[index] * logf(predictions[index])
            + (1.0f - target[index]) * logf(1.0f - predictions[index]);
        atomicAdd(cost, - partial_cost / size);
    }
}

__global__ void dBinaryCrossEntropyCost(float* predictions, float* target, float* dY, int size){
    int index = blockIdx.x * blockDim.x + threadIdx.x;

    if (index < size) {
        dY[index] = -1.0 * ( target[index]/predictions[index] - (1-target[index])/(1-predictions[index]));
    }
}

float BCECost::cost(Matrix predictions, Matrix target){
    assert(predictions.shape.y == target.shape.y);

    float* cost;
    cudaMallocManaged(&cost, sizeof(float));
    *cost = 0.0f;

    dim3 block_size(256);
    dim3 num_of_blocks((predictions.shape.x + block_size.x -1)/block_size.x); // Which will be 1 atm. Will optmise input at somepoint
    binaryCrossEntropyCost<<<num_of_blocks,block_size>>>(predictions.data_device.get(), target.data_device.get(), predictions.shape.x, cost);

    cudaDeviceSynchronize();
    Exception::throwIfDeviceErrorOccurred("Cannot compute binary cross entropy cost");

    float cost_value = *cost;
    cudaFree(cost);

    return cost_value;
}

Matrix BCECost::dCost(Matrix predictions, Matrix target, Matrix dY){
    //std::cout << predictions.shape.x << " " << target.shape.x <<std::endl;

    assert(predictions.shape.x == target.shape.x);
    
    dim3 block_size(256);
    dim3 num_of_blocks((predictions.shape.x + block_size.x -1)/block_size.x); // Again very non optimal.
    dBinaryCrossEntropyCost<<<num_of_blocks, block_size>>>(predictions.data_device.get(),target.data_device.get(),dY.data_device.get(), predictions.shape.x);
    Exception::throwIfDeviceErrorOccurred("Cannot compute derivative for binary cross entropy");

    return dY;
}