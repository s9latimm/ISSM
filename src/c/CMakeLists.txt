if (BAMG)
    list(APPEND ISSM_SOURCES
            bamg/BamgGeom.cpp
            bamg/BamgMesh.cpp
            bamg/BamgOpts.cpp
            bamg/CrackedEdge.cpp
            bamg/Curve.cpp
            bamg/Edge.cpp
            bamg/GeomEdge.cpp
            bamg/GeomSubDomain.cpp
            bamg/GeomVertex.cpp
            bamg/Geometry.cpp
            bamg/ListofIntersectionTriangles.cpp
            bamg/EigenMetric.cpp
            bamg/Metric.cpp
            bamg/BamgQuadtree.cpp
            bamg/SetOfE4.cpp
            bamg/SubDomain.cpp
            bamg/AdjacentTriangle.cpp
            bamg/Triangle.cpp
            bamg/BamgVertex.cpp
            bamg/VertexOnEdge.cpp
            bamg/VertexOnGeom.cpp
            bamg/VertexOnVertex.cpp
            bamg/Mesh.cpp
            shared/Bamg/BigPrimeNumber.cpp
            modules/Bamgx/Bamgx.cpp
            modules/BamgConvertMeshx/BamgConvertMeshx.cpp
            modules/BamgTriangulatex/BamgTriangulatex.cpp
    )
endif ()
# Do not include AmrBamg with AD
if (ADOLC)
    list(APPEND ISSM_SOURCES
            shared/Numerics/isnan.cpp
            shared/MemOps/MemOps.cpp
    )
else ()
    if (CODIPACK)
        list(APPEND ISSM_SOURCES
                shared/Numerics/isnan.cpp
        )
    else ()
        list(APPEND ISSM_SOURCES
                classes/AmrBamg.cpp
        )
    endif ()
