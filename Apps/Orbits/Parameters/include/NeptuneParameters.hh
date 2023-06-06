#ifndef NeptuneParameters_H
#define NeptuneParameters_H 

#include "Vector3D.hh"

class NeptuneParameters {
    public:
        NeptuneParameters();
        ~NeptuneParameters();

        void Init();

        static NeptuneParameters *GetInstance();

        Vector3D *GetStartPos(){ return fStartPos;}
        Vector3D *GetStartVel(){ return fStartVel;}
        double GetMass(){ return fMass;}
        double GetRadius(){ return fRadius;}

    private:
        static NeptuneParameters *fInstance;
        Vector3D *fStartPos;
        Vector3D *fStartVel;
        double fMass;
        double fAU;
        double fRadius;
};

#endif