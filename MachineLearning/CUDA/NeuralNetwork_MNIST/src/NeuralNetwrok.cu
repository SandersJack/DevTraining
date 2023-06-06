#include "NeuralNetwork.hh"

NeuralNetwork::NeuralNetwork(float learning_rate):
    learning_rate(learning_rate) {

}

NeuralNetwork::~NeuralNetwork(){
    for(auto layer : fLayers){
        delete layer;
    }
}

void NeuralNetwork::addLayer(NNLayer* layer){
    this->fLayers.push_back(layer);
}

Matrix NeuralNetwork::forward(Matrix X){
    Matrix Z = X;

    for (auto layer : fLayers){
        Z = layer->forward(Z);
    }

    Y = Z;
    return Y;
}

void NeuralNetwork::backprop(Matrix predictions, Matrix target){
    dY.allocateMemoryIfNot(predictions.shape);
    Matrix error = bce_cost.dCost(predictions, target, dY);

    // In REVERSE :O
    for (auto it = this->fLayers.rbegin(); it != this->fLayers.rend(); it++){
        error = (*it)->backprop(error, learning_rate);
    }

    cudaDeviceSynchronize();
}

std::vector<NNLayer*> NeuralNetwork::getLayers() const {
    return fLayers;
}