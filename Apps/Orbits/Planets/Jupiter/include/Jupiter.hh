#ifndef Jupiter_H
#define Jupiter_H

#include "Planets.hh"
#include "JupiterParameters.hh"
#include "PhysicsEqs.hh"
#include "TTree.h"
#include "Vector3D.hh"


class Jupiter: public Planets {
    public:
        Jupiter();
        ~Jupiter();

        void Init();
        void InitRootIO(TTree *t_main);
        void PrintPos();
        
        virtual void NextStep();

        ClassDef(Jupiter,1);

    private:


    
};

#endif