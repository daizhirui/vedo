"""
 Convert a mesh it into volume (left in grey) representation as vtkImageData 
 where the foreground voxels are 1 and the background voxels are 0.
 Internally the vtkPolyDataToImageStencil class is used.
 
 Right: the vtkImageData is isosurfaced.
"""
from vtkplotter import *

s = load('data/shapes/bunny.obj').normalize().rotateZ(45).wire()#.cutPlane()

img = actor2ImageData(s, spacing=(.02,.02,.02))

v = Volume(img, alphas=[0,.5]) # alphas=[0,1,0]

iso = isosurface(img, smoothing=0.9).color('b')

show([v, s.scale(1.05), text(__doc__)], at=0, N=2, verbose=0)

show([iso], at=1, interactive=1)
