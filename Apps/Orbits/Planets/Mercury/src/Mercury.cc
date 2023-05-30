#include "Mercury.hh"
#include "Vector3D.hh"
#include <iostream>

ClassImp(Mercury)

Mercury::Mercury() {
    Init();
}

Mercury::~Mercury(){

}

void Mercury::Init(){
    MercuryParameters *EParam = MercuryParameters::GetInstance();
    fMass = EParam->GetMass();
    fPosition = Vector3D(EParam->GetStartPos());
    fVelocity = Vector3D(EParam->GetStartVel());
    fRadius = EParam->GetRadius();
}

void Mercury::NextStep(){
    
    PhysicsEqs *PhysicsEqs = PhysicsEqs::GetInstance();

    Vector3D *sun = new Vector3D(0,0,0);
    double sun_mass = 1.989e30;
    
    Vector3D Mercury_a = PhysicsEqs->GetAcceleration(fPosition, sun, fMass, sun_mass, 0.1);

    fAcceleration = Mercury_a;

    fVelocity.AddX(Mercury_a.GetX()*fdt);
    fVelocity.AddY(Mercury_a.GetY()*fdt);
    fVelocity.AddZ(Mercury_a.GetZ()*fdt);

    fPosition.AddX(fVelocity.GetX()*fdt);
    fPosition.AddY(fVelocity.GetY()*fdt);
    fPosition.AddZ(fVelocity.GetZ()*fdt);

    fTime += fdt;
    
}

void Mercury::PrintPos(){
    //std::cout << fPosition->GetX() << " " << fPosition->GetY() << " " << fPosition->GetZ() << std::endl;
}