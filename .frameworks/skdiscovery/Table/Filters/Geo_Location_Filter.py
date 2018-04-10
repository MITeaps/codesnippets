# Geo Location Filter for selecting data within a region of interest
# Lat/Lon used to define circular area of interest
ap_lat = AutoParam(54.13308)
ap_lon = AutoParam(-165.98555)

# Radius of circule of interes (km)
ap_radius = AutoParam(15)

# GeoLocation filter
fl_geo = skdiscovery.data_structure.table.filters.GeoLocationFilter('GeoFilter',[ap_lat, ap_lon, ap_radius])
# Stage container for filter
sc_geo = StageContainer(fl_geo)

# Stabilization Filter used to stabalize GPS stations in a region
fl_stab = skdiscovery.data_structure.table.filters.StabilizationFilter('StabFilter')
# Stage container for filter
sc_stab = StageContainer(fl_stab)
