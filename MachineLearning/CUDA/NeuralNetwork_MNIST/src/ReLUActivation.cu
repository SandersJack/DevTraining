#include "ReLUActivation.hh"
#include "Exception.hh"

__global__ void reluActivationForward(float* Z, float* A, 
    int Z_x_dim, int Z_y_dim){

    int index = blockIdx.x * blockDim.x + threadIdx.x;

    if(index < Z_x_dim * Z_y_dim){
        A[index] = fmaxf(Z[index], 0);
        //printf("RELU: %i , %f \n", index, Z[index]);
    }
}

__global__ void reluActivationBackprop(float* Z, float* dA, float* dZ, 
    int Z_x_dim, int Z_y_dim) {

    int index = blockIdx.x * blockDim.x + threadIdx.x;

    if(index < Z_x_dim * Z_y_dim) {
        if(Z[index] > 0){
            dZ[index] = dA[index];
        } else {
            dZ[index] = 0;
        }
    }
}

ReLUActivation::ReLUActivation(std::string name){
    this->name = name;
}

ReLUActivation::~ReLUActivation(){

}

Matrix& ReLUActivation::forward(Matrix& Z){
    this->Z = Z;
    A.allocateMemoryIfNot(Z.shape);

    //std::cout << "RRRRRRRr" << std::endl;
    //td::cout << Z.shape.x*Z.shape.y << std::endl;
    //for( int i{0}; i<28*28*100; i++){
    //    std::cout << Z[i] << std::endl;
    //}

    dim3 block_size(256);
    dim3 num_of_blocks((Z.shape.y*Z.shape.x + block_size.x -1)/block_size.x);
    Z.copyHostToDevice();
    reluActivationForward<<<num_of_blocks, block_size>>>(Z.data_device.get(), A.data_device.get(),
    Z.shape.x, Z.shape.y);
    Exception::throwIfDeviceErrorOccurred("Cannot perform ReLU forward propagration.");
    A.copyDeviceToHost();
    //std::cout << "ZZZZZ AFTER"<< std::endl;
    //for(int i{0}; i<28*28*100; i++){
    ///    std::cout << A[i] << std::endl;
    //}

    return A;
}

Matrix& ReLUActivation::backprop(Matrix& dA, float learning_rate) {
    dZ.allocateMemoryIfNot(Z.shape);
    dim3 block_size(256);
    dim3 num_of_blocks((Z.shape.x*Z.shape.y + block_size.x -1)/block_size.x);
    reluActivationBackprop<<<num_of_blocks, block_size>>>(Z.data_device.get(), dA.data_device.get(), dZ.data_device.get(),
    Z.shape.x, Z.shape.y);
    Exception::throwIfDeviceErrorOccurred("Cannot perform ReLU backprop.");

    return dZ;
}