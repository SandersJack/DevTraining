#include "Satellite.hh"
#include "PhysicsEqs.hh"
#include <cmath>

ClassImp(Satellite)

Satellite::Satellite():fMass(0), fdt(0) , fTime(0), fName("c"), fStartAngle(-1), fStartTime(-1), fStart(true) {

}

Satellite::~Satellite(){}

void Satellite::SetStartPosition(double body_radius, Vector3D body_val,double sat_val){

    fPosition = Vector3D(body_val);
    fPosition.AddX(sat_val*1e3+body_radius);
    fOrbitRadius = sat_val*1e3;

}

void Satellite::SetStartVelocity(Vector3D body_val,double sat_val){

    fVelocity = Vector3D(body_val);
    fVelocity.AddY(sat_val);
    fDeltaV = sat_val;

}


void Satellite::NextStep() {

    if (fStartAngle != -1 && fStartTime > -1){
        std::cout << "[Satellite] Error: Can only use Either StartAngle or StartTime" <<std::endl;
        exit(1);
    }

    if((fBody->GetAngle()*180 / M_PI < fStartAngle && fStart && fStartAngle != -1) || (fTime < fStartTime && fStart && fStartTime > -1)){
        fPosition.SetX(fBody->GetPosition().GetX() + fOrbitRadius*cos(fBody->GetAngle()));
        fPosition.SetY(fBody->GetPosition().GetY() + fOrbitRadius*sin(fBody->GetAngle()));
    } else {
        if(fStart){
            fPosition.SetX(fBody->GetPosition().GetX() + fOrbitRadius*cos(fBody->GetAngle()));
            fPosition.SetY(fBody->GetPosition().GetY() + fOrbitRadius*sin(fBody->GetAngle()));
            //std::cout << fBody->GetAngle() << " " << fStartAngle << std::endl;
            fVelocity = Vector3D(fBody->GetVelocity());
            //std::cout << fBody->GetVelocity().GetX() << " " << fBody->GetVelocity().GetY() << std::endl;
            fVelocity.AddX(fDeltaV*sin(fBody->GetAngle()));
            fVelocity.AddY(fDeltaV*cos(fBody->GetAngle()));
            fStart = false;
            //std::cout << fDeltaV*sin(fBody->GetAngle()) << " " << fDeltaV*cos(fBody->GetAngle()) <<std::endl;
            //std::cout << fDeltaV*sin(M_PI) << " " << fDeltaV*cos(M_PI) <<std::endl;
        }

        PhysicsEqs *PhysicsEqs = PhysicsEqs::GetInstance();

        
        Vector3D Sat_a = PhysicsEqs->GetSatelliteAcceleration(fPosition, fMass, 1e10);

        fAcceleration = Sat_a;

        fVelocity.AddX(Sat_a.GetX()*fdt);
        fVelocity.AddY(Sat_a.GetY()*fdt);
        fVelocity.AddZ(Sat_a.GetZ()*fdt);


        fPosition.AddX(fVelocity.GetX()*fdt);
        fPosition.AddY(fVelocity.GetY()*fdt);
        fPosition.AddZ(fVelocity.GetZ()*fdt);
        
    }
    fTime += fdt;
}