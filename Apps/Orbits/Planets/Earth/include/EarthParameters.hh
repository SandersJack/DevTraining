#ifndef EarthParameters_H
#define EarthParameters_H 

class EarthParameters {
    public:
        EarthParameters();
        ~EarthParameters();

        static EarthParameters *GetInstance();

    private:
        static EarthParameters *fInstance;
};

#endif