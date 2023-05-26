#include "namedPlanets.hh"

#include "Earth.hh"
#include "Mars.hh"

namedPlanets::namedPlanets(){

}

namedPlanets *namedPlanets::fInstance = nullptr;

namedPlanets *namedPlanets::GetInstance() {
  if(!fInstance)
    fInstance = new namedPlanets();
  return fInstance;
};


Planets *namedPlanets::GetPlanetFunc(std::string planet) {
    if(planet == "Earth"){
        return new Earth();
    } else if (planet == "Mars") {
        return new Mars();
    } else {
        return nullptr;
    }
}