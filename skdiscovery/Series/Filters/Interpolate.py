# Create Interpolation filter
fl_interpolate = skdiscovery.data_structure.series.filters.InterpolateFilter('Interpolate')

# Create stage containter for Interpolation filter
sc_interpolate = StageContainer(fl_interpolate)
