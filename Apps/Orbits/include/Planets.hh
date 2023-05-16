#ifndef Planets_H
#define Planets_H 

#include "TObject.h"
#include "Vector3D.hh"

class Planets: public TObject {

    public:
        Planets();
        ~Planets();

        void SetPosition(Vector3D *val){ fPosition = val;};
        void SetVelocity(Vector3D *val){ fVelocity = val;};
        void SetAcceleration(Vector3D *val){ fAcceleration = val;}
        void SetMass(double val){ fMass = val;};

        Vector3D *SetPosition(){ return fPosition;}
        Vector3D *SetVelocity(){ return fVelocity;}
        Vector3D *SetAcceleration(){ return fAcceleration;}
        double SetMass(){return fMass;}

        void SetTimeStep(double val){ fdt = val;}

        virtual void NextStep() = 0;

    public:
        Vector3D *fPosition;
        Vector3D *fVelocity;
        Vector3D *fAcceleration;

        double fMass;
        double fdt;

        ClassDef(Planets,1);


};

#endif