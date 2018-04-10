# Create GPS Horizontal Plotter for PCA and MOGI
# Name of PCA or Mogi item
ap_pca_name = AutoParam('PCA')

# Create plotter item
acc_gpsplot = skdiscovery.data_structure.generic.accumulators.GPSHPlotter('GPSHPlotter',[ap_pca_name])

# Create Stage Container
sc_gpsplot = StageContainer(acc_gpsplot)
