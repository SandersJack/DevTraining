#include "RunManager.hh"
#include <iostream>


int main(){

    std::cout << "HELLO" << std::endl;
    //RunManager *runMan = RunManager::GetInstance();
    new RunManager();
    return 0;
}