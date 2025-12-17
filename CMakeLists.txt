cmake_minimum_required(VERSION 3.13)

project("ISSM" CXX C Fortran)
enable_language(Fortran)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

file(MAKE_DIRECTORY "${CMAKE_BINARY_DIR}/bin")
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY "${CMAKE_CURRENT_SOURCE_DIR}/bin")
message(STATUS "Binary files will be written to: ${CMAKE_BINARY_DIR}")
message(STATUS "Runtime files will be written to: ${CMAKE_RUNTIME_OUTPUT_DIRECTORY}")

if ("${CMAKE_CXX_COMPILER_ID}" STREQUAL "Clang")
    add_compile_options(-stdlib=libstdc++)
endif ()

add_compile_definitions(_DO_NOT_LOAD_GLOBALS_)
add_compile_definitions(_USE_MATH_DEFINES)

# config
list(APPEND CMAKE_MODULE_PATH "${CMAKE_CURRENT_SOURCE_DIR}/config")
include(config)
include_directories(config)

# chaco
include_directories("${CMAKE_CURRENT_SOURCE_DIR}/externalpackages/chaco/install/include")

# m1qn3
link_directories("${CMAKE_CURRENT_SOURCE_DIR}/externalpackages/m1qn3/install")

# triangle
include_directories("${CMAKE_CURRENT_SOURCE_DIR}/externalpackages/triangle/install/include")
link_directories("${CMAKE_CURRENT_SOURCE_DIR}/externalpackages/triangle/install/lib")

# petsc
include_directories("${CMAKE_CURRENT_SOURCE_DIR}/externalpackages/petsc/install/include")
link_directories("${CMAKE_CURRENT_SOURCE_DIR}/externalpackages/petsc/install/lib")

add_subdirectory(src)
add_executable(issm.exe src/c/main/issm.cpp)

target_link_libraries(issm.exe
        issm-sources
        petsc
        mpi
        metis
        m1qn3
        ddot
        gfortran
        triangle
)