endif ()
#}}}
# Core sources {{{
list(APPEND ISSM_SOURCES
        datastructures/DataSet.cpp
        classes/gauss/GaussSeg.cpp
        classes/gauss/GaussTria.cpp
        classes/gauss/GaussTetra.cpp
        classes/gauss/GaussPenta.cpp
        classes/IoModel.cpp
        classes/FemModel.cpp
        classes/Loads/Friction.cpp
        classes/Constraints/SpcTransient.cpp
        classes/DependentObject.cpp
        classes/Contours.cpp
        classes/Vertices.cpp
        classes/Nodes.cpp
        classes/Numberedcostfunction.cpp
        classes/Misfit.cpp
        classes/Cfsurfacesquare.cpp
        classes/Cfsurfacesquaretransient.cpp
        classes/Cfdragcoeffabsgrad.cpp
        classes/Cfdragcoeffabsgradtransient.cpp
        classes/Cfrheologybbarabsgrad.cpp
        classes/Cfrheologybbarabsgradtransient.cpp
        classes/Cfsurfacelogvel.cpp
        classes/Cflevelsetmisfit.cpp
        classes/Regionaloutput.cpp
        classes/Nodalvalue.cpp
        classes/Node.cpp
        classes/Vertex.cpp
        classes/Hook.cpp
        classes/Radar.cpp
        classes/BarystaticContributions.cpp
        classes/ExternalResults/Results.cpp
        classes/Elements/Element.cpp
        classes/Elements/Elements.cpp
        classes/Elements/ElementHook.cpp
        classes/Elements/Seg.cpp
        classes/Elements/SegRef.cpp
        classes/Elements/Tria.cpp
        classes/Elements/TriaRef.cpp
        classes/Elements/Tetra.cpp
        classes/Elements/TetraRef.cpp
        classes/Elements/Penta.cpp
        classes/Elements/PentaRef.cpp
        classes/Materials/Materials.cpp
        classes/Materials/Matice.cpp
        classes/Materials/Matlitho.cpp
        classes/Materials/Matestar.cpp
        classes/Constraints/Constraints.cpp
        classes/Constraints/SpcStatic.cpp
        classes/Constraints/SpcDynamic.cpp
        classes/Loads/Channel.cpp
        classes/Loads/Loads.cpp
        classes/Loads/Penpair.cpp
        classes/Loads/Pengrid.cpp
        classes/Loads/Moulin.cpp
        classes/Loads/Numericalflux.cpp
        classes/Loads/Neumannflux.cpp
        classes/matrix/ElementMatrix.cpp
        classes/matrix/ElementVector.cpp
        classes/Params/Parameters.cpp
        classes/Params/BoolParam.cpp
        classes/Params/ControlParam.cpp
        classes/Params/IntParam.cpp
        classes/Params/IntVecParam.cpp
        classes/Params/IntMatParam.cpp
        classes/Params/DoubleParam.cpp
        classes/Params/FileParam.cpp
        classes/Params/StringArrayParam.cpp
        classes/Params/DoubleMatParam.cpp
        classes/Params/DoubleTransientMatParam.cpp
        classes/Params/DoubleMatArrayParam.cpp
        classes/Params/DoubleVecParam.cpp
        classes/Params/StringParam.cpp
        classes/Params/MatrixParam.cpp
        classes/Params/VectorParam.cpp
        classes/Params/TransientParam.cpp
        classes/Params/TransientArrayParam.cpp
        classes/Params/TransientGriddedFieldParam.cpp
        classes/Params/DataSetParam.cpp
        classes/Profiler.cpp
        shared/Matrix/MatrixUtils.cpp
        shared/io/Disk/pfopen.cpp
        shared/io/Disk/pfclose.cpp
        shared/io/Disk/WriteLockFile.cpp
        shared/io/Print/PrintfFunction.cpp
        shared/io/Comm/IssmComm.cpp
        shared/io/Marshalling/IoCodeConversions.cpp
        shared/io/Marshalling/Marshalling.cpp
        shared/LatLong/Ll2xyx.cpp
        shared/LatLong/Xy2llx.cpp
        shared/FSanalyticals/fsanalyticals.cpp
        shared/Enum/EnumToStringx.cpp
        shared/Enum/StringToEnumx.cpp
        shared/Numerics/Verbosity.cpp
        shared/Numerics/GaussPoints.cpp
        shared/Numerics/cross.cpp
        shared/Numerics/cubic.cpp
        shared/Numerics/NewtonSolveDnorm.cpp
        shared/Numerics/ODE1.cpp
        shared/Numerics/extrema.cpp
        shared/Numerics/legendre.cpp
        shared/Numerics/XZvectorsToCoordinateSystem.cpp
        shared/Numerics/Normals.cpp
        shared/Numerics/Interpolation.cpp
        shared/Exceptions/Exceptions.cpp
        shared/Sorting/binary_search.cpp
        shared/Elements/Cuffey.cpp
        shared/Elements/BuddJacka.cpp
        shared/Elements/CuffeyTemperate.cpp
        shared/Elements/StressIntensityIntegralWeight.cpp
        shared/Elements/Paterson.cpp
        shared/Elements/Arrhenius.cpp
        shared/Elements/NyeCO2.cpp
        shared/Elements/NyeH2O.cpp
        shared/Elements/LliboutryDuval.cpp
        shared/Elements/PrintArrays.cpp
        shared/Elements/PddSurfaceMassBalance.cpp
        shared/Elements/PddSurfaceMassBalanceSicopolis.cpp
        shared/Elements/ComputeDelta18oTemperaturePrecipitation.cpp
        shared/Elements/ComputeMungsmTemperaturePrecipitation.cpp
        shared/Elements/ComputeD18OTemperaturePrecipitationFromPD.cpp
        shared/Elements/DrainageFunctionWaterfraction.cpp
        shared/Elements/EstarComponents.cpp
        shared/Random/random.cpp
        shared/Random/randomgenerator.cpp
        shared/String/DescriptorIndex.cpp
        toolkits/issm/IssmToolkitUtils.cpp
        toolkits/issm/IssmSolver.cpp
        toolkits/mpi/issmmpi.cpp
        toolkits/mpi/commops/DetermineLocalSize.cpp
        toolkits/mpi/commops/DetermineGlobalSize.cpp
        toolkits/mpi/commops/DetermineRowRankFromLocalSize.cpp
        toolkits/mpi/commops/GetOwnershipBoundariesFromRange.cpp
        toolkits/ToolkitOptions.cpp
        modules/MmeToInputFromIdx/MmeToInputFromIdx.cpp
        modules/MmeToInputx/MmeToInputx.cpp
        modules/ModelProcessorx/ModelProcessorx.cpp
        modules/ModelProcessorx/ElementsAndVerticesPartitioning.cpp
        modules/ModelProcessorx/EdgesPartitioning.cpp
        modules/ModelProcessorx/FacesPartitioning.cpp
        modules/ModelProcessorx/CreateParameters.cpp
        modules/ModelProcessorx/Autodiff/CreateParametersAutodiff.cpp
        modules/ModelProcessorx/CreateFaces.cpp
        modules/ModelProcessorx/CreateEdges.cpp
        modules/ModelProcessorx/CreateSingleNodeToElementConnectivity.cpp
        modules/ModelProcessorx/CreateNumberNodeToElementConnectivity.cpp
        modules/ModelProcessorx/CreateElementsVerticesAndMaterials.cpp
        modules/ModelProcessorx/CreateNodes.cpp
        modules/ParseToolkitsOptionsx/ParseToolkitsOptionsx.cpp
        modules/NodesDofx/NodesDofx.cpp
        modules/NodalValuex/NodalValuex.cpp
        modules/VertexCoordinatesx/VertexCoordinatesx.cpp
        modules/ElementCoordinatesx/ElementCoordinatesx.cpp
        modules/OutputResultsx/OutputResultsx.cpp
        modules/InputDepthAverageAtBasex/InputDepthAverageAtBasex.cpp
        modules/InputDuplicatex/InputDuplicatex.cpp
        modules/InputExtrudex/InputExtrudex.cpp
        modules/SurfaceAreax/SurfaceAreax.cpp
        modules/AllocateSystemMatricesx/AllocateSystemMatricesx.cpp
        modules/CreateJacobianMatrixx/CreateJacobianMatrixx.cpp
        modules/SystemMatricesx/SystemMatricesx.cpp
        modules/CreateNodalConstraintsx/CreateNodalConstraintsx.cpp
        modules/UpdateDynamicConstraintsx/UpdateDynamicConstraintsx.cpp
        modules/IoModelToConstraintsx/IoModelToConstraintsx.cpp
        modules/SetActiveNodesLSMx/SetActiveNodesLSMx.cpp
        modules/InputUpdateFromConstantx/InputUpdateFromConstantx.cpp
        modules/InputUpdateFromSolutionx/InputUpdateFromSolutionx.cpp
        modules/GeothermalFluxx/GeothermalFluxx.cpp
        modules/GetSolutionFromInputsx/GetSolutionFromInputsx.cpp
        modules/GetVectorFromInputsx/GetVectorFromInputsx.cpp
        modules/InputUpdateFromVectorx/InputUpdateFromVectorx.cpp
        modules/FloatingiceMeltingRatex/FloatingiceMeltingRatex.cpp
        modules/FloatingiceMeltingRatePicox/FloatingiceMeltingRatePicox.cpp
        modules/FrontalForcingsx/FrontalForcingsx.cpp
        modules/ConfigureObjectsx/ConfigureObjectsx.cpp
        modules/SpcNodesx/SpcNodesx.cpp
        modules/SurfaceMassBalancex/SurfaceMassBalancex.cpp
        modules/SurfaceMassBalancex/Gembx.cpp
        modules/Reducevectorgtofx/Reducevectorgtofx.cpp
        modules/Reduceloadx/Reduceloadx.cpp
        modules/ConstraintsStatex/ConstraintsStatex.cpp
        modules/ResetConstraintsx/ResetConstraintsx.cpp
        modules/ResetFSBasalBoundaryConditionx/ResetFSBasalBoundaryConditionx.cpp
        modules/Solverx/Solverx.cpp
        modules/StochasticForcingx/StochasticForcingx.cpp
        modules/Mergesolutionfromftogx/Mergesolutionfromftogx.cpp
        modules/UpdateMmesx/UpdateMmesx.cpp
        cores/ProcessArguments.cpp
        cores/ResetBoundaryConditions.cpp
        cores/WrapperCorePointerFromSolutionEnum.cpp
        cores/WrapperPreCorePointerFromSolutionEnum.cpp
        cores/CorePointerFromSolutionEnum.cpp
        cores/ad_core.cpp
        main/EnvironmentInit.cpp
        main/EnvironmentFinalize.cpp
        analyses/EnumToAnalysis.cpp
        solutionsequences/solutionsequence_la.cpp
        solutionsequences/solutionsequence_la_theta.cpp
        solutionsequences/solutionsequence_linear.cpp
        solutionsequences/solutionsequence_nonlinear.cpp
        solutionsequences/solutionsequence_newton.cpp
        solutionsequences/solutionsequence_fct.cpp
        solutionsequences/solutionsequence_schurcg.cpp
        solutionsequences/solutionsequence_sampling.cpp
        solutionsequences/convergence.cpp
        classes/Options/Options.cpp
        classes/RiftStruct.cpp
        modules/ModelProcessorx/Transient/UpdateElementsTransient.cpp
        modules/ModelProcessorx/Transient/UpdateParametersTransient.cpp
        cores/transient_core.cpp
        cores/steadystate_core.cpp
        cores/masstransport_core.cpp
        cores/mmemasstransport_core.cpp
        cores/oceantransport_core.cpp
        cores/depthaverage_core.cpp
        cores/extrudefrombase_core.cpp
        cores/extrudefromtop_core.cpp
        cores/thermal_core.cpp
        cores/smb_core.cpp
        cores/bmb_core.cpp
        cores/debris_core.cpp
        solutionsequences/solutionsequence_thermal_nonlinear.cpp
        modules/ControlInputSetGradientx/ControlInputSetGradientx.cpp
        modules/GetVectorFromControlInputsx/GetVectorFromControlInputsx.cpp
        modules/SetControlInputsFromVectorx/SetControlInputsFromVectorx.cpp
        modules/ModelProcessorx/Control/CreateParametersControl.cpp
        modules/ModelProcessorx/Control/UpdateElementsAndMaterialsControl.cpp
        modules/SurfaceAbsVelMisfitx/SurfaceAbsVelMisfitx.cpp
        modules/SurfaceRelVelMisfitx/SurfaceRelVelMisfitx.cpp
        modules/SurfaceLogVelMisfitx/SurfaceLogVelMisfitx.cpp
        modules/SurfaceLogVxVyMisfitx/SurfaceLogVxVyMisfitx.cpp
        modules/SurfaceAverageVelMisfitx/SurfaceAverageVelMisfitx.cpp
        modules/ThicknessAbsMisfitx/ThicknessAbsMisfitx.cpp
        modules/Gradjx/Gradjx.cpp
        modules/DragCoefficientAbsGradientx/DragCoefficientAbsGradientx.cpp
        modules/ThicknessAlongGradientx/ThicknessAlongGradientx.cpp
        modules/ThicknessAcrossGradientx/ThicknessAcrossGradientx.cpp
        modules/RheologyBbarAbsGradientx/RheologyBbarAbsGradientx.cpp
        modules/RheologyBAbsGradientx/RheologyBAbsGradientx.cpp
        shared/Numerics/BrentSearch.cpp
        cores/control_core.cpp
        cores/controltao_core.cpp
        cores/controlm1qn3_core.cpp
        cores/controladm1qn3_core.cpp
        cores/controlvalidation_core.cpp
        cores/adjointstressbalance_core.cpp
        cores/adjointbalancethickness_core.cpp
        cores/adjointbalancethickness2_core.cpp
        cores/AdjointCorePointerFromSolutionEnum.cpp
        solutionsequences/solutionsequence_adjoint_linear.cpp
        cores/hydrology_core.cpp
        solutionsequences/solutionsequence_hydro_nonlinear.cpp
        solutionsequences/solutionsequence_shakti_nonlinear.cpp
        solutionsequences/solutionsequence_glads_nonlinear.cpp
        cores/stressbalance_core.cpp
        solutionsequences/solutionsequence_stokescoupling_nonlinear.cpp
        cores/balancethickness_core.cpp
        cores/balancethickness2_core.cpp
        cores/balancevelocity_core.cpp
        cores/dummy_core.cpp
        cores/surfaceslope_core.cpp
        cores/bedslope_core.cpp
        cores/damage_core.cpp
        cores/levelsetfunctionslope_core.cpp
        cores/movingfront_core.cpp
        cores/groundingline_core.cpp
        modules/GroundinglineMigrationx/GroundinglineMigrationx.cpp
        classes/Loads/Riftfront.cpp
        modules/ConstraintsStatex/RiftConstraintsState.cpp
        modules/ModelProcessorx/CreateOutputDefinitions.cpp
        modules/OutputDefinitionsResponsex/OutputDefinitionsResponsex.cpp
        modules/InterpFromMeshToMesh2dx/InterpFromMeshToMesh2dx.cpp
        classes/Inputs/Inputs.cpp
        classes/Inputs/BoolInput.cpp
        classes/Inputs/DoubleInput.cpp
        classes/Inputs/IntInput.cpp
        classes/Inputs/ElementInput.cpp
        classes/Inputs/SegInput.cpp
        classes/Inputs/TriaInput.cpp
        classes/Inputs/PentaInput.cpp
        classes/Inputs/DatasetInput.cpp
        classes/Inputs/ControlInput.cpp
        classes/Inputs/TransientInput.cpp
        classes/Inputs/TransientFileInput.cpp
        classes/Inputs/ArrayInput.cpp
        classes/Inputs/IntArrayInput.cpp
)
#}}}
# ADJOINTMPI/MeDiPack sources {{{
if (ADJOINTMPI)
    list(APPEND ISSM_SOURCES
            toolkits/codipack/ampi_interface.cpp
    )
