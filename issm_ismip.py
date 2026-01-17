import os
import sys
from pathlib import Path

ISSM_DIR = Path(__file__).parent.absolute()

sys.path.append(str(ISSM_DIR / 'bin'))
sys.path.append(str(ISSM_DIR / 'lib'))
sys.path.append(str(ISSM_DIR / 'share'))
sys.path.append(str(ISSM_DIR / 'share/proj'))

if sys.platform == 'linux':
    from issmversion import issmversion

    from model import *
    from squaremesh import squaremesh
    from plotmodel import plotmodel
    from export_netCDF import export_netCDF
    from loadmodel import loadmodel
    from setmask import setmask
    from parameterize import parameterize
    from setflowequation import setflowequation
    from socket import gethostname
    from solve import solve

elif sys.platform == 'win32':
    from bin.issmversion import issmversion

    from bin.model import *
    from bin.squaremesh import squaremesh
    from bin.plotmodel import plotmodel
    from bin.export_netCDF import export_netCDF
    from bin.loadmodel import loadmodel
    from bin.setmask import setmask
    from bin.parameterize import parameterize
    from bin.setflowequation import setflowequation
    from bin.socket import gethostname
    from bin.solve import solve

NEWTON = False

if NEWTON:
    img_path = Path(__file__).parent / 'output' / 'newton'
else:
    img_path = Path(__file__).parent / 'output' / 'picard'

img_path.mkdir(parents=True, exist_ok=True)


