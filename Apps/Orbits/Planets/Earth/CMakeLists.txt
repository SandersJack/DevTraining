file(GLOB SRC "src/*.cc")
file(GLOB INC "include/*.hh")
include_directories(include)

get_filename_component(SubDir ${CMAKE_CURRENT_SOURCE_DIR} NAME)
get_filename_component(ParentDir ${CMAKE_CURRENT_SOURCE_DIR} PATH)

add_library(${SubDir} ${SRC})

install(TARGETS ${SubDir} DESTINATION lib-$ENV{SYSTEMINSTALL})
