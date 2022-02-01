# cmake_minimum_required(VERSION <specify CMake version here>)
project(data_mining)

set(CMAKE_CXX_STANDARD 11)

#include_directories(Project2)
#include_directories(Project3)
#file(COPY ${CMAKE_CURRENT_SOURCE_DIR}/config/trace.config
#        DESTINATION ${CMAKE_CURRENT_BINARY_DIR})


add_executable(data_mining
        adm.cpp)

