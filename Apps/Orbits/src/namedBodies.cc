#include "namedBodies.hh"

#include "Earth.hh"
#include "Mars.hh"
#include "Jupiter.hh"
#include "Saturn.hh"
#include "Uranus.hh"
#include "Neptune.hh"

#include "Moon.hh"

namedBodies::namedBodies(){

}

namedBodies *namedBodies::fInstance = nullptr;

namedBodies *namedBodies::GetInstance() {
  if(!fInstance)
    fInstance = new namedBodies();
  return fInstance;
};


Planets *namedBodies::GetPlanetFunc(std::string planet) {
    if(planet == "Earth"){
        return new Earth();
    } else if (planet == "Mars") {
        return new Mars();
    } else if (planet == "Jupiter") {
        return new Jupiter();
    } else if (planet == "Saturn") {
        return new Saturn();
    } else if (planet == "Uranus") {
        return new Uranus();
    } else if (planet == "Neptune") {
        return new Neptune();
    } else {
        return nullptr;
    }
}

Moons *namedBodies::GetMoonsFunc(std::string moo) {
    if(moo == "Moon"){
        return new Moon();
    } else {
        return nullptr;
    }
}

Satellite *namedBodies::GetSatelliteFunc(std::string sat) {
    if(sat == "Satellite"){
        return new Satellite();
    } else {
        return nullptr;
    }
}