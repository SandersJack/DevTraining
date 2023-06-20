#pragma once 
#include "Matrix.hh"
#include <iostream>

class NNLayer {

    public:
        virtual ~NNLayer() = 0;

        virtual Matrix& forward(Matrix& A) = 0;
        virtual Matrix& backprop(Matrix& dZ, float learning_rate) = 0;

        std::string getName() {return this->name;}

    protected:
        std::string name;
};

inline NNLayer::~NNLayer() {}