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

ROOT_GENERATE_DICTIONARY(Vector3DDict Vector3D.hh Planets.hh MODULE OrbitSim LINKDEF LinkDef.h)
target_include_directories(Vector3DDict PUBLIC "include/")
add_library(myLib SHARED src/Vector3D.cc src/Planets.cc)
target_link_libraries(${PROJECT_NAME} myLib)


include_directories("Parameters/include")
target_link_libraries(${PROJECT_NAME} Parameters)
add_subdirectory(Parameters)

set(PlanetsList Earth Mars)
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

ADD_CUSTOM_TARGET(link_target ALL
                  COMMAND ${CMAKE_COMMAND} -E create_symlink "${CMAKE_BINARY_DIR}Planets/Earth/libEarthPersistency_rdict.pcm" "${CMAKE_CURRENT_BINARY_DIR}/libEarthPersistency_rdict.pcm")

ADD_CUSTOM_TARGET(link_target1 ALL
                  COMMAND ${CMAKE_COMMAND} -E create_symlink "${CMAKE_BINARY_DIR}Planets/Earth/libEarthPersistency.rootmap" "${CMAKE_CURRENT_BINARY_DIR}/libEarthPersistency.rootmap")

ADD_CUSTOM_TARGET(link_target2 ALL
                  COMMAND ${CMAKE_COMMAND} -E create_symlink "${CMAKE_BINARY_DIR}Planets/Mars/libMarsPersistency_rdict.pcm" "${CMAKE_CURRENT_BINARY_DIR}/libMarsPersistency_rdict.pcm")

ADD_CUSTOM_TARGET(link_target3 ALL
                  COMMAND ${CMAKE_COMMAND} -E create_symlink "${CMAKE_BINARY_DIR}Planets/Mars/libMarsPersistency.rootmap" "${CMAKE_CURRENT_BINARY_DIR}/libMarsPersistency.rootmap")                 
#install(FILES "${PlanetsList}/lib${SubDir}Persistency_rdict.pcm" DESTINATION "${EXECUTABLE_OUTPUT_PATH}/build")
#install(FILES "${PlanetsList}/lib${SubDir}Persistency.rootmap" DESTINATION "${EXECUTABLE_OUTPUT_PATH}/build")
