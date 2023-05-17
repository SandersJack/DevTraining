#include "RunManager.hh"

#include "Earth.hh"
#include "Mars.hh"

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

  //fPlanets.push_back(new Earth());

  fEarth = new Earth();
  fEarth->SetTimeStep(fdt);

  fMars = new Mars();
  fMars->SetTimeStep(fdt);

 

  f_file = TFile::Open("Oribts.root", "recreate");
  t_main = new TTree("Data", "Orbit results");

  t_main->Branch("Earth", fEarth->IsA()->GetName(), &fEarth);
  t_main->Branch("Mars", fMars->IsA()->GetName(), &fMars);

  //for(Planets *p : fPlanets){
  //  t_main->Branch("Earth", p->IsA()->GetName(), static_cast<Earth*>(p));
  //  p->SetTimeStep(fdt);
  //}

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
    //for(Planets *p : fPlanets){
    //  p->NextStep();
    //}
    fEarth->NextStep();
    fEarth->PrintPos();

    fMars->NextStep();
    fMars->PrintPos();

    t += fdt;


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