#ifndef Venus_H
#define Venus_H

#include "Planets.hh"
#include "VenusParameters.hh"
#include "PhysicsEqs.hh"
#include "TTree.h"
#include "Vector3D.hh"


class Venus: public Planets {
    public:
        Venus();
        ~Venus();

        void Init();
        void InitRootIO(TTree *t_main);
        void PrintPos();
        
        virtual void NextStep();

        ClassDef(Venus,1);

    private:


    
};

#endif