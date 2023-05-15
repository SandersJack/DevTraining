#include "Earth.hh"

ClassImp(Earth)

Earth::Earth() {
    fEParam = EarthParameters::GetInstance();
    fPhysicsEqs = PhysicsEqs::GetInstance();
    Init();
}

Earth::~Earth(){}

void Earth::Init(){
    fMass = fEParam->GetMass();
    fPosition = fEParam->GetStartPos();
    fVelocity = fEParam->GetStartVel();
}

void Earth::NextStep(){

    Vector3D *sun = new Vector3D(0,0,0);
    double sun_mass = 1.989e30;

    Vector3D *Earth_a = fPhysicsEqs->GetAcceleration(fPosition, sun, fMass, sun_mass, 0.1);

    fVelocity->AddX(Earth_a->GetX()*fdt);
    fVelocity->AddY(Earth_a->GetY()*fdt);
    fVelocity->AddZ(Earth_a->GetZ()*fdt);

    fPosition->AddX(fVelocity->GetX()*fdt);
    fPosition->AddY(fVelocity->GetY()*fdt);
    fPosition->AddZ(fVelocity->GetZ()*fdt);

}