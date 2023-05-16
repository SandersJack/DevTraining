include_directories(include)

file(GLOB SRC "src/*.cc")
file(GLOB INC "include/*.hh")


get_filename_component(SubDir ${CMAKE_CURRENT_SOURCE_DIR} NAME)
get_filename_component(ParentDir ${CMAKE_CURRENT_SOURCE_DIR} PATH)

ROOT_GENERATE_DICTIONARY(${SubDir}PersistencyDICT ${INC} OPTIONS -inlineInputHeader -Iinclude MODULE ${SubDir}Persistency LINKDEF ${SubDir}LinkDef.h)
add_library(${SubDir}ObjPersistencyLib OBJECT ${SRC} ${SubDir}PersistencyDICT.cxx)
set_property(TARGET ${${SubDir}ObjPersistencyLib} PROPERTY POSITION_INDEPENDENT_CODE True)

#Then the real libraries 
add_library(${SubDir}Persistency SHARED $<TARGET_OBJECTS:${SubDir}ObjPersistencyLib>)


install(FILES ${CMAKE_CURRENT_BINARY_DIR}/lib${SubDir}Persistency_rdict.pcm DESTINATION lib-$ENV{SYSTEMINSTALL}/Persistency)
install(FILES ${CMAKE_CURRENT_BINARY_DIR}/lib${SubDir}Persistency.rootmap DESTINATION lib-$ENV{SYSTEMINSTALL}/Persistency)
install(TARGETS ${SubDir}Persistency DESTINATION lib-$ENV{SYSTEMINSTALL}/Persistency)
