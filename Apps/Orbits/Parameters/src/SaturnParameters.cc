#include "SaturnParameters.hh"
#include <iostream>
#include <cmath>

SaturnParameters::SaturnParameters(){
    Init();
}

SaturnParameters::~SaturnParameters(){
    
}

SaturnParameters *SaturnParameters::fInstance = nullptr;

SaturnParameters *SaturnParameters::GetInstance() {
    if(!fInstance)
        fInstance = new SaturnParameters();
    return fInstance;
}

void SaturnParameters::Init() {
    fAU = 1.495e11;
    double r = 9.074687986184;
    double v = 10.14e3;
    double angle = -190.51 * M_PI/180;
    fStartPos = new Vector3D(r*fAU*cos(angle),r*fAU*sin(angle),0);
    fStartVel = new Vector3D(-v*sin(angle),v*cos(angle),0);
    fMass = 568.32e24;
    fRadius = 60268e3;
}