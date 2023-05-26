#include "RunManager.hh"

#include "Earth.hh"
#include "Mars.hh"
#include "Moon.hh"

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

  //

  fEarth = new Earth();
  fEarth->SetTimeStep(fdt);
  fPlanets.push_back(fEarth);

  fMars = new Mars();
  fMars->SetTimeStep(fdt);
  fPlanets.push_back(fMars);

  fMoon = new Moon();
  fMoon->SetTimeStep(fdt);

 

  f_file = TFile::Open("Oribts.root", "recreate");
  t_main = new TTree("Data", "Orbit results");

  t_main->Branch("Moon", fMoon->IsA()->GetName(), &fMoon);

  for(Planets *p : fPlanets){
    std::cout << p->IsA()->GetName() << std::endl;
    t_main->Branch(p->IsA()->GetName(), "Planets", p);
  }
}

void RunManager::Run() {
  PhysicsEqs *PhyscisEq = PhysicsEqs::GetInstance();

   

  double t = 0;



  for (int i=0; i<1000; i++){
    for(Planets *p : fPlanets){
      p->NextStep();
    }
    fMoon->NextStep(fEarth);
    fMoon->PrintPos();

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