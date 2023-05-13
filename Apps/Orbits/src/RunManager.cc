#include "RunManager.hh"
#include "Vector3D.hh"
#include "PhysicsEqs.hh"
#include <iostream>

RunManager::RunManager() {
    std::cout << "RunManager" << std::endl;
}

RunManager *RunManager::fInstance = nullptr;

RunManager *RunManager::GetInstance() {
  if(!fInstance)
    fInstance = new RunManager();
  return fInstance;
};

void RunManager::Init() {

}

void RunManager::Run() {

  Vector3D *sun = new Vector3D(0,0,0);
  double sun_mass = 1.989e30;

  Vector3D *earth = new Vector3D(149.6e9,0,0);
  double earth_mass = 1.989e30;

  PhysicsEqs *PhyscisEq = PhysicsEqs::GetInstance();

  Vector3D *Earth_a = PhyscisEq->GetAcceleration(earth, sun, earth_mass, sun_mass, 0.1);

  Earth_a->Print();

  //std::cout << test->GetX() << " " << test->GetY() << " " << test->GetZ() << std::endl;
}