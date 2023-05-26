#ifndef InputManager_H
#define InputManager_H 1

#include <iostream>
#include <string>
#include <vector>
#include <map>

class InputManager {

    public:
        InputManager();

        static InputManager *GetInstance();

        void ParsePlanetFile(std::string file="config/PlanetsList.dat");

        std::vector<std::string> GetPlanetList(){ return fPlanetList;}
        std::map<std::string, std::string> GetMoonList(){ return fMoonsList;}

    private:
        static InputManager *fInstance;

        std::vector<std::string> fPlanetList;
        std::map<std::string, std::string> fMoonsList;

};

#endif