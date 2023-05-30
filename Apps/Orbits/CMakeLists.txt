cmake_minimum_required(VERSION 3.20)

include(CMakePrintHelpers)

project(OrbitSim)

find_package(ROOT REQUIRED COMPONENTS RIO)
if( ${ROOT_FOUND} )
    include(${ROOT_USE_FILE})
    message (STATUS "Found ROOT ${ROOT_VERSION} at ${ROOT_DIR}")
else()
    message (FATAL_ERROR "ROOT not found")
endif()

set(CMAKE_BINARY_DIR "${CMAKE_CURRENT_SOURCE_DIR}/build/")
set(EXECUTABLE_OUTPUT_PATH ".")
set(LIBRARY_OUTPUT_PATH "${CMAKE_BINARY_DIR}")
message(LIB="${LIBRARY_OUTPUT_PATH}")

include_directories(${ROOT_INCLUDE_DIR})
link_directories(${ROOT_LIBRARY_DIR})

file(GLOB SRC
     "src/*.cc")

set(MAIN_FILE Orbits.cc)
include_directories(include)


add_executable(OrbitSim ${MAIN_FILE} ${SRC})

target_link_libraries(OrbitSim ROOT::RIO)   
target_link_libraries(OrbitSim ${ROOT_LIBRARIES} )

ROOT_GENERATE_DICTIONARY(Vector3DDict Vector3D.hh Planets.hh Satellite.hh Moons.hh MODULE OrbitSim LINKDEF LinkDef.h)
target_include_directories(Vector3DDict PUBLIC "include/")
add_library(myLib SHARED src/Vector3D.cc src/Planets.cc src/Moons.cc src/Satellite.cc)
target_link_libraries(${PROJECT_NAME} myLib)


include_directories("Parameters/include")
target_link_libraries(${PROJECT_NAME} Parameters)
add_subdirectory(Parameters)

set(PlanetsList Earth Mars Jupiter)
set(PlanetsIncludeDirs ${PlanetsList})
list(TRANSFORM PlanetsIncludeDirs PREPEND "Planets/")
list(TRANSFORM PlanetsIncludeDirs APPEND "/include")
include_directories(${PlanetsIncludeDirs})
#foreach(P IN ${PlanetsList})
#    target_link_libraries(${PROJECT_NAME} ${P}Persistency) 
#endforeach()

message(PLANET_LIST="${PlanetsList}")


add_subdirectory(Planets)

message(PROJECT_SOURCE_DIR="${CMAKE_BINARY_DIR}Planets/${PlanetsList}/lib${PlanetsList}Persistency_rdict.pcm")

foreach(Planets ${PlanetsList})
    message(STATUS "${Planets}")
    message(STATUS "${CMAKE_BINARY_DIR}Planets/${Planets}/lib${Planets}Persistency_rdict.pcm")
    ADD_CUSTOM_TARGET(${Planets}_rdict_target ALL
        COMMAND ${CMAKE_COMMAND} -E create_symlink "${CMAKE_BINARY_DIR}Planets/${Planets}/lib${Planets}Persistency_rdict.pcm" "${CMAKE_CURRENT_BINARY_DIR}/lib${Planets}Persistency_rdict.pcm")

    ADD_CUSTOM_TARGET(${Planets}_rootmap_target ALL
        COMMAND ${CMAKE_COMMAND} -E create_symlink "${CMAKE_BINARY_DIR}Planets/${Planets}/lib${Planets}Persistency.rootmap" "${CMAKE_CURRENT_BINARY_DIR}/lib${Planets}Persistency.rootmap")
endforeach()
