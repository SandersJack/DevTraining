#include "MoonParameters.hh"
#include <iostream>

MoonParameters::MoonParameters(){
    Init();
}

MoonParameters::~MoonParameters(){
    
}

MoonParameters *MoonParameters::fInstance = nullptr;

MoonParameters *MoonParameters::GetInstance() {
    if(!fInstance)
        fInstance = new MoonParameters();
    return fInstance;
}

void MoonParameters::Init() {
    fAU = 1.5e11;
    //fStartPos = new Vector3D(1.0167*fAU+0.405400e9,0,0);
    //fStartVel = new Vector3D(0,29290+970,0);
    fStartPos = new Vector3D(0.405400e9,0,0);
    fStartVel = new Vector3D(0,970,0);
    fMass = 0.07346e24;
}