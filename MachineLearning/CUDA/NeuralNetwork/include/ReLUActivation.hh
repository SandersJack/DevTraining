#include "NNLayer.hh"

class ReLUActivation: public NNLayer {
    public:
        ReLUActivation(std::string name);
        ~ReLUActivation();

        Matrix& forward(Matrix& Z);
        Matrix& backprop(Matrix& sA, float learning_rate = 0.01);

    private:
        Matrix A;

        Matrix Z;
        Matrix dZ;
        
};