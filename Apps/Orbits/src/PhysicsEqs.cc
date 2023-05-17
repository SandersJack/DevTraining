#include "PhysicsEqs.hh"
#include <cmath>
#include <iostream>

PhysicsEqs::PhysicsEqs(): fG_const(0){
    fG_const = 6.67430e-11;
}

PhysicsEqs::~PhysicsEqs(){
}

PhysicsEqs *PhysicsEqs::fInstance = nullptr;

PhysicsEqs *PhysicsEqs::GetInstance() {
  if(!fInstance)
    fInstance = new PhysicsEqs();
  return fInstance;
};


Vector3D PhysicsEqs::GetAcceleration(Vector3D pos1, Vector3D pos2, double mass1, double mass2, double soft){

    double dx = (pos1.GetX() - pos2.GetX());
    double dy = (pos1.GetY() - pos2.GetY());
    double dz = (pos1.GetZ() - pos2.GetZ());

    double inv_r3 = pow((pow(dx,2) + pow(dy,2) + pow(dz,2) + pow(soft,2)),(-1.5));

    Vector3D acc_1 = Vector3D();
    acc_1.SetX(-fG_const * (dx * inv_r3) * mass2);
    acc_1.SetY(-fG_const * (dy * inv_r3) * mass2);
    acc_1.SetZ(-fG_const * (dz * inv_r3) * mass2);

    return acc_1;
}