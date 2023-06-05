#ifndef Uranus_H
#define Uranus_H

#include "Planets.hh"
#include "UranusParameters.hh"
#include "PhysicsEqs.hh"
#include "TTree.h"
#include "Vector3D.hh"


class Uranus: public Planets {
    public:
        Uranus();
        ~Uranus();

        void Init();
        void InitRootIO(TTree *t_main);
        void PrintPos();
        
        virtual void NextStep();

        ClassDef(Uranus,1);

    private:


    
};

#endif