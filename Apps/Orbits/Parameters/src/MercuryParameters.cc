#include "MercuryParameters.hh"
#include <iostream>
#include <cmath>

MercuryParameters::MercuryParameters(){
    Init();
}

MercuryParameters::~MercuryParameters(){
    
}

MercuryParameters *MercuryParameters::fInstance = nullptr;

MercuryParameters *MercuryParameters::GetInstance() {
    if(!fInstance)
        fInstance = new MercuryParameters();
    return fInstance;
}

void MercuryParameters::Init() {
    fAU = 1.495e11;
    double r = 0.30749100762;
    double v = 58.97e3;
    double angle = -205.48 * M_PI/180;
    fStartPos = new Vector3D(r*fAU*cos(angle),r*fAU*sin(angle),0);
    fStartVel = new Vector3D(-v*sin(angle),v*cos(angle),0);
    fMass = 0.33010e24;
    fRadius = 2440.5e3;
}