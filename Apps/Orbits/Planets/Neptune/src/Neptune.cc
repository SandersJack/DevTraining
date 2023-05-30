#include "Neptune.hh"
#include "Vector3D.hh"
#include <iostream>

ClassImp(Neptune)

Neptune::Neptune() {
    Init();
}

Neptune::~Neptune(){

}

void Neptune::Init(){
    NeptuneParameters *EParam = NeptuneParameters::GetInstance();
    fMass = EParam->GetMass();
    fPosition = Vector3D(EParam->GetStartPos());
    fVelocity = Vector3D(EParam->GetStartVel());
    fRadius = EParam->GetRadius();
}

void Neptune::NextStep(){
    
    PhysicsEqs *PhysicsEqs = PhysicsEqs::GetInstance();

    Vector3D *sun = new Vector3D(0,0,0);
    double sun_mass = 1.989e30;
    
    Vector3D Neptune_a = PhysicsEqs->GetAcceleration(fPosition, sun, fMass, sun_mass, 0.1);

    fAcceleration = Neptune_a;

    fVelocity.AddX(Neptune_a.GetX()*fdt);
    fVelocity.AddY(Neptune_a.GetY()*fdt);
    fVelocity.AddZ(Neptune_a.GetZ()*fdt);

    fPosition.AddX(fVelocity.GetX()*fdt);
    fPosition.AddY(fVelocity.GetY()*fdt);
    fPosition.AddZ(fVelocity.GetZ()*fdt);

    fTime += fdt;
    
}

void Neptune::PrintPos(){
    //std::cout << fPosition->GetX() << " " << fPosition->GetY() << " " << fPosition->GetZ() << std::endl;
}