endif ()
if (MEDIPACK)
    list(APPEND ISSM_SOURCES
            toolkits/codipack/ampi_interface.cpp
    )
endif ()
if (CODIPACK)
    list(APPEND ISSM_SOURCES
            toolkits/codipack/CoDiPackGlobal.cpp
    )
endif ()
#}}}
# DAKOTA sources {{{
if (DAKOTA)
    list(APPEND ISSM_SOURCES
            classes/Dakota/IssmDirectApplicInterface.h
            classes/Dakota/IssmParallelDirectApplicInterface.cpp
            modules/InputUpdateFromDakotax/InputUpdateFromDakotax.cpp
            modules/InputUpdateFromVectorDakotax/InputUpdateFromVectorDakotax.cpp
            modules/InputUpdateFromMatrixDakotax/InputUpdateFromMatrixDakotax.cpp
            modules/AverageOntoPartitionx/AverageOntoPartitionx.cpp
            modules/ModelProcessorx/Dakota/CreateParametersDakota.cpp
            modules/ModelProcessorx/Dakota/UpdateElementsAndMaterialsDakota.cpp
            cores/dakota_core.cpp
    )
    if (SYSTEM_HAS_FMEMOPEN)
        list(APPEND ISSM_SOURCES
                modules/QmuStatisticsx/QmuStatisticsx.cpp
        )
    endif ()
