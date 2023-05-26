#include "RunManager.hh"

#include "Earth.hh"
#include "Mars.hh"
#include "Moon.hh"

#include "namedPlanets.hh"
#include "InputManager.hh"

#include "Vector3D.hh"
#include "PhysicsEqs.hh"

#include <iostream>
#include <string>
#include <cmath>


RunManager::RunManager() {
}

RunManager *RunManager::fInstance = nullptr;

RunManager *RunManager::GetInstance() {
  if(!fInstance)
    fInstance = new RunManager();
  return fInstance;
};

void RunManager::Init() {

  fPlanetList = InputManager::GetInstance()->GetPlanetList();

  fdt = 86400; //seconds

  namedPlanets *conv = namedPlanets::GetInstance();

  std::cout << "[RunManager] Simulation using Planets: " << std::endl;
  for(std::string plan : fPlanetList){
    std::cout << "[RunManager] " << plan << std::endl;
    fPlanets.push_back(conv->GetPlanetFunc(plan));
  }

  //fMoon = new Moon();
  //fMoon->SetTimeStep(fdt);

  //t_main->Branch("Moon", fMoon->IsA()->GetName(), &fMoon);

  for(Planets *p : fPlanets){
    p->SetTimeStep(fdt);
  }

  fIOManager = RootIO::GetInstance();
  fIOManager->Init();
  fIOManager->InitBranches();

}

void RunManager::Run() {
  PhysicsEqs *PhyscisEq = PhysicsEqs::GetInstance();

  double t = 0;


  for (int i=0; i<1000; i++){
    for(Planets *p : fPlanets){
      p->NextStep();
    }
    //fMoon->NextStep(fEarth);
    //fMoon->PrintPos();

    t += fdt;


    fIOManager->SaveStep();

  }
  
  fIOManager->EndRun();

}