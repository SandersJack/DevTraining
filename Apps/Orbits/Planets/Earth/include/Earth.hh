#ifndef Earth_H
#define Earth_H

#include "Planets.hh"
#include "EarthParameters.hh"
#include "PhysicsEqs.hh"
#include "TTree.h"


class Earth: public Planets {
    public:
        Earth();
        ~Earth();

        void Init();
        void InitRootIO(TTree *t_main);
        
        virtual void NextStep();

        ClassDef(Earth,1);

    private:
        EarthParameters *fEParam;
        PhysicsEqs *fPhysicsEqs;

    
};

#endif