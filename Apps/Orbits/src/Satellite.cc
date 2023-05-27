#include "Satellite.hh"
#include "PhysicsEqs.hh"

ClassImp(Satellite)

Satellite::Satellite():fMass(0), fdt(0) , fTime(0){

}

Satellite::~Satellite(){}

void Satellite::SetStartPosition(Vector3D body_val,double sat_val){

    fPosition = Vector3D(body_val);
    fPosition.AddX(sat_val*1e3+6000e3);

}

void Satellite::SetStartVelocity(Vector3D body_val,double sat_val){

    fVelocity = Vector3D(body_val);
    fVelocity.AddY(sat_val);

}


void Satellite::NextStep() {

    PhysicsEqs *PhysicsEqs = PhysicsEqs::GetInstance();

    //fVelocity.Print();
    
    Vector3D Sat_a = PhysicsEqs->GetSatelliteAcceleration(fPosition, fMass, 0.1);

    fAcceleration = Sat_a;
    //fAcceleration.Print();

    fVelocity.AddX(Sat_a.GetX()*fdt);
    fVelocity.AddY(Sat_a.GetY()*fdt);
    fVelocity.AddZ(Sat_a.GetZ()*fdt);

    //fVelocity.Print();

    fPosition.AddX(fVelocity.GetX()*fdt);
    fPosition.AddY(fVelocity.GetY()*fdt);
    fPosition.AddZ(fVelocity.GetZ()*fdt);

    fTime += fdt;

}