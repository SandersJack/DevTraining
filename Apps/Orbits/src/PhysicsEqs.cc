#include "PhysicsEqs.hh"
#include "RunManager.hh"
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

Vector3D PhysicsEqs::GetSatelliteAcceleration(Vector3D pos1, double mass1, double soft){

    std::vector<Planets*> fPlanets = RunManager::GetInstance()->GetPlanetList();
    Vector3D acc_1 = Vector3D();

    /// Calc for SUN

    double dx = (pos1.GetX() - 0);
    double dy = (pos1.GetY() - 0);
    double dz = (pos1.GetZ() - 0);

    double inv_r3 = pow((pow(dx,2) + pow(dy,2) + pow(dz,2) + pow(soft,2)),(-1.5));

    double sun_mass = 1.989e30;
    
    acc_1.AddX(-fG_const * (dx * inv_r3) * sun_mass);
    acc_1.AddY(-fG_const * (dy * inv_r3) * sun_mass);
    acc_1.AddZ(-fG_const * (dz * inv_r3) * sun_mass);


    // Calc for Planets
    for(Planets *p : fPlanets){
        
      double dx = (pos1.GetX() - p->GetPosition().GetX());
      double dy = (pos1.GetY() - p->GetPosition().GetY());
      double dz = (pos1.GetZ() - p->GetPosition().GetZ());

      double inv_r3 = pow((pow(dx,2) + pow(dy,2) + pow(dz,2) + pow(soft,2)),(-1.5));
      
      acc_1.AddX(-fG_const * (dx * inv_r3) * p->GetMass());
      acc_1.AddY(-fG_const * (dy * inv_r3) * p->GetMass());
      acc_1.AddZ(-fG_const * (dz * inv_r3) * p->GetMass());

    }

    return acc_1;
}