#include "RootIO.hh"

#include "Planets.hh"
#include "RunManager.hh"

RootIO::RootIO(): fOutFilename("proton.root") {

}

RootIO *RootIO::fInstance = nullptr;

RootIO *RootIO::GetInstance() {
  if(!fInstance)
    fInstance = new RootIO();
  return fInstance;
};

void RootIO::Init(){

    f_file = TFile::Open(fOutFilename, "recreate");
    t_main = new TTree("Data", "Orbit results");

}

void RootIO::InitBranches() {
    std::vector<Planets*> fPlanets = RunManager::GetInstance()->GetPlanetList();

    std::vector<Moons*> fMoons = RunManager::GetInstance()->GetMoonList();

    for(Planets *p : fPlanets){
        t_main->Branch(p->IsA()->GetName(), "Planets", p);
        std::cout << "[RootIO] "<< p->IsA()->GetName() << "IO Initialised"<< std::endl;
    }

    for(Moons *m : fMoons){
        t_main->Branch(m->IsA()->GetName(), "Moons", m);
        std::cout << "[RootIO] "<< m->IsA()->GetName() << "IO Initialised"<< std::endl;
    }
}

void RootIO::SaveStep() {
    if(t_main->Fill()) {  // Error in writing the output file (e.g. disk quota exceeded)
      //std::cerr << "Error while writing the output file!" << std::endl;
    }
}

void RootIO::EndRun() {
    if(t_main->Write() <= 0) {  // Error in writing the output file (e.g. disk quota exceeded)
    //std::cerr << "Error while writing the output file!" << std::endl;
    }
    f_file->Close();
}