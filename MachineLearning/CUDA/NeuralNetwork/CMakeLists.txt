cmake_minimum_required(VERSION 3.8 FATAL_ERROR)
project(Neural_CUDA LANGUAGES CXX CUDA)
enable_language(CUDA)

set(CMAKE_BINARY_DIR "${CMAKE_CURRENT_SOURCE_DIR}/build/")
set(EXECUTABLE_OUTPUT_PATH "${CMAKE_BINARY_DIR}")
set(LIBRARY_OUTPUT_PATH "${CMAKE_BINARY_DIR}")

file(GLOB SRC
     "src/*.cu")

set(MAIN_FILE Main.cu)
include_directories(include)

add_executable(Neural ${MAIN_FILE} ${SRC})

set_target_properties(Neural PROPERTIES CUDA_ARCHITECTURES "72")