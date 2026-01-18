if (PYTHON AND NOT DEVELOPMENT)
    file(GLOB BIN_SCRIPTS
            "archive/*.py"
            "array/*.py"
            "boundaryconditions/*.py"
            "classes/*.py"
            "classes/clusters/*.py"
            "classes/qmu/*.py"
            "classes/qmu/dakota_method/*.py"
            "consistency/*.py"
            "coordsystems/*.py"
            "dev/issmversion.py"
            "exp/*.py"
            "extrusion/*.py"
            "geometry/*.py"
            "interp/*.py"
            "inversions/*.py"
            "io/*.py"
            "materials/*.py"
            "mech/*.py"
            "mesh/*.py"
            "mesh/planet/*.py"
            "mesh/rifts/*.py"
            "miscellaneous/*.py"
            "modules/*.py"
            "netcdf/*.py"
            "os/*.py"
            "parameterization/*.py"
            "partition/*.py"
            "plot/*.py"
            "plot/colormaps/*.py"
            "qmu/*.py"
            "qmu/setupdesign/*.py"
            "shp/*.py"
            "solve/*.py"
            "solvers/*.py"
    )
    #    message(STATUS "Copying Python scripts")
    #    file(COPY ${BIN_SCRIPTS} DESTINATION ${CMAKE_RUNTIME_OUTPUT_DIRECTORY})
    message(STATUS "Linking Python scripts")
    foreach (ORIGINAL IN ITEMS ${BIN_SCRIPTS})
        get_filename_component(LINK "${ORIGINAL}" NAME)
        file(CREATE_LINK "${ORIGINAL}" "${CMAKE_RUNTIME_OUTPUT_DIRECTORY}/${LINK}")
    endforeach ()
endif ()
