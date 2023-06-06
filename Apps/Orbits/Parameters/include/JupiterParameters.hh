#ifndef JupiterParameters_H
#define JupiterParameters_H 

#include "Vector3D.hh"

class JupiterParameters {
    public:
        JupiterParameters();
        ~JupiterParameters();

        void Init();

        static JupiterParameters *GetInstance();

        Vector3D *GetStartPos(){ return fStartPos;}
        Vector3D *GetStartVel(){ return fStartVel;}
        double GetMass(){ return fMass;}
        double GetRadius(){ return fRadius;}

    private:
        static JupiterParameters *fInstance;
        Vector3D *fStartPos;
        Vector3D *fStartVel;
        double fMass;
        double fAU;
        double fRadius;
};

#endif