#ifndef Moon_H
#define Moon_H

#include "Planets.hh"
#include "Earth.hh"
#include "MoonParameters.hh"
#include "PhysicsEqs.hh"
#include "TTree.h"
#include "Vector3D.hh"
#include "TObject.h"


class Moon: public TObject {
    public:
        Moon();
        ~Moon();

        void Init();
        void InitRootIO(TTree *t_main);
        void PrintPos();

        void SetPosition(Vector3D val){ fPosition = val;};
        void SetVelocity(Vector3D val){ fVelocity = val;};
        void SetAcceleration(Vector3D val){ fAcceleration = val;}
        void SetMass(double val){ fMass = val;};

        Vector3D GetPosition(){ return fPosition;}
        Vector3D GetVelocity(){ return fVelocity;}
        Vector3D GetAcceleration(){ return fAcceleration;}
        double GetMass(){return fMass;}

        void SetTimeStep(double val){ fdt = val;}
        
        void NextStep(Earth *E);

        ClassDef(Moon,1);

    private:

        Vector3D fSunPosition;
        Vector3D fPosition;
        Vector3D fVelocity;
        Vector3D fAcceleration;

        double fMass;
        double fdt;

    
};

#endif