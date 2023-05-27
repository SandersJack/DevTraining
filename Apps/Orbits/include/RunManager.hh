#ifndef RunManager_H
#define RunManager_H 

#include "Vector3D.hh"

#include "Planets.hh"
#include "Moons.hh"
#include "Satellite.hh"
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

        std::vector<Planets *>  GetPlanetList() { return fPlanets;}
        std::vector<Moons *>  GetMoonList() { return fMoons;}
        std::vector<Satellite *>  GetSatelliteList() { return fSatellites;}

    private:
        static RunManager *fInstance;
        Moon *fMoon;

        double fdt;
        double fStopTime;

        std::vector<Planets *> fPlanets;
        std::vector<std::string> fPlanetList;

        std::vector<Moons *> fMoons;
        std::map<std::string, std::string> fMoonMap;

        std::vector<Satellite *> fSatellites;
        std::map<std::string, std::string> fSatMap;
        std::map<std::string, std::vector<double>> fSatAtrMap;
        

        RootIO *fIOManager; 
        OrbitHelper *fHelper;
};
#endif