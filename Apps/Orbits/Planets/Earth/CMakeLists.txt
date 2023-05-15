file(GLOB SRC "src/*.cc")
file(GLOB INC "include/*.hh")
include_directories(include)

get_filename_component(SubDir ${CMAKE_CURRENT_SOURCE_DIR} NAME)
get_filename_component(ParentDir ${CMAKE_CURRENT_SOURCE_DIR} PATH)
ROOT_GENERATE_DICTIONARY(${SubDir}Dic ${INC} MODULE ${SubDir} LINKDEF LinkDef.h)
#target_include_directories(${SubDir}DIC PUBLIC "include/")
add_library(${SubDir} ${SRC})

#ROOT_GENERATE_DICTIONARY(${SubDir}DIC ${INC} MODULE ${SubDir}Lib LINKDEF LinkDef.h)
#target_include_directories(${SubDir}DIC PUBLIC "include/")
#add_library(${SubDir}Lib SHARED ${SRC})
#target_link_libraries(${PROJECT_NAME} ${SubDir}Lib)

install(FILES lib${SubDet}Lib_rdict.pcm DESTINATION lib-$ENV{SYSTEMINSTALL})
install(FILES lib${SubDet}Lib.rootmap DESTINATION lib-$ENV{SYSTEMINSTALL})
install(TARGETS ${SubDir} DESTINATION lib-$ENV{SYSTEMINSTALL})
