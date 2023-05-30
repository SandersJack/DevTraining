#include "MarsParameters.hh"
#include <iostream>
#include <cmath>

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
    fAU = 1.495e11;
    double r = 1.38227;
    double v = 26.50e3;
    double angle = 53.1 * M_PI/180;
    fStartPos = new Vector3D(r*fAU*cos(angle),r*fAU*sin(angle),0);
    fStartVel = new Vector3D(-v*sin(angle),v*cos(angle),0);
    fMass = 6.39e23;
    fRadius = 3389.5e3;
}