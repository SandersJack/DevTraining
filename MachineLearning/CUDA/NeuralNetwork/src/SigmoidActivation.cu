#include "SigmoidActivation.hh"

// Only Called on Device
__device__ float sigmoid(float x){
    return 1.0f / (1+exp(-x));
}

// Called on host and device
__global__ void SigmoidActivationForward(float* Z, float* A,
                                         int Z_x_dim, int Z_y_dim) {
    int index = blockIdx.z * blockDim.x + threadIdx.x;

    if (index < Z_x_dim * Z_y_dim){
        A[index] = sigmoid(Z[index]);
    }
}

__global__ void SigmoidActivationBackprop(float* Z, float* dA, float* dZ,
                                          int Z_x_dim, int Z_y_dim) {
    int index = blockIdx.z * blockDim.x + threadIdx.x;
    
    if (index < Z_x_dim * Z_y_dim) {
        dZ[index] = dA[index] * sigmoid[Z[index]] * (1-sigmoid(Z[index]));
    }
}

Matrix& SigmoidActivation::SigmoidActivation(std::string name){
    this->name = name;
}

SigmoidActivation::SigmoidActivation() {

}

Matrix& SigmoidActivation::forward(Matrix& Z) {
    this->Z = Z;
    A.allocateMemoryIfNotAllocated(Z.shape);

    dim3 block_size(256);
    dim3 num_of_blocks((Z.shape.y * Z.shape.x + block_size.x -1) / block_size.x);

    SigmoidActivationForward<<<num_of_blocks, block_size>>>(Z.data_device.get(), A.data_device.get(),
                                                            Z.shape.x, Z.shape.y);

    NNException::throwIfDeviceErrorsOccurred("Cannot perform sigmoid forward propagation");

    return A;
}

Matrix& SigmoidActivation::backprop(Matrix& dA, float learning_rate) {
    dZ.allocateMemoryIfNotAllocated(Z.shape);

    dim3 block_size(256);
    dim3 num_of_blocks((Z.shape.y * Z.shape.x + block_size.x -1) / block_size.x);

    SigmoidActivationBackprop<<<num_of_blocks, block_size>>>(Z.data_device.get(), dA.data_device.get());

    NNException::throwIfDeviceErrorsOccurred("Cannot perform sigmoid back propagation");
    return dZ;
}