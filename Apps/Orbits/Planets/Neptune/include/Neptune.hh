#ifndef Neptune_H
#define Neptune_H

#include "Planets.hh"
#include "NeptuneParameters.hh"
#include "PhysicsEqs.hh"
#include "TTree.h"
#include "Vector3D.hh"


class Neptune: public Planets {
    public:
        Neptune();
        ~Neptune();

        void Init();
        void InitRootIO(TTree *t_main);
        void PrintPos();
        
        virtual void NextStep();

        ClassDef(Neptune,1);

    private:


    
};

#endif