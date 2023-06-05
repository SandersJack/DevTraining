#pragma once
#include "Matrix.hh"
#include <vector>

class CoordinatesDataset {
    public:
        CoordinatesDataset(size_t batch_size, size_t number_of_batches);

        int getNumOfBatches();
        std::vector<Matrix>& getBatches();
        std::vector<Matrix>& getTargets();

    private:
        size_t batch_size;
        size_t number_of_batches;

        std::vector<Matrix> batches;
        std::vector<Matrix> targets;

};