#ifndef Vector3D_H
#define Vector3D_H 

#include "TObject.h"

class Vector3D: public TObject {

    public:
        Vector3D();
        Vector3D(double in_x, double in_y, double in_z);
        Vector3D(Vector3D *val);
        ~Vector3D();
        
        double GetX(){return fx;}
        double GetY(){return fy;}
        double GetZ(){return fz;}

        void SetX(double val){fx = val;}
        void SetY(double val){fy = val;}
        void SetZ(double val){fz = val;}
        void Set(double val_x, double val_y, double val_z){fx = val_x, fy=val_y; fz=val_z;};
        void Set(Vector3D *val){fx = val->GetX();fy = val->GetY();fz = val->GetZ();};
        
        void AddX(double val){fx += val;}
        void AddY(double val){fy += val;}
        void AddZ(double val){fz += val;}

        void Print();

        ClassDef(Vector3D, 1);
    private:
        double fx, fy,fz;
};

#endif
