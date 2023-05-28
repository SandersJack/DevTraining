#include "RunManager.hh"
#include "InputManager.hh"

#include <iostream>
#include <string>


int main(int argc, char* argv[]){
    // Default Parameters
    std::string infile = "config/PlanetsList.dat";
    std::string Mooninfile = "config/MoonsList.dat";
    std::string Satinfile = "config/SatelliteList.dat";
    double timeStep = 86400; //seconds
    double stopTime = 1000; //days

    // Parse inputs
    for (int i = 1; i < argc; i++)
    {  
        if (i + 1 != argc)
        {
            if (strcmp(argv[i], "-Ts") == 0) // TimeStep
            {                 
                timeStep = std::stod(argv[i + 1]);
                i++;
            } 
            if (strcmp(argv[i], "-St") == 0) // StopTime
            {                 
                stopTime = std::stod(argv[i + 1]);
                i++;
            }
        }
        if (strcmp(argv[i], "-h") == 0) // Help
            {                 
                std::cout << "Displaying Help Message:" << std::endl;
                std::cout << "-Ts <double> : Time step in seconds" << std::endl;
                std::cout << "-----------------------------------" << std::endl;
                std::cout << "-St <double> : Total time in days" << std::endl;
                exit(0);
        }
    }
    std::cout << "##########################################################" << std::endl;
    std::cout << "##    Running Orbit Simulation using Parameters: " << "       ##" << std::endl;
    std::cout << "##    Time Step = " << timeStep/(24*60*60) << " days. Total Time = " << stopTime << " days."  << "       ##" << std::endl;
    std::cout << "##########################################################" << std::endl;

    InputManager::GetInstance()->ParsePlanetFile(infile);
    InputManager::GetInstance()->ParsePlanetFile(Mooninfile);
    InputManager::GetInstance()->ParsePlanetFile(Satinfile);
    RunManager *runMan = RunManager::GetInstance();
    runMan->SetTimeStep(timeStep);
    runMan->SetStopTime(stopTime);
    runMan->Init();
    runMan->Run();
    return 0;
}