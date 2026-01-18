import os
import sys
from pathlib import Path

ISSM_DIR = Path(__file__).parent.absolute()
__ISMIP_DIR = ISSM_DIR / 'examples' / 'ISMIP'

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

__OUTPUT = ISSM_DIR / 'output'
__OUTPUT.mkdir(parents=True, exist_ok=True)


def __param():
    print("Now generating the mesh")

    md = model()

    md = squaremesh(md, 80000, 80000, 20, 20)

    plotmodel(md, 'data', 'mesh', 'figure', 1).savefig(__OUTPUT / 'mesh.png')

    export_netCDF(md, "./Models/ISMIP-Mesh_generation.nc")

    print("Setting the masks")

    md = loadmodel("./Models/ISMIP-Mesh_generation.nc")

    md = setmask(md, '', '')

    plotmodel(md, 'data', md.mask.ocean_levelset, 'figure', 2).savefig(__OUTPUT / 'mask.png')

    export_netCDF(md, "./Models/ISMIP-SetMask.nc")

    print("Parameterizing")

    md = loadmodel("./Models/ISMIP-SetMask.nc")

    md = parameterize(md, 'IsmipA_cor.py')

    export_netCDF(md, "./Models/ISMIP-Parameterization.nc")

    plotmodel(md, 'data', md.geometry.thickness).savefig(__OUTPUT / 'thickness.png')

    print("Extruding")

    md = loadmodel("./Models/ISMIP-Parameterization.nc")

    md = md.extrude(5, 1)

    plotmodel(md, 'data', md.geometry.base, 'figure', 3).savefig(__OUTPUT / 'geometry.png')

    export_netCDF(md, "./Models/ISMIP-Extrusion.nc")

    print("setting flow approximation")

    md = loadmodel("./Models/ISMIP-Extrusion.nc")

    md = setflowequation(md, 'HO', 'all')

    export_netCDF(md, "./Models/ISMIP-SetFlow.nc")

    print("setting boundary conditions")

    md = loadmodel("./Models/ISMIP-SetFlow.nc")

    md.stressbalance.spcvx = np.nan * np.ones((md.mesh.numberofvertices))
    md.stressbalance.spcvy = np.nan * np.ones((md.mesh.numberofvertices))
    md.stressbalance.spcvz = np.nan * np.ones((md.mesh.numberofvertices))

    basalnodes = np.nonzero(md.mesh.vertexonbase)

    md.stressbalance.spcvx[basalnodes] = 0.0
    md.stressbalance.spcvy[basalnodes] = 0.0

    maxX = np.squeeze(np.nonzero(md.mesh.x == np.nanmax(md.mesh.x)))
    minX = np.squeeze(np.nonzero(md.mesh.x == np.nanmin(md.mesh.x)))
    maxY = np.squeeze(np.nonzero(np.logical_and.reduce(
        (md.mesh.y == np.nanmax(md.mesh.y), md.mesh.x != np.nanmin(md.mesh.x), md.mesh.x != np.nanmax(md.mesh.x)))))
    minY = np.squeeze(np.nonzero(np.logical_and.reduce(
        (md.mesh.y == np.nanmin(md.mesh.y), md.mesh.x != np.nanmin(md.mesh.x), md.mesh.x != np.nanmax(md.mesh.x)))))

    md.stressbalance.vertex_pairing = np.hstack((np.vstack((minX + 1, maxX + 1)), np.vstack((minY + 1, maxY + 1)))).T

    export_netCDF(md, "./Models/ISMIP-BoundaryCondition.nc")


def __solve(solver):
    print("running the solver for the A case")

    md = loadmodel("./Models/ISMIP-BoundaryCondition.nc")

    md.cluster = generic('name', gethostname(), 'np', 2)

    md.verbose = verbose('convergence', True)

    if solver == 'picard':
        md.stressbalance.isnewton = 0
    elif solver == 'newton':
        md.stressbalance.isnewton = 1
    elif solver == 'newton_steps':
        md.stressbalance.isnewton = 3
    elif solver == 'newton_steps':
        md.stressbalance.isnewton = 4

    md.stressbalance.maxiter = 100
    md.settings.solver_residue_threshold = 1e10

    try:
        md = solve(md, 'Stressbalance')
    except AttributeError:
        return

    export_netCDF(md, "./Models/ISMIP-StressBalance.nc")

    img_path = __OUTPUT / solver
    img_path.mkdir(parents=True, exist_ok=True)

    plotmodel(md, 'data', md.results.StressbalanceSolution.Vel, 'mesh', 4).savefig(
        img_path / 'stressbalance.png')


if __name__ == '__main__':
    os.chdir(__ISMIP_DIR)

    # __param()

    __solve('picard')
    __solve('newton')
    __solve('newton_steps')
    __solve('newton_half')
