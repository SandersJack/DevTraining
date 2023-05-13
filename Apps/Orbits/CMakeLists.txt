cmake_minimum_required(VERSION 3.10)

project(OrbitSim)

set(CMAKE_BINARY_DIR "bin/")
set(EXECUTABLE_OUTPUT_PATH ${CMAKE_BINARY_DIR})

file(GLOB SRC
     "src/*.cc"
)

set(MAIN_FILE Orbits.cc)
include_directories(include)
add_executable(OrbitSim ${MAIN_FILE} ${SRC})

