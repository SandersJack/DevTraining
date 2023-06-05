#ifndef VenusParameters_H
#define VenusParameters_H 

#include "Vector3D.hh"

class VenusParameters {
    public:
        VenusParameters();
        ~VenusParameters();

        void Init();

        static VenusParameters *GetInstance();

        Vector3D *GetStartPos(){ return fStartPos;}
        Vector3D *GetStartVel(){ return fStartVel;}
        double GetMass(){ return fMass;}
        double GetRadius(){ return fRadius;}

    private:
        static VenusParameters *fInstance;
        Vector3D *fStartPos;
        Vector3D *fStartVel;
        double fMass;
        double fAU;
        double fRadius;
};

#endif