#ifndef namedBodies_H
#define namedBodies_H 1

#include "Planets.hh"
#include "Moons.hh"
#include "Satellite.hh"
#include <iostream>
#include <string>

class namedBodies {

    public:
        namedBodies();

        static namedBodies *GetInstance();

        Planets *GetPlanetFunc(std::string planet);
        Moons *GetMoonsFunc(std::string moo);
        Satellite *GetSatelliteFunc(std::string sat);

    private:
        static namedBodies *fInstance;
};

#endif