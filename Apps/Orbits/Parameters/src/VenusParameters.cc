#include "VenusParameters.hh"
#include <iostream>
#include <cmath>

VenusParameters::VenusParameters(){
    Init();
}

VenusParameters::~VenusParameters(){
    
}

VenusParameters *VenusParameters::fInstance = nullptr;

VenusParameters *VenusParameters::GetInstance() {
    if(!fInstance)
        fInstance = new VenusParameters();
    return fInstance;
}

void VenusParameters::Init() {
    fAU = 1.495e11;
    double r = 0.718459423901;
    double v = 35.26e3;
    double angle = -151.41 * M_PI/180;
    fStartPos = new Vector3D(r*fAU*cos(angle),r*fAU*sin(angle),0);
    fStartVel = new Vector3D(-v*sin(angle),v*cos(angle),0);
    fMass = 4.8673e24;
    fRadius = 6051.8e3;
}