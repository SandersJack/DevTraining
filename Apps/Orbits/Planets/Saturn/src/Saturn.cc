#include "Saturn.hh"
#include "Vector3D.hh"
#include <iostream>

ClassImp(Saturn)

Saturn::Saturn() {
    Init();
}

Saturn::~Saturn(){

}

void Saturn::Init(){
    SaturnParameters *EParam = SaturnParameters::GetInstance();
    fMass = EParam->GetMass();
    fPosition = Vector3D(EParam->GetStartPos());
    fVelocity = Vector3D(EParam->GetStartVel());
    fRadius = EParam->GetRadius();
}

void Saturn::NextStep(){
    
    PhysicsEqs *PhysicsEqs = PhysicsEqs::GetInstance();

    Vector3D *sun = new Vector3D(0,0,0);
    double sun_mass = 1.989e30;
    
    Vector3D Saturn_a = PhysicsEqs->GetAcceleration(fPosition, sun, fMass, sun_mass, 0.1);

    fAcceleration = Saturn_a;

    fVelocity.AddX(Saturn_a.GetX()*fdt);
    fVelocity.AddY(Saturn_a.GetY()*fdt);
    fVelocity.AddZ(Saturn_a.GetZ()*fdt);

    fPosition.AddX(fVelocity.GetX()*fdt);
    fPosition.AddY(fVelocity.GetY()*fdt);
    fPosition.AddZ(fVelocity.GetZ()*fdt);

    fTime += fdt;
    
}

void Saturn::PrintPos(){
    //std::cout << fPosition->GetX() << " " << fPosition->GetY() << " " << fPosition->GetZ() << std::endl;
}