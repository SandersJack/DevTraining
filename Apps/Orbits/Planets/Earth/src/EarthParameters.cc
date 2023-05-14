#include "EarthParameters.hh"
#include <iostream>


EarthParameters::EarthParameters(){
    std::cout << "EARTH TESTING" << std::endl;
}

EarthParameters::~EarthParameters(){
    
}

EarthParameters *EarthParameters::fInstance = nullptr;

EarthParameters *EarthParameters::GetInstance() {
    if(!fInstance)
        fInstance = new EarthParameters();
    return fInstance;
}