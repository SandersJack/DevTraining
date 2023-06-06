#ifndef Satellite_H
#define Satellite_H

#include "TObject.h"
#include "Vector3D.hh"
#include "Planets.hh"
#include <cmath>
#include <iostream>

class Satellite: public TObject {
    public:
        Satellite();
        ~Satellite();

        void SetStartPosition(double body_radius, Vector3D body_val,double sat_val);
        void SetStartVelocity(Vector3D body_val,double sat_val);

        void SetPosition(Vector3D val){ fPosition = val;};
        void SetVelocity(Vector3D val){ fVelocity = val;};
        void SetAcceleration(Vector3D val){ fAcceleration = val;}
        void SetMass(double val){ fMass = val;};
        void SetName(std::string val) {fName = val;}
        void SetBody(Planets *val) {fBody = val;}
        void SetStartAngle(double val) {fStartAngle = val;}
        void SetStartTime(double val) {fStartTime = val*24*50*60;}

        Vector3D GetPosition(){ return fPosition;}
        Vector3D GetVelocity(){ return fVelocity;}
        Vector3D GetAcceleration(){ return fAcceleration;}
        double GetMass(){return fMass;}
        std::string GetName(){ return fName;}

        double GetAngle(){return atan(fPosition.GetY()/fPosition.GetX());}

        void SetTimeStep(double val){ fdt = val;}

        void NextStep();

    private:
    
        Planets *fBody;

        Vector3D fPosition;
        Vector3D fVelocity;
        Vector3D fAcceleration;

        double fMass;
        double fdt;
        double fTime;
        double fStartAngle;
        double fStartTime; // Seconds
        double fOrbitRadius;
        double fDeltaV;
        bool fStart;


        std::string fName;

        ClassDef(Satellite,1);
};

#endif