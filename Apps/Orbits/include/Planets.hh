#ifndef Planets_H
#define Planets_H 

#include "TObject.h"
#include "Vector3D.hh"
#include <cmath>

class Planets: public TObject {

    public:
        Planets();
        ~Planets();

        void SetPosition(Vector3D val){ fPosition = val;};
        void SetVelocity(Vector3D val){ fVelocity = val;};
        void SetAcceleration(Vector3D val){ fAcceleration = val;}
        void SetMass(double val){ fMass = val;};

        Vector3D GetPosition(){ return fPosition;}
        Vector3D GetVelocity(){ return fVelocity;}
        Vector3D GetAcceleration(){ return fAcceleration;}
        double GetMass(){return fMass;}

        double GetAngle(){return atan(fPosition.GetY()/fPosition.GetX());}

        void SetTimeStep(double val){ fdt = val;}

        virtual void NextStep() = 0;

    public:
        Vector3D fPosition;
        Vector3D fVelocity;
        Vector3D fAcceleration;

        double fMass;
        double fdt;
        double fTime;

        ClassDef(Planets,1);


};

#endif