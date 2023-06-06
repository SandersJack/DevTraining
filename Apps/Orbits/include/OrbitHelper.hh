#ifndef OrbitHelper_H
#define OrbitHelper_H 1

#include <iostream>
#include <string>
#include <fstream>
#include <ctime>

class OrbitHelper {

    public:
        OrbitHelper();

        std::pair<double, double> GetMemoryUsage();
        std::string TimeString(time_t &time);
        std::string TimeString();

    private:


};

#endif