message(STATUS "Building Python bindings")

add_compile_definitions(_HAVE_PYTHON_)
add_compile_definitions(_PYTHON_MAJOR_=3)
add_compile_definitions(_HAVE_PYTHON_MODULES_)

find_package(Python 3.7 COMPONENTS Interpreter Development.Module NumPy REQUIRED)

execute_process(
        COMMAND "${Python_EXECUTABLE}"
        -c "import numpy; print(numpy.get_include())"
        OUTPUT_VARIABLE NUMPY_INCLUDE_DIR
        OUTPUT_STRIP_TRAILING_WHITESPACE
)
message(STATUS "Found NumPy: ${NUMPY_INCLUDE_DIR}")

include_directories(io ${PYTHON_INCLUDE_DIRS} ${NUMPY_INCLUDE_DIR}/numpy)

include_directories(BEFORE ../IssmConfig)
include_directories(include)

list(APPEND IO_SOURCES
        io/CheckNumPythonArguments.cpp
        io/FetchPythonData.cpp
        io/WritePythonData.cpp
)

add_library(libISSMPython STATIC
        ${IO_SOURCES}
)
target_link_libraries(libISSMPython ${PYTHON_LIBRARIES} Python::NumPy ${ISSM_EXTERNAL_LIBS} libISSMCore libISSMModules)

if (NOT MSYS2)
    add_library(libISSMApi_python STATIC
            io/ApiPrintf.cpp
    )
    target_link_libraries(libISSMApi_python libISSMPython)
endif ()

add_library(IssmConfig_python SHARED
        ../IssmConfig/IssmConfig.cpp
)
string(TIMESTAMP PACKAGE_BUILD_DATE "%a %b %d %H:%M:%S %Z %Y")
message(STATUS "Found date: ${PACKAGE_BUILD_DATE}")
target_compile_definitions(IssmConfig_python PUBLIC PACKAGE_BUILD_DATE="${PACKAGE_BUILD_DATE}")
target_link_libraries(IssmConfig_python libISSMPython)

if (CHACO)
    add_library(Chaco_python SHARED
            ../Chaco/Chaco.cpp
    )
    target_link_libraries(Chaco_python libISSMPython chaco)
endif ()

if (TRIANGLE)
    add_library(Triangle_python SHARED
            ../Triangle/Triangle.cpp
    )
    target_link_libraries(Triangle_python libISSMPython triangle)
endif ()

add_library(BamgConvertMesh_python SHARED
        ../BamgConvertMesh/BamgConvertMesh.cpp
)
target_link_libraries(BamgConvertMesh_python libISSMPython)

add_library(BamgMesher_python SHARED
        ../BamgMesher/BamgMesher.cpp
)
target_link_libraries(BamgMesher_python libISSMPython)

add_library(BamgTriangulate_python SHARED
        ../BamgTriangulate/BamgTriangulate.cpp
)
target_link_libraries(BamgTriangulate_python libISSMPython)

add_library(ContourToMesh_python SHARED
        ../ContourToMesh/ContourToMesh.cpp
)
target_link_libraries(ContourToMesh_python libISSMPython)

add_library(ContourToNodes_python SHARED
        ../ContourToNodes/ContourToNodes.cpp
)
target_link_libraries(ContourToNodes_python libISSMPython)

add_library(ElementConnectivity_python SHARED
        ../ElementConnectivity/ElementConnectivity.cpp
)
target_link_libraries(ElementConnectivity_python libISSMPython)

add_library(ExpToLevelSet_python SHARED
        ../ExpToLevelSet/ExpToLevelSet.cpp
)
target_link_libraries(ExpToLevelSet_python libISSMPython)

add_library(InterpFromGridToMesh_python SHARED
        ../InterpFromGridToMesh/InterpFromGridToMesh.cpp
)
target_link_libraries(InterpFromGridToMesh_python libISSMPython)

add_library(InterpFromMesh2d_python SHARED
        ../InterpFromMesh2d/InterpFromMesh2d.cpp
)
target_link_libraries(InterpFromMesh2d_python libISSMPython)

add_library(InterpFromMeshToGrid_python SHARED
        ../InterpFromMeshToGrid/InterpFromMeshToGrid.cpp
)
target_link_libraries(InterpFromMeshToGrid_python libISSMPython)

add_library(InterpFromMeshToMesh2d_python SHARED
        ../InterpFromMeshToMesh2d/InterpFromMeshToMesh2d.cpp
)
target_link_libraries(InterpFromMeshToMesh2d_python libISSMPython)

add_library(InterpFromMeshToMesh3d_python SHARED
        ../InterpFromMeshToMesh3d/InterpFromMeshToMesh3d.cpp
)
target_link_libraries(InterpFromMeshToMesh3d_python libISSMPython)

add_library(MeshPartition_python SHARED
        ../MeshPartition/MeshPartition.cpp
)
target_link_libraries(MeshPartition_python libISSMPython)

add_library(MeshProfileIntersection_python SHARED
        ../MeshProfileIntersection/MeshProfileIntersection.cpp
)
target_link_libraries(MeshProfileIntersection_python libISSMPython)

add_library(NodeConnectivity_python SHARED
        ../NodeConnectivity/NodeConnectivity.cpp
)
target_link_libraries(NodeConnectivity_python libISSMPython)

add_library(ProcessRifts_python SHARED
        ../ProcessRifts/ProcessRifts.cpp
)
target_link_libraries(ProcessRifts_python libISSMPython)
