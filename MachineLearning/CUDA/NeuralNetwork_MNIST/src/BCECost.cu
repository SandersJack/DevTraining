#include "BCECost.hh"
#include "Exception.hh"

#include <math.h>
#include <assert.h>

__global__ void binaryCrossEntropyCost(float* predictions, float* target, float* cost,
    int pred_x_dim, int pred_y_dim){
    
    int row = blockIdx.x * blockDim.x + threadIdx.x;
    int col = blockIdx.y * blockDim.y + threadIdx.y;


    if(row < pred_x_dim && col < pred_y_dim) {
        float partial_cost = target[row * pred_x_dim + col] * logf(predictions[row * pred_x_dim + col])
            + (1.0f - target[row * pred_x_dim + col]) * logf(1.0f - predictions[row * pred_x_dim + col]);
        atomicAdd(cost, - partial_cost / pred_x_dim);
    }
}

__global__ void dBinaryCrossEntropyCost(float* predictions, float* target, float* dY, 
    int pred_x_dim, int pred_y_dim){

    int row = blockIdx.x * blockDim.x + threadIdx.x;
    int col = blockIdx.y * blockDim.y + threadIdx.y;

    if (row < pred_x_dim && col < pred_y_dim) {
        dY[row * pred_x_dim + col] = -1.0 * ( target[row * pred_x_dim + col]/predictions[row * pred_x_dim + col] - (1-target[row * pred_x_dim + col])/(1-predictions[row * pred_x_dim + col]));
    }
}

float BCECost::cost(Matrix predictions, Matrix target){
    assert(predictions.shape.y == target.shape.y);

    float* cost;
    cudaMallocManaged(&cost, sizeof(float));
    *cost = 0.0f;

    dim3 block_size(8,8);
    dim3 num_of_blocks((predictions.shape.x + block_size.x -1)/block_size.x,(predictions.shape.y + block_size.y -1)/block_size.y); // Which will be 1 atm. Will optmise input at somepoint
    binaryCrossEntropyCost<<<num_of_blocks,block_size>>>(predictions.data_device.get(), target.data_device.get(), cost,
    predictions.shape.x,predictions.shape.x);

    cudaDeviceSynchronize();
    Exception::throwIfDeviceErrorOccurred("Cannot compute binary cross entropy cost");

    float cost_value = *cost;
    cudaFree(cost);

    return cost_value;
}

Matrix BCECost::dCost(Matrix predictions, Matrix target, Matrix dY){
    //std::cout << predictions.shape.x << " " << target.shape.x <<std::endl;

    assert(predictions.shape.x == target.shape.x);
    
    dim3 block_size(8,8);
    dim3 num_of_blocks((predictions.shape.x + block_size.x -1)/block_size.x,(predictions.shape.y + block_size.y -1)/block_size.y); // Again very non optimal.
    dBinaryCrossEntropyCost<<<num_of_blocks, block_size>>>(predictions.data_device.get(),target.data_device.get(),dY.data_device.get(), 
    predictions.shape.x, predictions.shape.y);
    Exception::throwIfDeviceErrorOccurred("Cannot compute derivative for binary cross entropy");

    return dY;
}