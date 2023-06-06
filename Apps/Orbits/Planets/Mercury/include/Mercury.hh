#ifndef Mercury_H
#define Mercury_H

#include "Planets.hh"
#include "MercuryParameters.hh"
#include "PhysicsEqs.hh"
#include "TTree.h"
#include "Vector3D.hh"


class Mercury: public Planets {
    public:
        Mercury();
        ~Mercury();

        void Init();
        void InitRootIO(TTree *t_main);
        void PrintPos();
        
        virtual void NextStep();

        ClassDef(Mercury,1);

    private:


    
};

#endif