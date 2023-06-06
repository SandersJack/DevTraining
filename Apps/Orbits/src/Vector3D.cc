#include "Vector3D.hh"
#include <iostream>

ClassImp(Vector3D)

Vector3D::Vector3D(): fx(0), fy(0), fz(0) {

}

Vector3D::Vector3D(double in_x, double in_y, double in_z): fx(0), fy(0), fz(0) {
    fx = in_x;
    fy = in_y;
    fz = in_z;
}

Vector3D::Vector3D(Vector3D *val): fx(0), fy(0), fz(0) {
    fx = val->GetX();
    fy = val->GetY();
    fz = val->GetZ();
}

Vector3D::~Vector3D(){
}

void Vector3D::Print(){
    std::cout << "{ " << fx << " , " << fy << " , " << fz << " }" << std::endl;
}