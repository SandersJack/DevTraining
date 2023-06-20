#pragma once
#include "Matrix.hh"
#include <vector>

class InputManager {

    public:
        InputManager();
        ~InputManager();

        void InitTraningData();

        std::vector<Matrix> GetTrainingData(){return fTraingData;}
        std::vector<Matrix> GetTargets(){return fTargets;}

    private:

        int reverseInt(int i);

        std::vector<Matrix> fTraingData;
        std::vector<Matrix> fTargets;
};