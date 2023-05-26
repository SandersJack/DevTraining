#include "InputManager.hh"


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

    std::string x = "c";
    
    while (std::getline(inFile, x)) {
        if(x.find('#') != std::string::npos)
            continue;
        fPlanetList.push_back(x);
    }
    

}