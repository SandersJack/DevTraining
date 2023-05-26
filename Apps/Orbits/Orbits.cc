#include "RunManager.hh"
#include "InputManager.hh"

#include <iostream>
#include <string>


int main(){

    std::string infile = "config/PlanetsList.dat";

    std::cout << "##########################################################" << std::endl;
    std::cout << "##########################################################" << std::endl;

    InputManager::GetInstance()->ParsePlanetFile(infile);
    RunManager *runMan = RunManager::GetInstance();
    runMan->Init();
    runMan->Run();
    return 0;
}