#ifndef MarsParameters_H
#define MarsParameters_H 

#include "Vector3D.hh"

class MarsParameters {
    public:
        MarsParameters();
        ~MarsParameters();

        void Init();

        static MarsParameters *GetInstance();

        Vector3D *GetStartPos(){ return fStartPos;}
        Vector3D *GetStartVel(){ return fStartVel;}
        double GetMass(){ return fMass;}

    private:
        static MarsParameters *fInstance;
        Vector3D *fStartPos;
        Vector3D *fStartVel;
        double fMass;
        double fAU;
};

#endif