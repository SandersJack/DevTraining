#include "EarthParameters.hh"
#include <iostream>

EarthParameters::EarthParameters(){
    Init();
}

EarthParameters::~EarthParameters(){
    
}

EarthParameters *EarthParameters::fInstance = nullptr;

EarthParameters *EarthParameters::GetInstance() {
    if(!fInstance)
        fInstance = new EarthParameters();
    return fInstance;
}

void EarthParameters::Init() {
    fAU = 1.495e11;
    fStartPos = new Vector3D(1.0167*fAU,0,0);
    fStartVel = new Vector3D(0,29290,0);
    fMass = 5.97219e24;
    fRadius = 6371e3; 
}