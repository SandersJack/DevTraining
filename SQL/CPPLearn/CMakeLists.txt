cmake_minimum_required(VERSION 3.20)

project(CPPSQL)

file(GLOB SRC
     "src/*.cc")

set(MAIN_FILE main.cc)
include_directories(include)

add_executable(CPPSQL ${MAIN_FILE} ${SRC})
target_link_libraries(CPPSQL LINK_PUBLIC sqlite3)
