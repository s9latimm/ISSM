message(STATUS "Building Python bindings")

add_compile_definitions(_HAVE_PYTHON_)
add_compile_definitions(_PYTHON_MAJOR_=3)
add_compile_definitions(_HAVE_PYTHON_MODULES_)
add_compile_definitions(ISSM_PREFIX="${CMAKE_INSTALL_PREFIX}")

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

add_library(IssmConfig_python SHARED
        ${IO_SOURCES}
        ../IssmConfig/IssmConfig.cpp
)
target_link_libraries(IssmConfig_python ${PYTHON_LIBRARIES} Python::NumPy)

if (NOT MSYS2)
    add_library(libISSMApi_python SHARED
            ${IO_SOURCES}
            io/ApiPrintf.cpp
    )
    target_link_libraries(libISSMApi_python ${PYTHON_LIBRARIES} Python::NumPy)
endif ()

if (CHACO)
    add_library(Chaco_python SHARED
            ${IO_SOURCES}
            ../Chaco/Chaco.cpp
    )
    target_link_libraries(Chaco_python ${PYTHON_LIBRARIES} Python::NumPy chaco)
endif ()

if (TRIANGLE)
    add_library(Triangle_python SHARED
            ${IO_SOURCES}
            ../Triangle/Triangle.cpp
    )
    target_link_libraries(Triangle_python ${PYTHON_LIBRARIES} Python::NumPy triangle)
endif ()

add_library(BamgConvertMesh_python SHARED
        ${IO_SOURCES}
        ../BamgConvertMesh/BamgConvertMesh.cpp
)
target_link_libraries(BamgConvertMesh_python ${PYTHON_LIBRARIES} Python::NumPy)

add_library(BamgMesher_python SHARED
        ${IO_SOURCES}
        ../BamgMesher/BamgMesher.cpp
)
target_link_libraries(BamgMesher_python ${PYTHON_LIBRARIES} Python::NumPy)

add_library(BamgTriangulate_python SHARED
        ${IO_SOURCES}
        ../BamgTriangulate/BamgTriangulate.cpp
)
target_link_libraries(BamgTriangulate_python ${PYTHON_LIBRARIES} Python::NumPy)

add_library(ContourToMesh_python SHARED
        ${IO_SOURCES}
        ../ContourToMesh/ContourToMesh.cpp
)
target_link_libraries(ContourToMesh_python ${PYTHON_LIBRARIES} Python::NumPy)

add_library(ContourToNodes_python SHARED
        ${IO_SOURCES}
        ../ContourToNodes/ContourToNodes.cpp
)
target_link_libraries(ContourToNodes_python ${PYTHON_LIBRARIES} Python::NumPy)

add_library(ElementConnectivity_python SHARED
        ${IO_SOURCES}
        ../ElementConnectivity/ElementConnectivity.cpp
)
target_link_libraries(ElementConnectivity_python ${PYTHON_LIBRARIES} Python::NumPy)

add_library(ExpToLevelSet_python SHARED
        ${IO_SOURCES}
        ../ExpToLevelSet/ExpToLevelSet.cpp
)
target_link_libraries(ExpToLevelSet_python ${PYTHON_LIBRARIES} Python::NumPy)

add_library(InterpFromGridToMesh_python SHARED
        ${IO_SOURCES}
        ../InterpFromGridToMesh/InterpFromGridToMesh.cpp
)
target_link_libraries(InterpFromGridToMesh_python ${PYTHON_LIBRARIES} Python::NumPy)

add_library(InterpFromMesh2d_python SHARED
        ${IO_SOURCES}
        ../InterpFromMesh2d/InterpFromMesh2d.cpp
)
target_link_libraries(InterpFromMesh2d_python ${PYTHON_LIBRARIES} Python::NumPy)

add_library(InterpFromMeshToGrid_python SHARED
        ${IO_SOURCES}
        ../InterpFromMeshToGrid/InterpFromMeshToGrid.cpp
)
target_link_libraries(InterpFromMeshToGrid_python ${PYTHON_LIBRARIES} Python::NumPy)

add_library(InterpFromMeshToMesh2d_python SHARED
        ${IO_SOURCES}
        ../InterpFromMeshToMesh2d/InterpFromMeshToMesh2d.cpp
)
target_link_libraries(InterpFromMeshToMesh2d_python ${PYTHON_LIBRARIES} Python::NumPy)

add_library(InterpFromMeshToMesh3d_python SHARED
        ${IO_SOURCES}
        ../InterpFromMeshToMesh3d/InterpFromMeshToMesh3d.cpp
)
target_link_libraries(InterpFromMeshToMesh3d_python ${PYTHON_LIBRARIES} Python::NumPy)

add_library(MeshPartition_python SHARED
        ${IO_SOURCES}
        ../MeshPartition/MeshPartition.cpp
)
target_link_libraries(MeshPartition_python ${PYTHON_LIBRARIES} Python::NumPy)

add_library(MeshProfileIntersection_python SHARED
        ${IO_SOURCES}
        ../MeshProfileIntersection/MeshProfileIntersection.cpp
)
target_link_libraries(MeshProfileIntersection_python ${PYTHON_LIBRARIES} Python::NumPy)

add_library(NodeConnectivity_python SHARED
        ${IO_SOURCES}
        ../NodeConnectivity/NodeConnectivity.cpp
)
target_link_libraries(NodeConnectivity_python ${PYTHON_LIBRARIES} Python::NumPy)

add_library(ProcessRifts_python SHARED
        ${IO_SOURCES}
        ../ProcessRifts/ProcessRifts.cpp
)
target_link_libraries(ProcessRifts_python ${PYTHON_LIBRARIES} Python::NumPy)
