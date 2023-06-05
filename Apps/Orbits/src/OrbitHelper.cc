#include "OrbitHelper.hh"

#include <sys/stat.h>
#include <sstream>


OrbitHelper::OrbitHelper(){

}

std::pair<double, double> OrbitHelper::GetMemoryUsage() {
  std::ifstream file;
  file.open("/proc/self/stat");
  std::string datum;
  double virtualMemory = 0.;
  double residentMemory = 0.;
  if(file.is_open()) {
    std::getline(file, datum);
    std::istringstream ss(datum);
    std::string del;
    int i{0};
    while(getline(ss, del, ' ')) {
        if(i == 22)
            virtualMemory = (std::stod(del)) / (1024. * 1024.); //virtual memory is in bytes
        if(i == 23)
            residentMemory = (std::stod(del)) * 4 / (1024.); //resident memory is in pages (4kb each)
        i++;
    }   
  }
  file.close();
  return std::make_pair(virtualMemory, residentMemory);
}

std::string OrbitHelper::TimeString(time_t &time) {
  static char Time[100];
  std::strftime(Time, sizeof(Time), "%a %b %d %H:%M:%S %Y", std::localtime(&time));
  return std::string(Time);
}

std::string OrbitHelper::TimeString() {
  time_t now = time(0);
  return TimeString(now);
}