endif ()
#}}}
# PETSc sources {{{
if (PETSC)
    list(APPEND ISSM_SOURCES
            toolkits/petsc
            toolkits/petsc/patches
            toolkits/petsc/patches/VecToMPISerial.cpp
            toolkits/petsc/patches/MatToMPISerial.cpp
            toolkits/petsc/patches/NewVec.cpp
            toolkits/petsc/patches/PetscOptionsDetermineSolverType.cpp
            toolkits/petsc/patches/NewMat.cpp
            toolkits/petsc/patches/VecFree.cpp
            toolkits/petsc/patches/KSPFree.cpp
            toolkits/petsc/patches/MatFree.cpp
            toolkits/petsc/patches/ISSMToPetscMatrixType.cpp
            toolkits/petsc/patches/ISSMToPetscInsertMode.cpp
            toolkits/petsc/patches/ISSMToPetscNormMode.cpp
            toolkits/petsc/objects/PetscMat.cpp
            toolkits/petsc/objects/PetscVec.cpp
            toolkits/petsc/objects/PetscSolver.cpp
    )
endif ()
#}}}
# MUMPS sources {{{
if (MUMPS)
    list(APPEND ISSM_SOURCES
            toolkits/mumps/MumpsSolve.cpp
    )
endif ()
#}}}
# GSL sources {{{
if (GSL)
    list(APPEND ISSM_SOURCES
            toolkits/gsl/DenseGslSolve.cpp
    )
