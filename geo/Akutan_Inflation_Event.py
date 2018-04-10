%matplotlib inline
import matplotlib.pyplot as plt
plt.rcParams['figure.figsize'] = (10,10)

from skdaccess.framework.param_class import *
from skdaccess.astro.kepler import DataFetcher as KDF
from skdaccess.geo.pbo import DataFetcher as PBODF
from skdaccess.geo.groundwater import DataFetcher as WDF
from skdaccess.geo.grace import DataFetcher as GRACEDF
from skdaccess.geo.gldas import DataFetcher as GLDASDF

# Setup skdiscovery
from skdiscovery import DiscoveryPipeline
from skdiscovery.framework.stagecontainers import *
import skdiscovery.table.filters
import skdiscovery.table.analysis
import skdiscovery.table.accumulators
import skdiscovery.series.filters
import skdiscovery.series.analysis
import skdiscovery.series.accumulators
import skdiscovery.generic.accumulators

# Start and end date
pbo_start_date = '2006-01-01'
pbo_end_date =   '2015-06-01'

# Select region around Alaska
pbo_lat_range = AutoList([50,75])
pbo_lon_range = AutoList([-175, -130])

# Retrieve station metadata
pbo_metadata = PBODF.getStationMetadata()

# Create the Data Fetcher to load the data
pbodf = PBODF(pbo_start_date, pbo_end_date, [pbo_lat_range, pbo_lon_range])

# Geo Location Filter for selecting data within a region of interest
# Lat/Lon used to define circular area of interest
ap_lat = AutoParam(54.13308)
ap_lon = AutoParam(-165.98555)

# Radius of circule of interes (km)
ap_radius = AutoParam(15)

# GeoLocation filter
fl_geo = skdiscovery.table.filters.GeoLocationFilter('GeoFilter',[ap_lat, ap_lon, ap_radius])
# Stage container for filter
sc_geo = StageContainer(fl_geo)

# Table filter to remove site with bad noise
# List of labels
ap_label_list = AutoList(['AV13'])

# Create table filter
fl_table = skdiscovery.table.filters.TableFilter('TableFilter', [ap_label_list])

# Create Stage Container
sc_table = StageContainer(fl_table)

# Create Stabilization Filter for stabilizing a region
fl_stab = skdiscovery.table.filters.StabilizationFilter('StabFilter')
# Stage container for filter
sc_stab = StageContainer(fl_stab)

# Set tau
ap_kf_tau = AutoParam(120)
# Set Sigma Squared
ap_kf_sigmasq = AutoParam(4)
# Set R
ap_kf_R = AutoParam(1)

# Create Kalman Smoother
fl_kf = skdiscovery.table.filters.KalmanFilter('Kalman Smoother', [ap_kf_tau, ap_kf_sigmasq, ap_kf_R])

# Create stage container for low pass filter
sc_kf = StageContainer(fl_kf)

# Principal Component Analysis with specified time window
# Set start time
ap_pca_start = AutoParam('2007-09-01')
# Set end time
ap_pca_end = AutoParam('2008-11-01')
# Set number of components
ap_pca_type = AutoParam('PCA')
# Set column names to use
pca_column_names = ('dN','dE')

# Create PCA analysis item
ana_gca = skdiscovery.table.analysis.General_Component_Analysis('PCA', [ap_pca_type, ap_pca_start, ap_pca_end],
                                                            n_components=3, column_names=pca_column_names)
# Create stagecontainer for PCA analysis                                                       
sc_gca = StageContainer(ana_gca)

# Create GPS Horizontal Plotter for PCA and MOGI
# Name of PCA or Mogi item
pca_name = 'PCA'

# Create plotter item
acc_gpsplot = skdiscovery.generic.accumulators.GPSHPlotter('GPSHPlotter',pca_name)

# Create Stage Container
sc_gpsplot = StageContainer(acc_gpsplot)

# Create pipeline
pipe = DiscoveryPipeline(pbodf,[sc_stab, sc_geo, sc_table, sc_kf, sc_gca, sc_gpsplot])

# Run Pipeline
pipe.run()
