#include "JupiterParameters.hh"
#include <iostream>
#include <cmath>

JupiterParameters::JupiterParameters(){
    Init();
}

JupiterParameters::~JupiterParameters(){
    
}

JupiterParameters *JupiterParameters::fInstance = nullptr;

JupiterParameters *JupiterParameters::GetInstance() {
    if(!fInstance)
        fInstance = new JupiterParameters();
    return fInstance;
}

void JupiterParameters::Init() {
    fAU = 1.495e11;
    double r = 4.95057179982;
    double v = 13.72e3;
    double angle = -268.187 * M_PI/180;
    fStartPos = new Vector3D(r*fAU*cos(angle),r*fAU*sin(angle),0);
    fStartVel = new Vector3D(-v*sin(angle),v*cos(angle),0);
    fMass = 1898.13e24;
    fRadius = 71492e3;
}