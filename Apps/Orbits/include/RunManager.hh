#ifndef RunManager_H
#define RunManager_H 

#include <iostream>

class RunManager {

    public:
        RunManager();
        static RunManager *GetInstance();
        void Test() {std::cout << "HERE"<<std::endl;}

    private:
        static RunManager *fInstance;
};
#endif