cmake_minimum_required(VERSION 3.10)

project(OrbitSim)

file(GLOB SRC
     "src/*.cc"
)

set(MAIN_FILE Orbits.cc)
include_directories(include)
add_executable(OrbitSim ${MAIN_FILE} ${SRC})

