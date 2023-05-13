#ifndef Vector3D_H
#define Vector3D_H 

class Vector3D {

    public:
        Vector3D();
        Vector3D(double in_x, double in_y, double in_z);

        void Set(double val_x, double val_y, double val_z){fx = val_x, fy=val_y; fz=val_z;};
        double GetX(){return fx;}
        double GetY(){return fy;}
        double GetZ(){return fz;}


    private:
        double fx, fy,fz;
};

#endif
