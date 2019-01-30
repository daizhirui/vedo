'''
Use a scalar to paint colored bands on a mesh,
this can be combined with opacities values for each vertex of the mesh.
Keyword depthpeeling improves the rendering of translucent objects.
'''
from vtkplotter import Plotter, hyperboloid, torus, text
from numpy import linspace


vp = Plotter(depthpeeling=1, axes=2, verbose=0, bg='blackboard')

hyp = hyperboloid()
scalars = hyp.coordinates()[:,2]        # let z-coord be the scalar
hyp.pointColors(scalars, bands=5, cmap='rainbow') # make color bands

tor = torus(thickness=0.3)
scalars = tor.coordinates()[:,2]        # let z-coord be the scalar
transp = linspace(1, 0.5, len(scalars)) # set transparencies from 1 -> .5
tor.pointColors(scalars, alpha=transp, bands=3, cmap='winter')

# vp.addScalarBar(hyp, title='hyperboloid')
# vp.addScalarBar(tor, title='torus', horizontal=True)

doc=None
doc = text(__doc__, bg='lg')

vp.show([hyp, tor, doc], viewup='z')





