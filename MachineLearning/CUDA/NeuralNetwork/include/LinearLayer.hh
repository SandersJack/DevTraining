#pragma once

#include "NNLayer.hh"
#include "Shape.hh"
#include "Matrix.hh"

class LinearLayer: public NNLayer {

    public:
        LinearLayer(std::string name, Shape W_shape);
        ~LinearLayer();

        Matrix& forward(Matrix& A);
        Matrix& backprop(Matrix& dZ, float learning_rate = 0.01);

        int getXDim() const;
        int getYDim() const;

        Matrix getWeightsMatrix() const;
        Matrix getBiasVector() const;

    private:
        const float weights_init_threshold = 0.01;

        Matrix W;
        Matrix b;

        Matrix Z;
        Matrix A;
        Matrix dA;

        void initBiasWithZeros();
        void initWeightsRand();

        void computeAndStoreBackpropError(Matrix& dZ);
        void computeAndStoreLayerOutput(Matrix& A);
        void computeAndStoreBackpropOutput(Matrix& dZ);
        void updateWeights(Matrix& dZ, float learning_rate);
        void updateBias(Matrix& dZ, float learning_rate);

};