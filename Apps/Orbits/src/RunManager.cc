#include "RunManager.hh"

#include "Earth.hh"
#include "Mars.hh"
#include "Moon.hh"

#include "namedBodies.hh"
#include "InputManager.hh"

#include "Vector3D.hh"
#include "PhysicsEqs.hh"

#include <iostream>
#include <string>
#include <cmath>


RunManager::RunManager(): fdt(0), fStopTime(0) {
}

RunManager *RunManager::fInstance = nullptr;

RunManager *RunManager::GetInstance() {
  if(!fInstance)
    fInstance = new RunManager();
  return fInstance;
};

void RunManager::Init() {

  fPlanetList = InputManager::GetInstance()->GetPlanetList();

  fMoonMap = InputManager::GetInstance()->GetMoonList();

  fSatMap = InputManager::GetInstance()->GetSatelliteList();
  fSatAtrMap = InputManager::GetInstance()->GetSatelliteAtributesList();

  namedBodies *conv = namedBodies::GetInstance();
  // Init Bodies and Satellites
  std::cout << "[RunManager] Simulation using Planets: " << std::endl;
  for(std::string plan : fPlanetList){
    std::cout << "[RunManager] " << plan << std::endl;
    Planets *b = conv->GetPlanetFunc(plan);
    fPlanets.push_back(b);
    std::map<std::string, std::string>::iterator iter = fMoonMap.find(plan);
    if (iter != fMoonMap.end() )
    {
      std::cout << "[RunManager] - " << iter->second << std::endl;
      Moons *m = conv->GetMoonsFunc(iter->second);
      m->SetBody(b);
      fMoons.push_back(m);
    }

    std::map<std::string, std::pair<std::string,std::string>>::iterator sat_iter = fSatMap.find(plan);
    if (sat_iter != fSatMap.end() )
    {
      std::cout << "[RunManager] - " << sat_iter->second.second << std::endl;
      std::map<std::string, std::vector<double>>::iterator atr_iter = fSatAtrMap.find(sat_iter->second.second);
      Satellite *s = conv->GetSatelliteFunc(sat_iter->second.first);
      if (atr_iter != fSatAtrMap.end() )
      {
        s->SetMass(atr_iter->second[0]);
        s->SetStartPosition(b->GetRadius(),b->GetPosition(),atr_iter->second[1]);
        s->SetStartVelocity(b->GetVelocity(),atr_iter->second[2]);
        s->SetName(sat_iter->second.second);
      }
      fSatellites.push_back(s);
    }
  }


  for(Planets *p : fPlanets){
    p->SetTimeStep(fdt);
  }

  for(Moons *m : fMoons){
    m->SetTimeStep(fdt);
  }

  for(Satellite *s : fSatellites){
    s->SetTimeStep(fdt);
  }


  fIOManager = RootIO::GetInstance();
  fIOManager->Init();
  fIOManager->InitBranches();

  fHelper = new OrbitHelper();

}

void RunManager::Run() {
  PhysicsEqs *PhyscisEq = PhysicsEqs::GetInstance();

  double t = 0;

  // Step the Simualtion by Dt
  for (int i=0; i<fStopTime; i++){
    for(Planets *p : fPlanets){
      p->NextStep();
    }

    for(Moons *m : fMoons){
      m->NextStep();
    }

    for(Satellite *s : fSatellites){
      s->NextStep();
    }

    t += fdt;

    int fDisplayPeriod = 100;
    if(i % fDisplayPeriod == 0) {
    std::pair<Double_t, Double_t> memoryUsage = fHelper->GetMemoryUsage();
    std::cout << "[" << fHelper->TimeString() << "] Running Day "
              << i
              << " [Memory usage -> Virtual: " << memoryUsage.first
              << " MB, Resident: " << memoryUsage.second << " MB]" << std::endl;
    }



    fIOManager->SaveStep();

  }
  
  fIOManager->EndRun();
  std::cout << "[RunManager] Simulation Complete :)" << std::endl;
}

