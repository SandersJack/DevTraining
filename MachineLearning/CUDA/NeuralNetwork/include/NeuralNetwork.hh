#pragma once

#include "Matrix.hh"
#include "NNLayer.hh"
#include "BCECost.hh"
#include <vector>

class NeuralNetwork {
    public:
        NeuralNetwork(float learning_rate = 0.01);
        ~NeuralNetwork();

        Matrix forward(Matrix X);
        void backprop(Matrix predictions, Matrix target);

        void addLayer(NNLayer *layer);
        std::vector<NNLayer*> getLayers() const;

    private:
        std::vector<NNLayer*> layers;
        BCECost bce_cost;

        Matrix Y;
        Matrix dY;
        float learning_rate;

};