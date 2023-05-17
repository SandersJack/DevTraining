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

set(CMAKE_BINARY_DIR "${CMAKE_CURRENT_SOURCE_DIR}")
set(EXECUTABLE_OUTPUT_PATH ".")
set(LIBRARY_OUTPUT_PATH "${CMAKE_BINARY_DIR}/lib")

include_directories(${ROOT_INCLUDE_DIR})
link_directories(${ROOT_LIBRARY_DIR})

file(GLOB SRC
     "src/*.cc")

set(MAIN_FILE Orbits.cc)
include_directories(include)


add_executable(OrbitSim ${MAIN_FILE} ${SRC})

target_link_libraries(OrbitSim ROOT::RIO)   
target_link_libraries(OrbitSim ${ROOT_LIBRARIES} )

ROOT_GENERATE_DICTIONARY(Vector3DDict Vector3D.hh Planets.hh MODULE OrbitSim LINKDEF LinkDef.h)
target_include_directories(Vector3DDict PUBLIC "include/")
add_library(myLib SHARED src/Vector3D.cc src/Planets.cc)
target_link_libraries(${PROJECT_NAME} myLib)


include_directories("Parameters/include")
target_link_libraries(${PROJECT_NAME} Parameters)
add_subdirectory(Parameters)

set(PlanetsList Earth)
set(PlanetsIncludeDirs ${PlanetsList})
list(TRANSFORM PlanetsIncludeDirs PREPEND "Planets/")
list(TRANSFORM PlanetsIncludeDirs APPEND "/include")
include_directories(${PlanetsIncludeDirs})
target_link_libraries(${PROJECT_NAME} ${PlanetsList}Persistency)
add_subdirectory(Planets)

message(PROJECT_SOURCE_DIR="${PlanetsList}")

#install(FILES "${PlanetsList}/lib${SubDir}Persistency_rdict.pcm" DESTINATION "${EXECUTABLE_OUTPUT_PATH}/build")
#install(FILES "${PlanetsList}/lib${SubDir}Persistency.rootmap" DESTINATION "${EXECUTABLE_OUTPUT_PATH}/build")
