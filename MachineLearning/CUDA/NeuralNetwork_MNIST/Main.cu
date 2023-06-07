#include "InputManager.hh"
#include "Matrix.hh"
#include "NeuralNetwork.hh"
#include "LinearLayer.hh"
#include "ReLUActivation.hh"
#include "Exception.hh"
#include "BCECost.hh"

#include <vector>
#include <iostream>

float computeAccuracy(const Matrix& predictions, const Matrix& targets);

int main() {
    InputManager *inMan = new InputManager();

    inMan->InitTraningData();

    std::vector<Matrix> trainData = inMan->GetTrainingData();
    std::vector<Matrix> targets = inMan->GetTargets();
    
    BCECost bce_cost;

    NeuralNetwork nn;
    nn.addLayer(new LinearLayer("linear_1", Shape(28*28,1)));
    nn.addLayer(new ReLUActivation("relu_1"));
    nn.addLayer(new LinearLayer("linear_2", Shape(1, 10)));
    nn.addLayer(new ReLUActivation("relu_2"));


    Matrix Y;
    std::cout << "[Main] Start of Training" << std::endl;
    for(int epoch=0; epoch<1; epoch++){
        float cost = 0.0;
        for(int batch=0; batch<trainData.size(); batch++){
            Y = nn.forward(trainData.at(batch));
            nn.backprop(Y, targets.at(batch));
            cost += bce_cost.cost(Y, targets.at(batch));
        }
        

        if (epoch % 1 == 0){
            std::cout << "Epoch: " << epoch << ", Cost:" << cost/trainData.size() << std::endl;
        }
    }
    // Compute accuracy
    Y = nn.forward(trainData.at(0));
    Y.copyDeviceToHost();

    float accuracy = computeAccuracy(Y, targets.at(0));
    std::cout << "Accuracy: " << accuracy << std::endl;

    return 0;
}

float computeAccuracy(const Matrix& predictions, const Matrix& targets) {
    int m = predictions.shape.x;
    int correct_predictions = 0;

    for (int i = 0; i<m; i++) {
        float prediction = predictions[i] > 0.5 ? 1:0;
        if (prediction == targets[i]){
            correct_predictions++;
        }
    }

    return static_cast<float>(correct_predictions)/m;
}