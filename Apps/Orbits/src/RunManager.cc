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

  /*2460077.500000000 = A.D. 2023-May-13 00:00:00.0000 TDB 
 X =-9.502733785242791E+07 Y =-1.187272762699778E+08 Z = 3.915031966490299E+04
 VX= 2.288459517324164E+01 VY=-1.860895478429658E+01 VZ= 4.221814236808896E-04
 LT= 5.072627390815210E+02 RG= 1.520735434010618E+08 RR= 2.283656603172539E-01*/

  Vector3D *sun = new Vector3D(0,0,0);
  double sun_mass = 1.989e30;
  double AU = 1.5e11;
  Vector3D *earth_pos = new Vector3D(1.0167*AU,0,0);
  double earth_mass = 5.97219e24;
  Vector3D *earth_v = new Vector3D(0,29290,0);

  PhysicsEqs *PhyscisEq = PhysicsEqs::GetInstance();

  double dt = 86400; //seconds 

  double t = 0;

  Vector3D *Earth_a = PhyscisEq->GetAcceleration(earth_pos, sun, earth_mass, sun_mass, 0.1);
  Earth_a->Print();
  earth_v->Print();
  earth_pos->Print();

  for (int i=0; i<380; i++){
    std::cout << "==================" <<std::endl;
    std::cout << t << " "  << i <<std::endl;

    Vector3D *Earth_a = PhyscisEq->GetAcceleration(earth_pos, sun, earth_mass, sun_mass, 0.1);

    earth_v->AddX(Earth_a->GetX()*dt);
    earth_v->AddY(Earth_a->GetY()*dt);
    earth_v->AddZ(Earth_a->GetZ()*dt);

    earth_pos->AddX(earth_v->GetX()*dt);
    earth_pos->AddY(earth_v->GetY()*dt);
    earth_pos->AddZ(earth_v->GetZ()*dt);

    t += dt;
    
    Earth_a->Print();
    earth_v->Print();
    earth_pos->Print();
  }
  

  //std::cout << test->GetX() << " " << test->GetY() << " " << test->GetZ() << std::endl;
}