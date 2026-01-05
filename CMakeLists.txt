cmake_minimum_required(VERSION 3.13)

project("ISSM" CXX C Fortran)
enable_language(Fortran)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)
set(CMAKE_EXPORT_COMPILE_COMMANDS YES)

file(MAKE_DIRECTORY "${CMAKE_BINARY_DIR}/bin")
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY "${CMAKE_CURRENT_SOURCE_DIR}/bin")

set(CMAKE_STATIC_LIBRARY_PREFIX "")
set(CMAKE_SHARED_LIBRARY_PREFIX "")
file(MAKE_DIRECTORY "${CMAKE_BINARY_DIR}/lib")
set(CMAKE_LIBRARY_OUTPUT_DIRECTORY "${CMAKE_CURRENT_SOURCE_DIR}/lib")

message(STATUS "Binary files will be written to: ${CMAKE_BINARY_DIR}")
message(STATUS "Library files will be written to: ${CMAKE_LIBRARY_OUTPUT_DIRECTORY}")
message(STATUS "Runtime files will be written to: ${CMAKE_RUNTIME_OUTPUT_DIRECTORY}")

if ("${CMAKE_CXX_COMPILER_ID}" STREQUAL "Clang")
    add_compile_options($<$<OR:$<COMPILE_LANGUAGE:C>,$<COMPILE_LANGUAGE:CXX>>:-fcolor-diagnostics>)
    add_compile_options($<$<OR:$<COMPILE_LANGUAGE:C>,$<COMPILE_LANGUAGE:CXX>>:-stdlib=libstdc++>)
elseif ("${CMAKE_CXX_COMPILER_ID}" STREQUAL "GNU")
    add_compile_options($<$<OR:$<COMPILE_LANGUAGE:C>,$<COMPILE_LANGUAGE:CXX>>:-fdiagnostics-color=always>)
endif ()

add_compile_definitions(_DO_NOT_LOAD_GLOBALS_)
add_compile_definitions(_USE_MATH_DEFINES)

set(WRAPPERS true)
set(PYTHON true)

list(APPEND CMAKE_MODULE_PATH "${CMAKE_CURRENT_SOURCE_DIR}/config")
include(config)
include_directories(config)

if (CHACO)
    include_directories("${CMAKE_CURRENT_SOURCE_DIR}/externalpackages/chaco/install/include")
    link_directories("${CMAKE_CURRENT_SOURCE_DIR}/externalpackages/chaco/install/lib")
    list(APPEND ISSM_EXTERNAL_LIBS chaco)
    add_compile_definitions(_HAVE_CHACO_)
endif ()

if (M1QN3)
    link_directories("${CMAKE_CURRENT_SOURCE_DIR}/externalpackages/m1qn3/install")
    list(APPEND ISSM_EXTERNAL_LIBS m1qn3 ddot)
    add_compile_definitions(_HAVE_M1QN3_)
endif ()

if (TRIANGLE)
    include_directories("${CMAKE_CURRENT_SOURCE_DIR}/externalpackages/triangle/install/include")
    link_directories("${CMAKE_CURRENT_SOURCE_DIR}/externalpackages/triangle/install/lib")
    list(APPEND ISSM_EXTERNAL_LIBS triangle)
    add_compile_definitions(_HAVE_TRIANGLE_)
endif ()

if (PETSC)
    include_directories("${CMAKE_CURRENT_SOURCE_DIR}/externalpackages/petsc/install/include")
    link_directories("${CMAKE_CURRENT_SOURCE_DIR}/externalpackages/petsc/install/lib")
    list(APPEND ISSM_EXTERNAL_LIBS petsc mpi metis)
    add_compile_definitions(_HAVE_PETSC_)
    add_compile_definitions(HAVE_MPI)
    add_compile_definitions(_HAVE_METIS_)
endif ()

add_subdirectory(src)
add_executable(issm.exe src/c/main/issm.cpp)

target_link_libraries(issm.exe issm-sources m gfortran ${ISSM_EXTERNAL_LIBS})

if ("${CMAKE_CXX_COMPILER_ID}" STREQUAL "Clang")
    set_property(TARGET issm.exe PROPERTY LINKER_TYPE LLD)
endif ()
