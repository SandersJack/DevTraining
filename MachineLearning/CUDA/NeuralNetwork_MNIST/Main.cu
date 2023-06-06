#include "InputManager.hh"
#include "Matrix.hh"

#include <vector>
#include <iostream>

int main() {
    InputManager *inMan = new InputManager();

    inMan->InitTraningData();

    std::vector<Matrix> trainData = inMan->GetTrainingData();
    std::vector<Matrix> targets = inMan->GetTargets();

    std::cout << trainData.size() << std::endl;
    std::cout << (int)trainData[10].shape.x << std::endl;
}