#include "Mars.hh"
#include "Vector3D.hh"
#include <iostream>

ClassImp(Mars)

Mars::Mars() {
    Init();
}

Mars::~Mars(){

}

void Mars::Init(){
    MarsParameters *EParam = MarsParameters::GetInstance();
    fMass = EParam->GetMass();
    fPosition = Vector3D(EParam->GetStartPos());
    fVelocity = Vector3D(EParam->GetStartVel());
}

void Mars::NextStep(){
    
    PhysicsEqs *PhysicsEqs = PhysicsEqs::GetInstance();

    Vector3D *sun = new Vector3D(0,0,0);
    double sun_mass = 1.989e30;
    
    Vector3D Mars_a = PhysicsEqs->GetAcceleration(fPosition, sun, fMass, sun_mass, 0.1);

    fAcceleration = Mars_a;

    fVelocity.AddX(Mars_a.GetX()*fdt);
    fVelocity.AddY(Mars_a.GetY()*fdt);
    fVelocity.AddZ(Mars_a.GetZ()*fdt);

    fPosition.AddX(fVelocity.GetX()*fdt);
    fPosition.AddY(fVelocity.GetY()*fdt);
    fPosition.AddZ(fVelocity.GetZ()*fdt);

    fTime += fdt;
    
}

void Mars::PrintPos(){
    //std::cout << fPosition->GetX() << " " << fPosition->GetY() << " " << fPosition->GetZ() << std::endl;
}