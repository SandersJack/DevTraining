#ifndef RootIO_H
#define RootIO_H 1 

#include <iostream>
#include <string>

#include "TROOT.h"
#include "TTree.h"
#include "TFile.h"

class RootIO {
    
    public:
        RootIO();

        static RootIO *GetInstance();

        void Init();
        void InitBranches();
        void SaveStep();
        void EndRun();

        void SetFilename(const char *val) {fOutFilename = val;}

    private:
        static RootIO *fInstance;

        const char *fOutFilename;
        TFile *f_file;
        TTree *t_main;

};

#endif