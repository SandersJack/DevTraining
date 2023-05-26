#ifndef InputManager_H
#define InputManager_H 1

#include <iostream>
#include <string>
#include <vector>

class InputManager {

    public:
        InputManager();

        static InputManager *GetInstance();

        void ParsePlanetFile(std::string file="config/PlanetsList.dat");

        std::vector<std::string> GetPlanetList(){ return fPlanetList;}

    private:
        static InputManager *fInstance;

        std::vector<std::string> fPlanetList;
};

#endif