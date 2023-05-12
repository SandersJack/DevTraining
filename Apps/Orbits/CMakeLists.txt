project(Orbits)

file(GLOB SOURCES src/*.cc)
file(GLOB headers src/*.hh)


add_executable(OrbitSim Orbits.cc ${SOURCES})

include_directories(include)