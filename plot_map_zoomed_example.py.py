import matplotlib.pyplot as plt
from matplotlib import patches
import astropy.units as u

import sunpy.map
import sunpy.data.sample


# Define a region of interest
l = 250*u.arcsec
x0 = -100*u.arcsec
y0 = -400*u.arcsec

# Create a SunPy Map, and a second submap over the region of interest.
smap = sunpy.map.Map(sunpy.data.sample.AIA_171_IMAGE)
submap = smap.submap(u.Quantity([x0-l, x0+l]), u.Quantity([y0-l, y0+l]))



# Create a new matplotlib figure, larger than default.
fig = plt.figure(figsize=(5,12))

# Add a first Axis, using the WCS from the map.
ax1 = fig.add_subplot(2,1,1, projection=smap.wcs)

# Plot the Map on the axes with default settings.
smap.plot()

# Define a region to highlight with a box
# We have to convert the region of interest to degress, and then get the raw values.
bottom_left = u.Quantity([x0-l, y0-l]).to(u.deg).value
l2 = (l*2).to(u.deg).value

# create the rectangle, we use the world transformation to plot in physical units.
rect = patches.Rectangle(bottom_left, l2, l2, color='white', fill=False,
                         transform=ax1.get_transform('world'))

# Add the rectangle to the plot.
ax1.add_artist(rect)



# Create a second axis on the plot.
ax2 = fig.add_subplot(2,1,2, projection=submap.wcs)

submap.plot()

# Add a overlay grid.
submap.draw_grid(grid_spacing=10*u.deg)

# Change the title.
ax2.set_title('Zoomed View')


plt.show()

