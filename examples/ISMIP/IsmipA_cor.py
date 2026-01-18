import numpy as np
from plotmodel import plotmodel
from SetIceSheetBC import SetIceSheetBC
#Parameterization for ISMIP F experiment

#Set the Simulation generic name #md.miscellaneous
#->
md.miscellaneous.name = 'IsmipA_cor'
#Geometry
print('   Constructing Geometry')

#Define the geometry of the simulation #md.geometry
#surface is [-x * tan(3.0 * pi / 180)] #md.mesh
#->
md.geometry.surface = md.mesh.x * np.tan(0.5 * np.pi / 180.0)
#base is [surface - 1000 + 100 * exp(-((x - L / 2) .^ 2 + (y - L / 2) .^ 2) / (10000.^2))]
#L is the size of the side of the square #max(md.mesh.x) - min(md.mesh.x)
#->
L = np.nanmax(md.mesh.x) - np.nanmin(md.mesh.x)
#->
md.geometry.base = md.geometry.surface - 1000.0 + 500.0 * np.sin(md.mesh.x * 2.0 * np.pi / L) *  np.sin(md.mesh.y * 2.0 * np.pi / L)
#thickness is the difference between surface and base #md.geometry
#->
md.geometry.thickness = md.geometry.surface - md.geometry.base
#plot the geometry to check it out
#->

print('   Defining friction parameters')

#These parameters will not be used but need to be fixed #md.friction
#one friction coefficient per node (md.mesh.numberofvertices,1)
#conversion form year to seconds with #md.constants.yts
#->
md.friction.coefficient = 200.0 * np.ones((md.mesh.numberofvertices))
#one friction exponent (p, q) per element
#->
md.friction.p = np.ones(md.mesh.numberofelements)
#->
md.friction.q = np.ones(md.mesh.numberofelements)

print('   Construct ice rheological properties')

#The rheology parameters sit in the material section #md.materials
#B has one value per vertex
#->
md.materials.rheology_B = 6.8067e7 * np.ones(md.mesh.numberofvertices)
#n has one value per element
#->
md.materials.rheology_n = 3 * np.ones(md.mesh.numberofelements)

print('   Set boundary conditions')

#Set the default boundary conditions for an ice-sheet
# #help SetIceSheetBC
#->
md = SetIceSheetBC(md)
