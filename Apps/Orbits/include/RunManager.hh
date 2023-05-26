#ifndef RunManager_H
#define RunManager_H 

#include "Vector3D.hh"

#include "Planets.hh"
#include "Earth.hh"
#include "Mars.hh"
#include "Moon.hh"

#include "RootIO.hh"
#include "OrbitHelper.hh"

#include <iostream>
#include <vector>




class RunManager {

    public:
        RunManager();
        static RunManager *GetInstance();
        void Test() {std::cout << "HERE"<<std::endl;}

        void Init();
        void Run();

        void SetTimeStep(double val) {fdt = val;}
        void SetStopTime(double val) {fStopTime = val;}

        std::vector<Planets *>  GetPlanetMap() { return fPlanets;}

    private:
        static RunManager *fInstance;
        Moon *fMoon;

        double fdt;
        double fStopTime;

        std::vector<Planets *> fPlanets;
        std::vector<std::string> fPlanetList;

        RootIO *fIOManager; 
        OrbitHelper *fHelper;
};
#endif