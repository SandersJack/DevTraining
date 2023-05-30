#ifndef MercuryParameters_H
#define MercuryParameters_H 

#include "Vector3D.hh"

class MercuryParameters {
    public:
        MercuryParameters();
        ~MercuryParameters();

        void Init();

        static MercuryParameters *GetInstance();

        Vector3D *GetStartPos(){ return fStartPos;}
        Vector3D *GetStartVel(){ return fStartVel;}
        double GetMass(){ return fMass;}
        double GetRadius(){ return fRadius;}

    private:
        static MercuryParameters *fInstance;
        Vector3D *fStartPos;
        Vector3D *fStartVel;
        double fMass;
        double fAU;
        double fRadius;
};

#endif