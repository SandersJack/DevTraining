#pragma once
#include <memory>

struct Shape
{
    size_t x,y;

    Shape(size_t x=1, size_t y=1);
};


class Matrix {
    public:
        Matrix(size_t z_dim = 1, size_t y_dim = 1);
        Matrix(Shape shape);

        Shape shape;

        std::shared_ptr<float> data_device;
        std::shared_ptr<float> data_host; 

        void allocateMemory();
        void allocateMemoryIfNot(Shape shape);

        void copyHostToDevice();
        void copyDeviceToHost();

        float& operator[](const int index);
        const float& operator[](const int index) const; 


    private:

        bool device_allocated;
        bool host_allocated;

        void allocateCUDAMemory();
        void allocateHostMemory();

};