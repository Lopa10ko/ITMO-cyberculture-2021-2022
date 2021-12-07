cmake_minimum_required(VERSION 3.20)
project(C_LAB2 LANGUAGES C CXX)

set(CMAKE_C_STANDARD 11)

add_subdirectory(lib/googletest-main)
include_directories(lib/googletest-main/googletest/include)
include_directories(lib/googletest-main/googlemock/include)


add_executable(C_LAB2
        Tests/ClassName.h Tests/test.cpp main.cpp)
target_link_libraries(C_LAB2 gtest gtest_main)
