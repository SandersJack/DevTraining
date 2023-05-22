#include "Earth.hh"
#include "Vector3D.hh"
#include <iostream>

ClassImp(Earth)

Earth::Earth() {
    Init();
}

Earth::~Earth(){

}

void Earth::Init(){
    EarthParameters *EParam = EarthParameters::GetInstance();
    fMass = EParam->GetMass();
    fPosition = Vector3D(EParam->GetStartPos());
    fVelocity = Vector3D(EParam->GetStartVel());
}

void Earth::NextStep(){
    
    PhysicsEqs *PhysicsEqs = PhysicsEqs::GetInstance();

    Vector3D *sun = new Vector3D(0,0,0);
    double sun_mass = 1.989e30;
    
    Vector3D Earth_a = PhysicsEqs->GetAcceleration(fPosition, sun, fMass, sun_mass, 0.1);

    fAcceleration = Earth_a;

    fVelocity.AddX(Earth_a.GetX()*fdt);
    fVelocity.AddY(Earth_a.GetY()*fdt);
    fVelocity.AddZ(Earth_a.GetZ()*fdt);

    fPosition.AddX(fVelocity.GetX()*fdt);
    fPosition.AddY(fVelocity.GetY()*fdt);
    fPosition.AddZ(fVelocity.GetZ()*fdt);

    fTime += fdt;
    
}

void Earth::PrintPos(){
    //std::cout << fPosition->GetX() << " " << fPosition->GetY() << " " << fPosition->GetZ() << std::endl;
}