import numpy as np
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

sie = np.append(asv.si_eimp[::,0],asv.si_eimp[::,1])
mge = np.append(asv.mg_eimp[::,0],asv.mg_eimp[::,1])
balmere = np.append(asv.balmer_eimp[::,0],asv.balmer_eimp[::,1])
mgwe = np.append(asv.mgw_eimp[::,0],asv.mgw_eimp[::,1])
hmie = np.append(asv.hmi_eimp[::,0],asv.hmi_eimp[::,1])

sicoords = np.zeros((2,20+1))
mgcoords = np.zeros((2,20+1))
balmercoords = np.zeros((2,20+1))
mgwcoords = np.zeros((2,20+1))
hmicoords = np.zeros((2,20+1))

sicoords[0,:10:] = csv.sicoords1[::,0]
sicoords[1,:10:] = csv.sicoords1[::,1]
sicoords[0,11::] = csv.sicoords2[::,0]
sicoords[1,11::] = csv.sicoords2[::,1]
sicoords[0,10] = 218.5
sicoords[1,10] = 262.5

mgcoords[0,:10:] = csv.mgcoords1[::,0]
mgcoords[1,:10:] = csv.mgcoords1[::,1]
mgcoords[0,11::] = csv.mgcoords2[::,0]
mgcoords[1,11::] = csv.mgcoords2[::,1]
mgcoords[0,10] = 218.5
mgcoords[1,10] = 262.5

balmercoords[0,:10:] = csv.balmercoords1[::,0]
balmercoords[1,:10:] = csv.balmercoords1[::,1]
balmercoords[0,11::] = csv.balmercoords2[::,0]
balmercoords[1,11::] = csv.balmercoords2[::,1]
balmercoords[0,10] = 218.5
balmercoords[1,10] = 262.5

mgwcoords[0,:10:] = csv.mgwcoords1[::,0]
mgwcoords[1,:10:] = csv.mgwcoords1[::,1]
mgwcoords[0,11::] = csv.mgwcoords2[::,0]
mgwcoords[1,11::] = csv.mgwcoords2[::,1]
mgwcoords[0,10] = 218.5
mgwcoords[1,10] = 262.5

hmicoords[0,:10:] = csv.hmicoords1[::,0]
hmicoords[1,:10:] = csv.hmicoords1[::,1]
hmicoords[0,11::] = csv.hmicoords2[::,0]
hmicoords[1,11::] = csv.hmicoords2[::,1]
hmicoords[0,10] = 218.5
hmicoords[1,10] = 262.5

#check order of coords with respect to associated energy array
#then try plotting E,  x,  z


#An Axes3D object is created just like any other axes using the projection=‘3d’ keyword. 
#Create a new matplotlib.figure.Figure and add a new axes to it of type Axes3D

#LINE PLOTS
#Axes3D.plot(xs, ys, *args, *kwargs)
#|args      |description
#|xs, ys    |x and y 
#|zs 	    |z value(s), either one for all points or one for each point
#|zdir 	    |Which direction to use as z (‘x’, ‘y’ or ‘z’) when plotting a 2D set.
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(sie[:21], sicoords[0,:], sicoords[1,::]  zdir='z')
plt.show()

#SCATTER PLOTS
# Axes3D.scatter(xs, ys, zs=0, zdir='z', s=20, c='b', depthshade=True, *args, **kwargs)
#|args      |description
#|xs, ys    |x and y 
#|zs 	    |Either an array of the same length as xs and ys or a single value to place all points in the same plane.Default is 0.
#|zdir 	    |Which direction to use as z (‘x’, ‘y’ or ‘z’) when plotting a 2D set.
#|s 	    |Size in points^2. It is a scalar or an array of the same length as x and y.
#|c 	    | color. c can be a single color format string, or a sequence of color specifications of length N, or a sequence of N numbers to be mapped to colors using the cmap and norm specified via kwargs (see below). Note that c should not be a single numeric RGB or RGBA sequence because that is indistinguishable from an array of values to be colormapped. c can be a 2-D array in which the rows are RGB or RGBA, however.
#|depthshade|Whether or not to shade the scatter markers to give the appearance of depth. Default is True.
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(sicoords[0,:], sicoords[1,::], sie[:21], zdir='z', s=20)
plt.show()