endif ()
#}}}
# PROJ sources {{{
if (PROJ)
    list(APPEND ISSM_SOURCES
            modules/CoordinateSystemTransformx/CoordinateSystemTransformx.cpp
    )
endif ()
#}}}
# Analyses {{{
if (ADJOINTBALANCETHICKNESS)
    list(APPEND ISSM_SOURCES
            analyses/AdjointBalancethicknessAnalysis.cpp
    )
endif ()
if (ADJOINTBALANCETHICKNESS2)
    list(APPEND ISSM_SOURCES
            analyses/AdjointBalancethickness2Analysis.cpp
    )
endif ()
if (ADJOINTHORIZ)
    list(APPEND ISSM_SOURCES
            analyses/AdjointHorizAnalysis.cpp
    )
endif ()
if (AGE)
    list(APPEND ISSM_SOURCES
            analyses/AgeAnalysis.cpp
    )
endif ()
if (BALANCETHICKNESS)
    list(APPEND ISSM_SOURCES
            analyses/BalancethicknessAnalysis.cpp
    )
endif ()
if (BALANCETHICKNESS2)
    list(APPEND ISSM_SOURCES
            analyses/Balancethickness2Analysis.cpp
    )
endif ()
if (BALANCETHICKNESSSOFT)
    list(APPEND ISSM_SOURCES
            analyses/BalancethicknessSoftAnalysis.cpp
    )
endif ()
if (BALANCEVELOCITY)
    list(APPEND ISSM_SOURCES
            analyses/BalancevelocityAnalysis.cpp
    )
endif ()
if (L2PROJECTIONBASE)
    list(APPEND ISSM_SOURCES
            analyses/L2ProjectionBaseAnalysis.cpp
    )
endif ()
if (DAMAGEEVOLUTION)
    list(APPEND ISSM_SOURCES
            analyses/DamageEvolutionAnalysis.cpp
    )
    list(APPEND ISSM_SOURCES
            modules/Damagex/Damagex.cpp
    )
endif ()
if (DEBRIS)
    list(APPEND ISSM_SOURCES
            analyses/DebrisAnalysis.cpp
    )
