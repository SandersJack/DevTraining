#ifndef Saturn_H
#define Saturn_H

#include "Planets.hh"
#include "SaturnParameters.hh"
#include "PhysicsEqs.hh"
#include "TTree.h"
#include "Vector3D.hh"


class Saturn: public Planets {
    public:
        Saturn();
        ~Saturn();

        void Init();
        void InitRootIO(TTree *t_main);
        void PrintPos();
        
        virtual void NextStep();

        ClassDef(Saturn,1);

    private:


    
};

#endif