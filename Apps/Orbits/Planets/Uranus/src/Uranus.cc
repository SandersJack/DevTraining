#include "Uranus.hh"
#include "Vector3D.hh"
#include <iostream>

ClassImp(Uranus)

Uranus::Uranus() {
    Init();
}

Uranus::~Uranus(){

}

void Uranus::Init(){
    UranusParameters *EParam = UranusParameters::GetInstance();
    fMass = EParam->GetMass();
    fPosition = Vector3D(EParam->GetStartPos());
    fVelocity = Vector3D(EParam->GetStartVel());
    fRadius = EParam->GetRadius();
}

void Uranus::NextStep(){
    
    PhysicsEqs *PhysicsEqs = PhysicsEqs::GetInstance();

    Vector3D *sun = new Vector3D(0,0,0);
    double sun_mass = 1.989e30;
    
    Vector3D Uranus_a = PhysicsEqs->GetAcceleration(fPosition, sun, fMass, sun_mass, 0.1);

    fAcceleration = Uranus_a;

    fVelocity.AddX(Uranus_a.GetX()*fdt);
    fVelocity.AddY(Uranus_a.GetY()*fdt);
    fVelocity.AddZ(Uranus_a.GetZ()*fdt);

    fPosition.AddX(fVelocity.GetX()*fdt);
    fPosition.AddY(fVelocity.GetY()*fdt);
    fPosition.AddZ(fVelocity.GetZ()*fdt);

    fTime += fdt;
    
}

void Uranus::PrintPos(){
    //std::cout << fPosition->GetX() << " " << fPosition->GetY() << " " << fPosition->GetZ() << std::endl;
}