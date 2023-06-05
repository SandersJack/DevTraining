#ifndef MoonParameters_H
#define MoonParameters_H 

#include "Vector3D.hh"

class MoonParameters {
    public:
        MoonParameters();
        ~MoonParameters();

        void Init();

        static MoonParameters *GetInstance();

        Vector3D *GetStartPos(){ return fStartPos;}
        Vector3D *GetStartVel(){ return fStartVel;}
        double GetMass(){ return fMass;}

    private:
        static MoonParameters *fInstance;
        Vector3D *fStartPos;
        Vector3D *fStartVel;
        double fMass;
        double fAU;
};

#endif