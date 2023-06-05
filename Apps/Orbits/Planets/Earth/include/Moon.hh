#ifndef Moon_H
#define Moon_H

#include "Moons.hh"
#include "Earth.hh"
#include "MoonParameters.hh"
#include "PhysicsEqs.hh"
#include "TTree.h"
#include "Vector3D.hh"
#include "TObject.h"


class Moon: public Moons {
    public:
        Moon();
        ~Moon();

        void Init();
        void InitRootIO(TTree *t_main);
        void PrintPos();
        
        virtual void NextStep();

        ClassDef(Moon,1);

    private:

        Vector3D fSunPosition;
};

#endif