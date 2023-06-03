#pragma once

#include "NNLayer.hh"

class SigmoidActivation: public NNLayer {
    public:
        SigmoidActivation(std::string name);
        ~SigmoidActivation();

        Matrix& forward(Matrix& Z);
        Matrix& backprop(Matrix& sA, float learning_rate = 0.01);

    private:
        Matrix A;

        Matrix Z;
        Matrix dZ;

};