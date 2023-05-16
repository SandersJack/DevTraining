#include "RunManager.hh"

#include "Earth.hh"

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

  fdt = 86400; //seconds

  fPlanets.push_back(new Earth());

  f_file = TFile::Open("Oribts.root", "recreate");
  t_main = new TTree("Data", "Orbit results");

  for(Planets *p : fPlanets){
    t_main->Branch("Earth", p->IsA()->GetName(), static_cast<Earth*>(p));
    p->SetTimeStep(fdt);
  }

  //fEarth = new Vector3D();

  //t_main->Branch("Earth", fEarth->IsA()->GetName(), &fEarth);

  fMars = new Vector3D();

  t_main->Branch("Mars", fMars->IsA()->GetName(), &fMars);

}

void RunManager::Run() {

  Vector3D *sun = new Vector3D(0,0,0);
  double sun_mass = 1.989e30;
  double AU = 1.5e11;
  Vector3D *earth_pos = new Vector3D(1.0167*AU,0,0);
  double earth_mass = 5.97219e24;
  Vector3D *earth_v = new Vector3D(0,29290,0);

  Vector3D *mars_pos = new Vector3D(1.6662*AU,0,0);
  double mars_mass = 6.39e23;
  Vector3D *mars_v = new Vector3D(0,21970,0);

  PhysicsEqs *PhyscisEq = PhysicsEqs::GetInstance();

   

  double t = 0;



  for (int i=0; i<1000; i++){
    /*
    Vector3D *Earth_a = PhyscisEq->GetAcceleration(earth_pos, sun, earth_mass, sun_mass, 0.1);

    earth_v->AddX(Earth_a->GetX()*dt);
    earth_v->AddY(Earth_a->GetY()*dt);
    earth_v->AddZ(Earth_a->GetZ()*dt);

    earth_pos->AddX(earth_v->GetX()*dt);
    earth_pos->AddY(earth_v->GetY()*dt);
    earth_pos->AddZ(earth_v->GetZ()*dt);
    */
   
    for(Planets *p : fPlanets){
      p->NextStep();
    }

    Vector3D *Mars_a = PhyscisEq->GetAcceleration(mars_pos, sun, mars_mass, sun_mass, 0.1);

    mars_v->AddX(Mars_a->GetX()*fdt);
    mars_v->AddY(Mars_a->GetY()*fdt);
    mars_v->AddZ(Mars_a->GetZ()*fdt);

    mars_pos->AddX(mars_v->GetX()*fdt);
    mars_pos->AddY(mars_v->GetY()*fdt);
    mars_pos->AddZ(mars_v->GetZ()*fdt);

    t += fdt;

    //Vector3D tmp = Vector3D(Earth_a);
    //fEarth->Set(earth_pos);
    fMars->Set(mars_pos);

    if(t_main->Fill()) {  // Error in writing the output file (e.g. disk quota exceeded)
      //std::cerr << "Error while writing the output file!" << std::endl;
    }

  }

  //
  
  if(t_main->Write() <= 0) {  // Error in writing the output file (e.g. disk quota exceeded)
    //std::cerr << "Error while writing the output file!" << std::endl;
  }
  t_main->Print();
  f_file->Close();
  
}