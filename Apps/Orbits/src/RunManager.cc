#include "RunManager.hh"
#include "Vector3D.hh"
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
  Vector3D *test = new Vector3D(10,15,19);

  std::cout << test->GetX() << " " << test->GetY() << " " << test->GetZ() << std::endl;
}