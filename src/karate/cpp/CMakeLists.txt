cmake_minimum_required(VERSION 3.5)

project(main LANGUAGES CXX)

IF(NOT CMAKE_BUILD_TYPE)
  SET(CMAKE_BUILD_TYPE Release)
ENDIF()

set(CMAKE_INCLUDE_CURRENT_DIR ON)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)


find_package(Boost REQUIRED)

include_directories(
  ${PROJECT_SOURCE_DIR}
)

add_executable(main
  src/main.cpp
)

target_link_libraries(main
    ${Boost_LIBS}
)

