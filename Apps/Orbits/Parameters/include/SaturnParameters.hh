#ifndef SaturnParameters_H
#define SaturnParameters_H 

#include "Vector3D.hh"

class SaturnParameters {
    public:
        SaturnParameters();
        ~SaturnParameters();

        void Init();

        static SaturnParameters *GetInstance();

        Vector3D *GetStartPos(){ return fStartPos;}
        Vector3D *GetStartVel(){ return fStartVel;}
        double GetMass(){ return fMass;}
        double GetRadius(){ return fRadius;}

    private:
        static SaturnParameters *fInstance;
        Vector3D *fStartPos;
        Vector3D *fStartVel;
        double fMass;
        double fAU;
        double fRadius;
};

#endif