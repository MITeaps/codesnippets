# Library Imports
%matplotlib inline
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
from skdaccess.geo.pbo import DataFetcher as PBODF
from skdiscovery.utilities.spherical_voronoi import getVoronoiCollection
import numpy as np
import pandas as pd


# Retrieve station metadata
pbo_metadata = PBODF.getStationMetadata()
pbo_metadata = pd.DataFrame.from_dict(pbo_metadata,orient='index')

llat = 24
ulat = 50
llon = -125
rlon = -66

# Create map
bmap= Basemap(llcrnrlat=llat, urcrnrlat=ulat, llcrnrlon=llon, 
             urcrnrlon=rlon,projection='gnom', lon_0=np.mean([llon,rlon]), 
             lat_0=np.mean([llat,ulat]), resolution='i')

# Get voronoi tessellation 
collection,sv,patch_index  = getVoronoiCollection(pbo_metadata, 'Lat','Lon',full_sphere=False,bmap=bmap)

# Create plot
fig = plt.figure()
ax = plt.gca()
fig.set_size_inches(8,8)

# Draw coastlines but not lakes and rivers
for i,cp in enumerate(bmap.coastpolygons):
     if bmap.coastpolygontypes[i]<2:
        bmap.plot(cp[0],cp[1],'k-')

# Add voronoi Polygons to map
ax.add_collection(collection)
