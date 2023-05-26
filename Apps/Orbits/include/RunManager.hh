#ifndef RunManager_H
#define RunManager_H 

#include "Vector3D.hh"

#include "Planets.hh"
#include "Earth.hh"
#include "Mars.hh"
#include "Moon.hh"

#include "RootIO.hh"

#include <iostream>
#include <vector>




class RunManager {

    public:
        RunManager();
        static RunManager *GetInstance();
        void Test() {std::cout << "HERE"<<std::endl;}

        void Init();
        void Run();

        std::vector<Planets *>  GetPlanetMap() { return fPlanets;}

    private:
        static RunManager *fInstance;

        TBranch *fEarthBranch;
        Earth *fEarth;
        Mars *fMars;
        Moon *fMoon;

        double fdt;

        std::vector<Planets *> fPlanets;

        RootIO *fIOManager; 
};
#endif