#ifndef RunManager_H
#define RunManager_H 

#include "Vector3D.hh"

#include "Planets.hh"
#include "Earth.hh"

#include <iostream>
#include <vector>

#include "TROOT.h"
#include "TTree.h"
#include "TFile.h"


class RunManager {

    public:
        RunManager();
        static RunManager *GetInstance();
        void Test() {std::cout << "HERE"<<std::endl;}

        void Init();
        void Run();

    private:
        static RunManager *fInstance;
        TFile *f_file;
        TTree *t_main;

        TBranch *fEarthBranch;
        Earth *fEarth;
        Vector3D *fMars;

        double fdt;

        std::vector<Planets *> fPlanets;
};
#endif