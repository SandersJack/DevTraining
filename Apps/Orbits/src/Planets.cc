#include "Planets.hh"

ClassImp(Planets)

Planets::Planets():fMass(0), fdt(0) , fTime(0), fRadius(0){

}

Planets::~Planets(){}

double Planets::GetAngle(){

    double angle = atan(fPosition.GetY()/fPosition.GetX());
    if (angle >= 0 && fPosition.GetX() > 0 && fPosition.GetY() > 0){
        return angle;
    } else if (fPosition.GetX() > 0 && fPosition.GetY() < 0){
        return 2*M_PI + angle;
    }
    else{
        return angle +  M_PI;
    }

}