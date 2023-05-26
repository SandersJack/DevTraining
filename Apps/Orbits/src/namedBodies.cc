#include "namedBodies.hh"

#include "Earth.hh"
#include "Mars.hh"

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