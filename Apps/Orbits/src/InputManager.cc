#include "InputManager.hh"

#include <iostream>
#include <string>
#include <fstream>
#include <sstream>

InputManager::InputManager() {

}

InputManager *InputManager::fInstance = nullptr;

InputManager *InputManager::GetInstance() {
    if(!fInstance)
        fInstance = new InputManager();
    return fInstance;
}


void InputManager::ParsePlanetFile(std::string file) {
    std::ifstream inFile;
    std::cout << "[InputManager] Opening Config File: "<< file << std::endl;
    inFile.open(file);

    if (!inFile) {
        std::cout << "Unable to open file" << std::endl;
        exit(1); // terminate with error
    }
    
    std::string x = "c";
    if(file.find("Planets") != std::string::npos) {
        while (std::getline(inFile, x)) {
            if(x.find('#') != std::string::npos)
                continue;
            fPlanetList.push_back(x);
        }
    } else if(file.find("Moons") != std::string::npos) {
        while (std::getline(inFile, x)) {
            if(x.find('#') != std::string::npos)
                continue;
            std::string Moon = "";
            std::string Planet = "";
            bool write = false;
            for (int i = 0; i < x.length(); i++) {
                // Print current character
                if(x[i-1] == '('){
                    Moon = x.substr(0, i-1);
                    write = true;
                }
                if(write){
                    if(x[i] == ')')
                        break;
                    Planet += x[i];
                }
            }
            fMoonsList.insert({Planet,Moon});
        }
    } else if(file.find("Satellite") != std::string::npos) {
        while (std::getline(inFile, x)) {
            if(x.find('#') != std::string::npos)
                continue;
            
            std::vector<std::string> tokens;
        
            std::istringstream iss(x);
            std::string s;
            while (iss >> s) {
                tokens.push_back(s);
            }
            
            std::string Sat = "";
            std::string Planet = "";
            std::vector<double> Atributes;
            bool write = false;
            for(int t{0}; t<tokens.size(); t++){
                if(t == 0){
                    for (int i = 0; i < tokens[t].length(); i++) {
                        // Print current character
                        if(x[i-1] == '('){
                            Sat = tokens[t].substr(0, i-1);
                            write = true;
                        }
                        if(write){
                            if(tokens[t][i] == ')')
                                break;
                            Planet += x[i];
                        }
                    }
                    fSatelliteList.insert({Planet,Sat});
                }
                if(t>0){
                    int inter = std::stod(tokens[t]);
                    Atributes.push_back(inter);
                }
            }
            fSatelliteAtributesList.insert({Sat,Atributes});
        }
    }

}