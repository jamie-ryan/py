import numpy as np
import scipy 
import matplotlib.pyplot as plt
from scipy.io.idl import readsav
from mpl_toolkits.mplot3d import Axes3D

#use readsav as you would use idlsave.read.
filepath = '/home/jim/PhD/Jan20-2016/'
arraysav = '29-Mar-2014-integrated-energies-Jan20-2016.sav'
#structsav = '29-Mar-2014-integrated-energies-structureJan20-2016.sav'
coordsav = 'coord_arrays.sav'
asv = readsav(filepath+arraysav, verbose = True) 
#ssv = readsav(filepath+structsav, verbose = True) 
csv = readsav(filepath+coordsav, verbose = True) 

sie = asv.si_eimp
mge = asv.mg_eimp
balme = asv.balmer_eimp
mgwe = asv.mgw_eimp
hmie = asv.hmi_eimp


sic1 = csv.sicoords1
sic2 = csv.sicoords2

#or
cn = n_elements(csv.sicoords1)
sic = fltarr(2, 2*cn)
sic[*, 0: cn - 1] = csv.sicoords1
sic[*, cn: *] = csv.sicoords2

#then try plotting E,  x,  z


#An Axes3D object is created just like any other axes using the projection=‘3d’ keyword. 
#Create a new matplotlib.figure.Figure and add a new axes to it of type Axes3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

#LINE PLOTS
#Axes3D.plot(xs, ys, *args, *kwargs)
#|args      |description
#|xs, ys    |x and y 
#|zs 	    |z value(s), either one for all points or one for each point
#|zdir 	    |Which direction to use as z (‘x’, ‘y’ or ‘z’) when plotting a 2D set.


#SCATTER PLOTS
# Axes3D.scatter(xs, ys, zs=0, zdir='z', s=20, c='b', depthshade=True, *args, **kwargs)
#|args      |description
#|xs, ys    |x and y 
#|zs 	    |Either an array of the same length as xs and ys or a single value to place all points in the same plane.Default is 0.
#|zdir 	    |Which direction to use as z (‘x’, ‘y’ or ‘z’) when plotting a 2D set.
#|s 	    |Size in points^2. It is a scalar or an array of the same length as x and y.
#|c 	    | color. c can be a single color format string, or a sequence of color specifications of length N, or a sequence of N numbers to be mapped to colors using the cmap and norm specified via kwargs (see below). Note that c should not be a single numeric RGB or RGBA sequence because that is indistinguishable from an array of values to be colormapped. c can be a 2-D array in which the rows are RGB or RGBA, however.
#|depthshade|Whether or not to shade the scatter markers to give the appearance of depth. Default is True.

