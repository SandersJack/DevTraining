#ifndef PhysicsEqs_H
#define PhysicsEqs_H 

#include "Vector3D.hh"

class PhysicsEqs{

    public:
        PhysicsEqs();
        ~PhysicsEqs();
        static PhysicsEqs *GetInstance();

        Vector3D GetAcceleration(Vector3D pos1, Vector3D pos2, double mass1, double mass2, double soft);
        Vector3D GetSatelliteAcceleration(Vector3D pos1, double mass1, double soft);


    private:
        static PhysicsEqs *fInstance;
        double fG_const;
};

#endif

