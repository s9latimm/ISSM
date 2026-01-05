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

    from model import model
    from triangle import triangle
    from setmask import setmask
    from parameterize import parameterize
    from setflowequation import setflowequation
    from solve import solve
    from plotmodel import plotmodel

elif sys.platform == 'win32':
    from bin.issmversion import issmversion

    from bin.model import model
    from bin.triangle import triangle
    from bin.setmask import setmask
    from bin.parameterize import parameterize
    from bin.setflowequation import setflowequation
    from bin.solve import solve
    from bin.plotmodel import plotmodel

if __name__ == '__main__':
    os.chdir('examples/SquareIceShelf')

    md = model()

    md = triangle(md, 'DomainOutline.exp', 50000)

    md = setmask(md, 'all', '')

    md = parameterize(md, 'Square.py')

    md.stressbalance.isnewton = 1

    md = setflowequation(md, 'SSA', 'all')

    md = solve(md, 'Stressbalance')

    plotmodel(md, 'data', md.results.StressbalanceSolution.Vel)
