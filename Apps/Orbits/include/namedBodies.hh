#ifndef namedBodies_H
#define namedBodies_H 1

#include "Planets.hh"
#include "Moons.hh"
#include <iostream>
#include <string>

class namedBodies {

    public:
        namedBodies();

        static namedBodies *GetInstance();

        Planets *GetPlanetFunc(std::string planet);
        Moons *GetMoonsFunc(std::string moo);

    private:
        static namedBodies *fInstance;
};

#endif