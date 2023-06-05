#include "Jupiter.hh"
#include "Vector3D.hh"
#include <iostream>

ClassImp(Jupiter)

Jupiter::Jupiter() {
    Init();
}

Jupiter::~Jupiter(){

}

void Jupiter::Init(){
    JupiterParameters *EParam = JupiterParameters::GetInstance();
    fMass = EParam->GetMass();
    fPosition = Vector3D(EParam->GetStartPos());
    fVelocity = Vector3D(EParam->GetStartVel());
    fRadius = EParam->GetRadius();
}

void Jupiter::NextStep(){
    
    PhysicsEqs *PhysicsEqs = PhysicsEqs::GetInstance();

    Vector3D *sun = new Vector3D(0,0,0);
    double sun_mass = 1.989e30;
    
    Vector3D Jupiter_a = PhysicsEqs->GetAcceleration(fPosition, sun, fMass, sun_mass, 0.1);

    fAcceleration = Jupiter_a;

    fVelocity.AddX(Jupiter_a.GetX()*fdt);
    fVelocity.AddY(Jupiter_a.GetY()*fdt);
    fVelocity.AddZ(Jupiter_a.GetZ()*fdt);

    fPosition.AddX(fVelocity.GetX()*fdt);
    fPosition.AddY(fVelocity.GetY()*fdt);
    fPosition.AddZ(fVelocity.GetZ()*fdt);

    fTime += fdt;
    
}

void Jupiter::PrintPos(){
    //std::cout << fPosition->GetX() << " " << fPosition->GetY() << " " << fPosition->GetZ() << std::endl;
}