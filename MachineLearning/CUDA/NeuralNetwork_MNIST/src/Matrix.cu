#include "Matrix.hh"
#include "Exception.hh"

Shape::Shape(size_t x, size_t y): 
    x(x), y(y) 
{}

Matrix::Matrix(size_t x_dim, size_t y_dim):
    shape(x_dim,y_dim), data_device(nullptr), data_host(nullptr),
    device_allocated(false), host_allocated(false){}

Matrix::Matrix(Shape shape):
    Matrix(shape.x, shape.y){}


void Matrix::allocateHostMemory(){
    if(!host_allocated){
        data_host = std::shared_ptr<float>(new float[shape.x * shape.y],
                                            [&](float* ptr){delete[] ptr;});
        host_allocated = true;
    }
}

void Matrix::allocateCUDAMemory(){
    if(!device_allocated){
        float* device_memory = nullptr;
        cudaMalloc(&device_memory,shape.x*shape.y*sizeof(float));
        Exception::throwIfDeviceErrorOccurred("Cannot allocate CUDA memory for Tensor3D");
        data_device = std::shared_ptr<float>(device_memory, 
                                            [&](float* ptr){cudaFree(ptr);});
        device_allocated = true;
       }
}

void Matrix::allocateMemory(){
    allocateCUDAMemory();
    allocateHostMemory();
}

void Matrix::allocateMemoryIfNot(Shape shape){
    if(!device_allocated && !host_allocated){
        this->shape = shape;
        allocateMemory();
    }
}

void Matrix::copyHostToDevice(){
    if(device_allocated && host_allocated){
        cudaMemcpy(data_device.get(),data_host.get(), shape.x*shape.y*sizeof(float), cudaMemcpyHostToDevice);
        Exception::throwIfDeviceErrorOccurred("Cannot copy host data to CUDA device");
    } else {
        throw Exception("Cannot copy host data to non allocated memory on host");
    }
}

void Matrix::copyDeviceToHost(){
    if(device_allocated && host_allocated){
        cudaMemcpy(data_host.get(),data_device.get(), shape.x*shape.y*sizeof(float), cudaMemcpyDeviceToHost);
    }
}

float& Matrix::operator[](const int index){
    return data_host.get()[index];
}

const float& Matrix::operator[](const int index) const {
    return data_host.get()[index];
}