endif ()
if (STRESSBALANCE)
    list(APPEND ISSM_SOURCES
            analyses/StressbalanceAnalysis.cpp
    )
endif ()
if (UZAWAPRESSURE)
    list(APPEND ISSM_SOURCES
            analyses/UzawaPressureAnalysis.cpp
    )
endif ()
if (STRESSBALANCESIA)
    list(APPEND ISSM_SOURCES
            analyses/StressbalanceSIAAnalysis.cpp
    )
endif ()
if (STRESSBALANCEVERTICAL)
    list(APPEND ISSM_SOURCES
            analyses/StressbalanceVerticalAnalysis.cpp
    )
endif ()
if (ENTHALPY)
    list(APPEND ISSM_SOURCES
            analyses/EnthalpyAnalysis.cpp
    )
endif ()
if (GLHEIGHTADVECTION)
    list(APPEND ISSM_SOURCES
            analyses/GLheightadvectionAnalysis.cpp
    )
endif ()
if (HYDROLOGYSHREVE)
    list(APPEND ISSM_SOURCES
            analyses/HydrologyShreveAnalysis.cpp
    )
endif ()
if (HYDROLOGYTWS)
    list(APPEND ISSM_SOURCES
            analyses/HydrologyTwsAnalysis.cpp
    )
endif ()
if (HYDROLOGYSHAKTI)
    list(APPEND ISSM_SOURCES
            analyses/HydrologyShaktiAnalysis.cpp
    )
endif ()
if (HYDROLOGYPISM)
    list(APPEND ISSM_SOURCES
            analyses/HydrologyPismAnalysis.cpp
    )
endif ()
if (HYDROLOGYGLADS)
    list(APPEND ISSM_SOURCES
            analyses/HydrologyGlaDSAnalysis.cpp
    )
endif ()
if (HYDROLOGYDCINEFFICIENT)
    list(APPEND ISSM_SOURCES
            analyses/HydrologyDCInefficientAnalysis.cpp
    )
endif ()
if (HYDROLOGYDCEFFICIENT)
    list(APPEND ISSM_SOURCES
            analyses/HydrologyDCEfficientAnalysis.cpp
    )
endif ()
if (HYDROLOGYARMAPW)
    list(APPEND ISSM_SOURCES
            analyses/HydrologyArmapwAnalysis.cpp
    )
endif ()
if (L2PROJECTIONEPL)
    list(APPEND ISSM_SOURCES
            analyses/L2ProjectionEPLAnalysis.cpp
    )
endif ()
if (MELTING)
    list(APPEND ISSM_SOURCES
            analyses/MeltingAnalysis.cpp
    )
endif ()
if (MASSTRANSPORT)
    list(APPEND ISSM_SOURCES
            analyses/MasstransportAnalysis.cpp
            analyses/MmemasstransportAnalysis.cpp
    )
endif ()
if (OCEANTRANSPORT)
    list(APPEND ISSM_SOURCES
            analyses/OceantransportAnalysis.cpp
    )
endif ()
if (SMB)
    list(APPEND ISSM_SOURCES
            analyses/SmbAnalysis.cpp
    )
endif ()
if (FREESURFACEBASE)
    list(APPEND ISSM_SOURCES
            analyses/FreeSurfaceBaseAnalysis.cpp
    )
endif ()
if (FREESURFACETOP)
    list(APPEND ISSM_SOURCES
            analyses/FreeSurfaceTopAnalysis.cpp
    )
endif ()
if (EXTRUDEFROMBASE)
    list(APPEND ISSM_SOURCES
            analyses/ExtrudeFromBaseAnalysis.cpp
    )
endif ()
if (EXTRUDEFROMTOP)
    list(APPEND ISSM_SOURCES
            analyses/ExtrudeFromTopAnalysis.cpp
    )
endif ()
if (DEPTHAVERAGE)
    list(APPEND ISSM_SOURCES
            analyses/DepthAverageAnalysis.cpp
    )
endif ()
if (THERMAL)
    list(APPEND ISSM_SOURCES
            analyses/ThermalAnalysis.cpp
    )
endif ()
if (SMOOTH)
    list(APPEND ISSM_SOURCES
            analyses/SmoothAnalysis.cpp
    )
endif ()
if (LEVELSET)
    list(APPEND ISSM_SOURCES
            analyses/LevelsetAnalysis.cpp
    )
    list(APPEND ISSM_SOURCES
            modules/Calvingx/Calvingx.cpp
    )
    list(APPEND ISSM_SOURCES
            modules/KillIcebergsx/KillIcebergsx.cpp
    )
