#ifndef UranusParameters_H
#define UranusParameters_H 

#include "Vector3D.hh"

class UranusParameters {
    public:
        UranusParameters();
        ~UranusParameters();

        void Init();

        static UranusParameters *GetInstance();

        Vector3D *GetStartPos(){ return fStartPos;}
        Vector3D *GetStartVel(){ return fStartVel;}
        double GetMass(){ return fMass;}
        double GetRadius(){ return fRadius;}

    private:
        static UranusParameters *fInstance;
        Vector3D *fStartPos;
        Vector3D *fStartVel;
        double fMass;
        double fAU;
        double fRadius;
};

#endif