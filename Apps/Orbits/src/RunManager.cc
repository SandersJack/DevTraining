#include "RunManager.hh"
#include "Vector3D.hh"
#include "PhysicsEqs.hh"
#include <iostream>
#include <cmath>




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

  f_file = TFile::Open("Oribts.root", "recreate");
  t_main = new TTree("Data", "Orbit results");

  fposition = new Vector3D();

  t_main->Branch("position", fposition->IsA()->GetName(), &fposition);

}

void RunManager::Run() {

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

  for (int i=0; i<360; i++){

    Vector3D *Earth_a = PhyscisEq->GetAcceleration(earth_pos, sun, earth_mass, sun_mass, 0.1);

    earth_v->AddX(Earth_a->GetX()*dt);
    earth_v->AddY(Earth_a->GetY()*dt);
    earth_v->AddZ(Earth_a->GetZ()*dt);

    earth_pos->AddX(earth_v->GetX()*dt);
    earth_pos->AddY(earth_v->GetY()*dt);
    earth_pos->AddZ(earth_v->GetZ()*dt);

    t += dt;

    //Vector3D tmp = Vector3D(Earth_a);
    fposition->Set(earth_pos);
    if(t_main->Fill()) {  // Error in writing the output file (e.g. disk quota exceeded)
      std::cerr << "Error while writing the output file!" << std::endl;
    }

  }

  //
  
  if(t_main->Write() <= 0) {  // Error in writing the output file (e.g. disk quota exceeded)
    std::cerr << "Error while writing the output file!" << std::endl;
  }
  t_main->Print();
  f_file->Close();
  
}