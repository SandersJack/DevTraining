#include "MarsParameters.hh"
#include <iostream>

MarsParameters::MarsParameters(){
    Init();
}

MarsParameters::~MarsParameters(){
    
}

MarsParameters *MarsParameters::fInstance = nullptr;

MarsParameters *MarsParameters::GetInstance() {
    if(!fInstance)
        fInstance = new MarsParameters();
    return fInstance;
}

void MarsParameters::Init() {
    fAU = 1.5e11;
    fStartPos = new Vector3D(1.6662*fAU,0,0);
    fStartVel = new Vector3D(0,21970,0);
    fMass = 6.39e23;
}