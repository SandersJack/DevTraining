include_directories(include)

file(GLOB SRC "src/*.cc")
file(GLOB INC "include/*.hh")

include_directories(${CMAKE_SOURCE_DIR}/include)

add_library(Parameters SHARED ${SRC})

install(TARGETS Parameters Parameters DESTINATION CMAKE_BINARY_DIR)