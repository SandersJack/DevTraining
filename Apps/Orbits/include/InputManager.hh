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

        std::map<std::string, std::pair<std::string,std::string>> GetSatelliteList(){ return fSatelliteList;}
        std::map<std::string, std::vector<double>> GetSatelliteAtributesList(){ return fSatelliteAtributesList;}

    private:
        static InputManager *fInstance;

        std::vector<std::string> fPlanetList;

        std::map<std::string, std::string> fMoonsList;

        std::map<std::string, std::pair<std::string,std::string>> fSatelliteList;
        std::map<std::string, std::vector<double>> fSatelliteAtributesList;

};

#endif