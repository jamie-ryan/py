
####insert test,py #something to import idl .sav file
import sunpy.map
import sunpy.data.sample
import matplotlib.pyplot as plt
from matplotlib import patches
smap = sunpy.map.Map(sunpy.data.sample.AIA_171_IMAGE)

fig = plt.figure()
ax = plt.subplot()

smap.plot()
rect = patches.Rectangle([-350, -650], 500, 500, color = 'white', fill=False)
ax.set_title('My customized plot')
ax.add_artist(rect)
plt.colorbar()
plt.show()



