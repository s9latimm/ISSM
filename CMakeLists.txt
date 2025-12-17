cmake_minimum_required(VERSION 3.13)

project("ISSM" CXX C Fortran)
enable_language(Fortran)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)
set(CMAKE_EXPORT_COMPILE_COMMANDS YES)

file(MAKE_DIRECTORY "${CMAKE_BINARY_DIR}/bin")
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY "${CMAKE_CURRENT_SOURCE_DIR}/bin")
message(STATUS "Binary files will be written to: ${CMAKE_BINARY_DIR}")
message(STATUS "Runtime files will be written to: ${CMAKE_RUNTIME_OUTPUT_DIRECTORY}")

add_compile_options($<$<OR:$<COMPILE_LANG_AND_ID:C,GNU>,$<COMPILE_LANG_AND_ID:CXX,GNU>>:-fdiagnostics-color=always>)
add_compile_options($<$<OR:$<COMPILE_LANG_AND_ID:C,Clang>,$<COMPILE_LANG_AND_ID:CXX,Clang>>:-fcolor-diagnostics>)

add_compile_options($<$<OR:$<COMPILE_LANG_AND_ID:C,Clang>,$<COMPILE_LANG_AND_ID:CXX,Clang>>:-stdlib=libstdc++>)

add_compile_definitions(_DO_NOT_LOAD_GLOBALS_)
add_compile_definitions(_USE_MATH_DEFINES)

list(APPEND CMAKE_MODULE_PATH "${CMAKE_CURRENT_SOURCE_DIR}/config")
include(config)
include_directories(config)

if (CHACO)
    include_directories("${CMAKE_CURRENT_SOURCE_DIR}/externalpackages/chaco/install/include")
    link_directories("${CMAKE_CURRENT_SOURCE_DIR}/externalpackages/chaco/install/lib")
    list(APPEND ISSM_EXTERNAL_LIBS chaco)
endif ()

if (M1QN3)
    link_directories("${CMAKE_CURRENT_SOURCE_DIR}/externalpackages/m1qn3/install")
    list(APPEND ISSM_EXTERNAL_LIBS m1qn3 ddot)
endif ()

if (TRIANGLE)
    include_directories("${CMAKE_CURRENT_SOURCE_DIR}/externalpackages/triangle/install/include")
    link_directories("${CMAKE_CURRENT_SOURCE_DIR}/externalpackages/triangle/install/lib")
    list(APPEND ISSM_EXTERNAL_LIBS triangle)
endif ()

if (PETSC)
    include_directories("${CMAKE_CURRENT_SOURCE_DIR}/externalpackages/petsc/install/include")
    link_directories("${CMAKE_CURRENT_SOURCE_DIR}/externalpackages/petsc/install/lib")
    list(APPEND ISSM_EXTERNAL_LIBS petsc mpi metis)
endif ()

add_subdirectory(src)
add_executable(issm.exe src/c/main/issm.cpp)

target_link_libraries(issm.exe issm-sources m gfortran ${ISSM_EXTERNAL_LIBS})
