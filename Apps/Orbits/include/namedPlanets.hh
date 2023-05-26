#ifndef namedPlanets_H
#define namedPlanets_H 1

#include "Planets.hh"
#include <iostream>
#include <string>

class namedPlanets {

    public:
        namedPlanets();

        static namedPlanets *GetInstance();

        Planets *GetPlanetFunc(std::string planet);

    private:
        static namedPlanets *fInstance;
};

#endif