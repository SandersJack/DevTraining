#include "RunManager.hh"
#include "InputManager.hh"

#include <iostream>
#include <string>


int main(){
    // Default Parameters
    std::string infile = "config/PlanetsList.dat";
    std::string Mooninfile = "config/MoonsList.dat";
    double timeStep = 86400; //seconds
    double stopTime = 1000; //days

    std::cout << "##########################################################" << std::endl;
    std::cout << "##    Running Orbit Simulation using Parameters: " << "       ##" << std::endl;
    std::cout << "##    Time Step = " << timeStep/(24*60*60) << " days. Total Time = " << stopTime << " days."  << "       ##" << std::endl;
    std::cout << "##########################################################" << std::endl;

    InputManager::GetInstance()->ParsePlanetFile(infile);
    InputManager::GetInstance()->ParsePlanetFile(Mooninfile);
    RunManager *runMan = RunManager::GetInstance();
    runMan->SetTimeStep(timeStep);
    runMan->SetStopTime(stopTime);
    runMan->Init();
    runMan->Run();
    return 0;
}