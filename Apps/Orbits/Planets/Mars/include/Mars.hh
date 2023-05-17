#ifndef Mars_H
#define Mars_H

#include "Planets.hh"
#include "MarsParameters.hh"
#include "PhysicsEqs.hh"
#include "TTree.h"
#include "Vector3D.hh"


class Mars: public Planets {
    public:
        Mars();
        ~Mars();

        void Init();
        void InitRootIO(TTree *t_main);
        void PrintPos();
        
        virtual void NextStep();

        ClassDef(Mars,1);

    private:


    
};

#endif