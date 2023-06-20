cmake_minimum_required(VERSION 3.20)

project(CPPSQL)

set(MAIN_FILE main.cc)

add_executable(CPPSQL ${MAIN_FILE} )
target_link_libraries(CPPSQL LINK_PUBLIC sqlite3)
