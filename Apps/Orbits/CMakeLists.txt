cmake_minimum_required(VERSION 3.20)

project(OrbitSim)

find_package(ROOT REQUIRED COMPONENTS RIO)
if( ${ROOT_FOUND} )
    include(${ROOT_USE_FILE})
    message (STATUS "Found ROOT ${ROOT_VERSION} at ${ROOT_DIR}")
else()
    message (FATAL_ERROR "ROOT not found")
endif()

set(CMAKE_BINARY_DIR "bin/")
set(EXECUTABLE_OUTPUT_PATH ${CMAKE_BINARY_DIR})
#set(LIBRARY_OUTPUT_PATH "${CMAKE_BINARY_DIR}/lib")

include_directories(${ROOT_INCLUDE_DIR})
link_directories(${ROOT_LIBRARY_DIR})

file(GLOB SRC
     "src/*.cc")

set(MAIN_FILE Orbits.cc)
include_directories(include)


add_executable(OrbitSim ${MAIN_FILE} ${SRC})

target_link_libraries(OrbitSim ROOT::RIO)   
target_link_libraries(OrbitSim ${ROOT_LIBRARIES} )

ROOT_GENERATE_DICTIONARY(Vector3DDict Vector3D.hh MODULE OrbitSim LINKDEF LinkDef.h)
target_include_directories(Vector3DDict PUBLIC "include/")

add_library(myLib SHARED src/Vector3D.cc)

target_link_libraries(${PROJECT_NAME} myLib)


set(PlanetsList Earth)
set(PlanetsIncludeDirs ${PlanetsList})
list(TRANSFORM PlanetsIncludeDirs PREPEND "Planets/")
list(TRANSFORM PlanetsIncludeDirs APPEND "/include")
include_directories(${PlanetsIncludeDirs})
target_link_libraries(${PROJECT_NAME} ${PlanetsList})

add_subdirectory(Planets)