def main():
    os.chdir('examples/ISMIP')

    ParamFile = 'IsmipA_cor.py'

    print("Now generating the mesh")
    # initialize md as a new model help(model)
    # ->
    md = model()
    # generate a squaremesh help(squaremesh)
    # Side is 80 km long with 20 points
    # ->
    md = squaremesh(md, 80000, 80000, 20, 20)

    # plot the given mesh plotdoc()
    # ->
    plotmodel(md, 'data', 'mesh', 'figure', 1).savefig(img_path / 'mesh.png')
    # save the given model
    # ->
    export_netCDF(md, "./Models/ISMIP-Mesh_generation.nc")

    print("Setting the masks")
    # load the preceding step help(loadmodel)
    # path is given by the organizer with the name of the given step
    # ->
    md = loadmodel("./Models/ISMIP-Mesh_generation.nc")
    # set the mask help(setmask)
    # all MISMIP nodes are grounded
    # ->
    md = setmask(md, '', '')
    # plot the given mask #md.mask to locate the field
    # ->
    plotmodel(md, 'data', md.mask.ocean_levelset, 'figure', 2).savefig(img_path / 'mask.png')
    # save the given model
    # ->
    export_netCDF(md, "./Models/ISMIP-SetMask.nc")

    print("Parameterizing")
    # load the preceding step #help loadmodel
    # path is given by the organizer with the name of the given step
    # ->
    md = loadmodel("./Models/ISMIP-SetMask.nc")
    # parametrize the model # help parameterize
    # you will need to fill up the parameter file (given by the
    # ParamFile variable)
    # ->
    md = parameterize(md, ParamFile)
    # save the given model
    # ->
    export_netCDF(md, "./Models/ISMIP-Parameterization.nc")

    plotmodel(md, 'data', md.geometry.thickness).savefig(img_path / 'thickness.png')

    print("Extruding")
    # load the preceding step #help loadmodel
    # path is given by the organizer with the name of the given step
    # ->
    md = loadmodel("./Models/ISMIP-Parameterization.nc")
    # vertically extrude the preceding mesh #help extrude
    # only 5 layers exponent 1
    # ->
    md = md.extrude(5, 1)
    # plot the 3D geometry #plotdoc
    # ->
    plotmodel(md, 'data', md.geometry.base, 'figure', 3).savefig(img_path / 'geometry.png')
    # save the given model
    # ->
    export_netCDF(md, "./Models/ISMIP-Extrusion.nc")

    print("setting flow approximation")
    # load the preceding step #help loadmodel
    # path is given by the organizer with the name of the given step
    # ->
    md = loadmodel("./Models/ISMIP-Extrusion.nc")
    # set the approximation for the flow computation #help setflowequation
    # We will be using the Higher Order Model (HO)
    # ->
    md = setflowequation(md, 'HO', 'all')
    # save the given model
    # ->
    export_netCDF(md, "./Models/ISMIP-SetFlow.nc")

    print("setting boundary conditions")
    # load the preceding step #help loadmodel
    # path is given by the organizer with the name of the given step
    # ->
    md = loadmodel("./Models/ISMIP-SetFlow.nc")
    # dirichlet boundary condition are known as SPCs
    # ice frozen to the base, no velocity   #md.stressbalance
    # SPCs are initialized at NaN one value per vertex
    # ->
    md.stressbalance.spcvx = np.nan * np.ones((md.mesh.numberofvertices))
    # ->
    md.stressbalance.spcvy = np.nan * np.ones((md.mesh.numberofvertices))
    # ->
    md.stressbalance.spcvz = np.nan * np.ones((md.mesh.numberofvertices))
    # extract the nodenumbers at the base #md.mesh.vertexonbase
    # ->
    basalnodes = np.nonzero(md.mesh.vertexonbase)
    # set the sliding to zero on the bed (Vx and Vy)
    # ->
    md.stressbalance.spcvx[basalnodes] = 0.0
    # ->
    md.stressbalance.spcvy[basalnodes] = 0.0
    # periodic boundaries have to be fixed on the sides
    # Find the indices of the sides of the domain, for x and then for y
    # for x
    # create maxX, list of indices where x is equal to max of x (use >> help find)
    # ->
    maxX = np.squeeze(np.nonzero(md.mesh.x == np.nanmax(md.mesh.x)))
    # create minX, list of indices where x is equal to min of x
    # ->
    minX = np.squeeze(np.nonzero(md.mesh.x == np.nanmin(md.mesh.x)))
    # for y
    # create maxY, list of indices where y is equal to max of y
    # but not where x is equal to max or min of x
    # (i.e, indices in maxX and minX should be excluded from maxY and minY)
    # ->
    maxY = np.squeeze(np.nonzero(np.logical_and.reduce(
        (md.mesh.y == np.nanmax(md.mesh.y), md.mesh.x != np.nanmin(md.mesh.x), md.mesh.x != np.nanmax(md.mesh.x)))))
    # create minY, list of indices where y is equal to max of y
    # but not where x is equal to max or min of x
    # ->
    minY = np.squeeze(np.nonzero(np.logical_and.reduce(
        (md.mesh.y == np.nanmin(md.mesh.y), md.mesh.x != np.nanmin(md.mesh.x), md.mesh.x != np.nanmax(md.mesh.x)))))
    # set the node that should be paired together, minX with maxX and minY with maxY
    # #md.stressbalance.vertex_pairing
    # ->
    md.stressbalance.vertex_pairing = np.hstack((np.vstack((minX + 1, maxX + 1)), np.vstack((minY + 1, maxY + 1)))).T
    if ParamFile == 'IsmipF_cor.py':
        # if we are dealing with IsmipF the solution is in masstransport
        md.masstransport.vertex_pairing = md.stressbalance.vertex_pairing

    # save the given model
    # ->
    export_netCDF(md, "./Models/ISMIP-BoundaryCondition.nc")

    print("running the solver for the A case")
    # load the preceding step #help loadmodel
    # path is given by the organizer with the name of the given step
    # ->
    md = loadmodel("./Models/ISMIP-BoundaryCondition.nc")
    # Set cluster #md.cluster
    # generic parameters #help generic
    # set only the name and number of process
    # ->
    md.cluster = generic('name', gethostname(), 'np', 2)
    # Set which control message you want to see #help verbose
    # ->
    md.verbose = verbose('convergence', True)
    # Solve #help solve
    # we are solving a StressBalance
    # ->

    if NEWTON:
        md.stressbalance.isnewton = 1

    md.stressbalance.maxiter = 80

    md = solve(md, 'Stressbalance')
    # save the given model
    # ->
    export_netCDF(md, "./Models/ISMIP-StressBalance.nc")
    # plot the surface velocities #plotdoc
    # ->

    plotmodel(md, 'data', md.results.StressbalanceSolution.Vel, 'figure', 4).savefig(img_path / 'stressbalance.png')


if __name__ == '__main__':
    main()