endif ()
if (EXTRAPOLATION)
    list(APPEND ISSM_SOURCES
            analyses/ExtrapolationAnalysis.cpp
    )
endif ()
#}}}
# Love sources (only if (have Fortran) {{{
if (LOVE)
    if (FORTRAN)
        list(APPEND ISSM_SOURCES
                cores/love_core.cpp
                analyses/LoveAnalysis.cpp
                modules/Zgesvx/Zgesvx.cpp
                modules/Zgesvx/Zgesvx.h
                modules/Zgesvx/dcabs1.f
                modules/Zgesvx/dlamch.f
                modules/Zgesvx/ieeeck.f
                modules/Zgesvx/ilaenv.f
                modules/Zgesvx/iparmq.f
                modules/Zgesvx/izamax.f
                modules/Zgesvx/lsame.f
                modules/Zgesvx/xerbla.f
                modules/Zgesvx/zgemm.f
                modules/Zgesvx/zgeru.f
                modules/Zgesvx/zgesv.f
                modules/Zgesvx/zgetf2.f
                modules/Zgesvx/zgetrf2.f
                modules/Zgesvx/zgetrf.f
                modules/Zgesvx/zgetrs.f
                modules/Zgesvx/zlaswp.f
                modules/Zgesvx/zscal.f
                modules/Zgesvx/zswap.f
                modules/Zgesvx/ztrsm.f
        )
    endif ()
endif ()
#}}}
# Esa sources {{{
if (ESA)
    list(APPEND ISSM_SOURCES
            cores/esa_core.cpp
            analyses/EsaAnalysis.cpp
    )
endif ()
#}}}
# Ocean sources {{{
if (OCEAN)
    list(APPEND ISSM_SOURCES
            modules/OceanExchangeDatax/OceanExchangeDatax.cpp
    )
endif ()
#}}}
# Sampling sources {{{
if (SAMPLING)
    list(APPEND ISSM_SOURCES
            cores/sampling_core.cpp
            analyses/SamplingAnalysis.cpp
    )
endif ()
#}}}
# SLC sources {{{
if (SEALEVELCHANGE)
    list(APPEND ISSM_SOURCES
            cores/sealevelchange_core.cpp
            analyses/SealevelchangeAnalysis.cpp
            classes/GrdLoads.cpp
            classes/SealevelGeometry.cpp
    )    # GIA Ivins physics (only if (have Fortran)
    if (FORTRAN)
        list(APPEND ISSM_SOURCES
                modules/GiaDeflectionCorex/GiaDeflectionCorex.cpp
                modules/GiaDeflectionCorex/distme.f
                modules/GiaDeflectionCorex/freed.f
                modules/GiaDeflectionCorex/ojrule.f
                modules/GiaDeflectionCorex/pwise.f
                modules/GiaDeflectionCorex/qwise.f
                modules/GiaDeflectionCorex/stot.f
                modules/GiaDeflectionCorex/what0.f)
    endif ()
endif ()
#}}}
# METIS sources {{{
if (METIS)
    list(APPEND ISSM_SOURCES
            modules/MeshPartitionx/MeshPartitionx.cpp
    )
    list(APPEND ISSM_SOURCES
            toolkits/metis/patches/METIS_PartMeshNodalPatch.cpp
    )
endif ()
#}}}
# Esmf sources {{{
if (ESMF)
    list(APPEND ISSM_SOURCES
            main/esmfbinders.cpp
    )
endif ()
#}}}
# SEMIC sources {{{
if (SEMIC)
    if (FORTRAN)
        list(APPEND ISSM_SOURCES
                modules/SurfaceMassBalancex/run_semic.f90)
        list(APPEND ISSM_SOURCES
                modules/SurfaceMassBalancex/run_semic_transient.f90)
    endif ()
