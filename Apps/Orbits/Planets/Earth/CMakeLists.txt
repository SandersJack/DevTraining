include_directories(include)

file(GLOB SRC "src/*.cc")
file(GLOB INC "include/*.hh")


get_filename_component(SubDir ${CMAKE_CURRENT_SOURCE_DIR} NAME)
get_filename_component(ParentDir ${CMAKE_CURRENT_SOURCE_DIR} PATH)

ROOT_GENERATE_DICTIONARY(${SubDir}PersistencyDICT ${INC} OPTIONS -inlineInputHeader -Iinclude MODULE ${SubDir}Persistency LINKDEF ${SubDir}LinkDef.h)
#add_library(${SubDir}ObjPersistencyLib OBJECT ${SRC} ${SubDir}PersistencyDICT.cxx)
#set_property(TARGET ${${SubDir}ObjPersistencyLib} PROPERTY POSITION_INDEPENDENT_CODE True)

#Then the real libraries 
#add_library(${SubDir}Persistency SHARED $<TARGET_OBJECTS:${SubDir}ObjPersistencyLib>)
add_library(${SubDir}Persistency SHARED ${SRC} ${SubDir}PersistencyDICT.cxx)

message(PROJECT_SOURCE_DIR="${CMAKE_BINARY_DIR}")
message(DIR="${CMAKE_CURRENT_BINARY_DIR}/lib${SubDir}Persistency_rdict.pcm")

install(FILES "${CMAKE_CURRENT_BINARY_DIR}/lib${SubDir}Persistency_rdict.pcm" DESTINATION "${CMAKE_BINARY_DIR}")
install(FILES "${CMAKE_CURRENT_BINARY_DIR}/lib${SubDir}Persistency.rootmap" DESTINATION "${CMAKE_BINARY_DIR}")

install(TARGETS ${SubDir}Persistency DESTINATION EXECUTABLE_OUTPUT_PATH)