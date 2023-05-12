project(Orbits)

file(GLOB SOURCES src/*.cc)
file(GLOB headers src/*.hh)


add_executable(Orbits Orbits.cc ${SOURCES})

include_directories(include)