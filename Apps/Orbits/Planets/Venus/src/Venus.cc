#include "Venus.hh"
#include "Vector3D.hh"
#include <iostream>

ClassImp(Venus)

Venus::Venus() {
    Init();
}

Venus::~Venus(){

}

void Venus::Init(){
    VenusParameters *EParam = VenusParameters::GetInstance();
    fMass = EParam->GetMass();
    fPosition = Vector3D(EParam->GetStartPos());
    fVelocity = Vector3D(EParam->GetStartVel());
    fRadius = EParam->GetRadius();
}

void Venus::NextStep(){
    
    PhysicsEqs *PhysicsEqs = PhysicsEqs::GetInstance();

    Vector3D *sun = new Vector3D(0,0,0);
    double sun_mass = 1.989e30;
    
    Vector3D Venus_a = PhysicsEqs->GetAcceleration(fPosition, sun, fMass, sun_mass, 0.1);

    fAcceleration = Venus_a;

    fVelocity.AddX(Venus_a.GetX()*fdt);
    fVelocity.AddY(Venus_a.GetY()*fdt);
    fVelocity.AddZ(Venus_a.GetZ()*fdt);

    fPosition.AddX(fVelocity.GetX()*fdt);
    fPosition.AddY(fVelocity.GetY()*fdt);
    fPosition.AddZ(fVelocity.GetZ()*fdt);

    fTime += fdt;
    
}

void Venus::PrintPos(){
    //std::cout << fPosition->GetX() << " " << fPosition->GetY() << " " << fPosition->GetZ() << std::endl;
}