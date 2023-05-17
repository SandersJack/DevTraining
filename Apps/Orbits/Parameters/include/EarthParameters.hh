#ifndef EarthParameters_H
#define EarthParameters_H 

#include "Vector3D.hh"

class EarthParameters {
    public:
        EarthParameters();
        ~EarthParameters();

        void Init();

        static EarthParameters *GetInstance();

        Vector3D *GetStartPos(){ return fStartPos;}
        Vector3D *GetStartVel(){ return fStartVel;}
        double GetMass(){ return fMass;}

    private:
        static EarthParameters *fInstance;
        Vector3D *fStartPos;
        Vector3D *fStartVel;
        double fMass;
        double fAU;
};

#endif