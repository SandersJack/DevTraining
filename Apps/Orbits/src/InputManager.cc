#include "InputManager.hh"

#include <iostream>
#include <string>
#include <fstream>

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
    inFile.open(file);

    if (!inFile) {
        std::cout << "Unable to open file" << std::endl;
        exit(1); // terminate with error
    }
    std::cout << file << std::endl;
    std::string x = "c";
    if(file.find("Planets") != std::string::npos) {
        while (std::getline(inFile, x)) {
            if(x.find('#') != std::string::npos)
                continue;
            fPlanetList.push_back(x);
        }
    } else {
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
    }

}