endif ()
#}}}
# Wrapper sources
# Kml sources {{{
list(APPEND kml_sources
        modules/Exp2Kmlx/Exp2Kmlx.cpp
        modules/Kml2Expx/Kml2Expx.cpp
        modules/Shp2Kmlx/Shp2Kmlx.cpp
        modules/KMLFileReadx/KMLFileReadx.cpp
        modules/KMLMeshWritex/KMLMeshWritex.cpp
        modules/KMLOverlayx/KMLOverlayx.cpp
        kml/KML_Attribute.cpp
        kml/KML_Comment.cpp
        kml/KML_ColorStyle.cpp
        kml/KML_Container.cpp
        kml/KML_Document.cpp
        kml/KML_Feature.cpp
        kml/KML_File.cpp
        kml/KML_Folder.cpp
        kml/KML_Geometry.cpp
        kml/KML_GroundOverlay.cpp
        kml/KML_Icon.cpp
        kml/KML_LatLonBox.cpp
        kml/KML_LinearRing.cpp
        kml/KML_LineString.cpp
        kml/KML_LineStyle.cpp
        kml/KML_MultiGeometry.cpp
        kml/KML_Object.cpp
        kml/KML_Overlay.cpp
        kml/KML_Point.cpp
        kml/KML_Placemark.cpp
        kml/KML_Polygon.cpp
        kml/KML_PolyStyle.cpp
        kml/KML_Style.cpp
        kml/KML_StyleSelector.cpp
        kml/KML_SubStyle.cpp
        kml/KML_Unknown.cpp
        kml/KMLFileReadUtils.cpp
)
#}}}
# NEOPZ sources {{{
list(APPEND neopz_sources
        classes/AmrNeopz.cpp
)
#}}}
# Modules sources {{{
list(APPEND MODULES_SOURCES
        shared/Threads/LaunchThread.cpp
        shared/Threads/PartitionRange.cpp
        shared/Exp/exp.cpp
        shared/Triangle/AssociateSegmentToElement.cpp
        shared/Triangle/GridInsideHole.cpp
        shared/Triangle/OrderSegments.cpp
        shared/Triangle/SplitMeshForRifts.cpp
        shared/Triangle/TriangleUtils.cpp
        modules/Trianglex/Trianglex.cpp
        modules/ProcessRiftsx/ProcessRiftsx.cpp
        modules/PointCloudFindNeighborsx/PointCloudFindNeighborsx.cpp
        modules/PointCloudFindNeighborsx/PointCloudFindNeighborsxt.cpp
        modules/InterpFromGridToMeshx/InterpFromGridToMeshx.cpp
        modules/InterpFromMesh2dx/InterpFromMesh2dx.cpp
        modules/InterpFromMesh2dx/InterpFromMesh2dxt.cpp
        modules/InterpFromMeshToMesh3dx/InterpFromMeshToMesh3dx.cpp
        modules/InterpFromMeshToGridx/InterpFromMeshToGridx.cpp
        modules/MeshProfileIntersectionx/MeshProfileIntersectionx.cpp
        modules/ContourToMeshx/ContourToMeshx.cpp
        modules/ContourToMeshx/ContourToMeshxt.cpp
        modules/ExpToLevelSetx/ExpToLevelSetx.cpp
        modules/ExpToLevelSetx/ExpToLevelSetxt.cpp
        modules/ContourToNodesx/ContourToNodesx.cpp
        modules/DistanceToMaskBoundaryx/DistanceToMaskBoundaryx.cpp
        modules/DistanceToMaskBoundaryx/DistanceToMaskBoundaryxt.cpp
        modules/NodeConnectivityx/NodeConnectivityx.cpp
        modules/ElementConnectivityx/ElementConnectivityx.cpp
        modules/PropagateFlagsFromConnectivityx/PropagateFlagsFromConnectivityx.cpp
)
if (CHACO)
    list(APPEND MODULES_SOURCES
            modules/Chacox/Chacox.cpp
            modules/Chacox/input_parse.cpp
            modules/Chacox/chaco_seconds.cpp
            modules/Chacox/user_params.cpp
    )
endif ()
if (SCOTCH)
    list(APPEND MODULES_SOURCES
            modules/Scotchx/Scotchx.cpp
    )
endif ()
#}}}
# Kriging (wrapper and executable)
# Kriging sources {{{
if (KRIGING)
    list(APPEND ISSM_SOURCES
            classes/kriging/Observations.cpp
            classes/kriging/GaussianVariogram.cpp
            classes/kriging/ExponentialVariogram.cpp
            classes/kriging/SphericalVariogram.cpp
            classes/kriging/PowerVariogram.cpp
            classes/kriging/Quadtree.cpp
            classes/kriging/Covertree.cpp
            classes/kriging/Observation.cpp
            modules/Krigingx/pKrigingx.cpp
    )
    list(APPEND MODULES_SOURCES
            modules/Krigingx/Krigingx.cpp
            modules/Krigingx/pKrigingx.cpp
    )
endif ()
#}}}

add_library(libISSMCore STATIC ${ISSM_SOURCES})
target_link_libraries(libISSMCore m gfortran petsc mpi metis triangle)

add_library(libISSMModules STATIC ${MODULES_SOURCES})
target_link_libraries(libISSMModules m gfortran petsc mpi metis triangle)

if (NOT MSYS2)
    add_library(libISSMOverload STATIC
            shared/String/ApiPrintf.cpp
    )
    target_link_libraries(libISSMCore libISSMOverload)
    target_link_libraries(libISSMModules libISSMOverload)
endif ()
