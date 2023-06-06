#pragma once
#include "Matrix.hh"
#include <vector>

class InputManager {

    public:
        InputManager();
        ~InputManager();

        void InitTraningData();

    private:

        int reverseInt(int i);

        std::vector<Matrix> fTraingData;
        std::vector<Matrix> fTargets;
};