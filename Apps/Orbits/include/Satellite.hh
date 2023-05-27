#ifndef Satellite_H
#define Satellite_H

#include "TObject.h"
#include "Vector3D.hh"
#include <cmath>
#include <iostream>

class Satellite: public TObject {
    public:
        Satellite();
        ~Satellite();

        void SetStartPosition(Vector3D body_val,double sat_val);
        void SetStartVelocity(Vector3D body_val,double sat_val);

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

        void NextStep();

    private:

        Vector3D fPosition;
        Vector3D fVelocity;
        Vector3D fAcceleration;

        double fMass;
        double fdt;
        double fTime;

        ClassDef(Satellite,1);
};

#endif