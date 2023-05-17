#include "Moon.hh"
#include "Earth.hh"
#include "Vector3D.hh"
#include <iostream>

ClassImp(Moon)

Moon::Moon() {
    Init();
}

Moon::~Moon(){

}

void Moon::Init(){
    MoonParameters *EParam = MoonParameters::GetInstance();
    fMass = EParam->GetMass();
    fPosition = Vector3D(EParam->GetStartPos());
    fVelocity = Vector3D(EParam->GetStartVel());
}

void Moon::NextStep(Earth *E){
    
    PhysicsEqs *PhysicsEqs = PhysicsEqs::GetInstance();

    Vector3D *cen = new Vector3D(0,0,0);
    double sun_mass = 1.989e30;
    
    //std::cout << E->GetMass() << std::endl;
    Vector3D Moon_a = PhysicsEqs->GetAcceleration(fPosition, cen, fMass, sun_mass, 0.1);
    Vector3D Moon_Earth = PhysicsEqs->GetAcceleration(fPosition, cen, fMass, E->GetMass(), 0.1);

    fAcceleration = Moon_Earth;

    //fAcceleration.AddX(Moon_a.GetX());
    //fAcceleration.AddY(Moon_a.GetY());
    //fAcceleration.AddZ(Moon_a.GetZ());

    fVelocity.AddX(fAcceleration.GetX()*fdt);
    fVelocity.AddY(fAcceleration.GetY()*fdt);
    fVelocity.AddZ(fAcceleration.GetZ()*fdt);

    fPosition.AddX(fVelocity.GetX()*fdt);
    fPosition.AddY(fVelocity.GetY()*fdt);
    fPosition.AddZ(fVelocity.GetZ()*fdt);

    fSunPosition.SetX(fPosition.GetX() + E->GetPosition().GetX());
    fSunPosition.SetY(fPosition.GetY() + E->GetPosition().GetY());
    fSunPosition.SetZ(fPosition.GetZ() + E->GetPosition().GetZ());
    
}

void Moon::PrintPos(){
    //std::cout << fPosition->GetX() << " " << fPosition->GetY() << " " << fPosition->GetZ() << std::endl;
}