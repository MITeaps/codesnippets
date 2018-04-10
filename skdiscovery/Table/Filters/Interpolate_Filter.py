# Create filter to linearly interpolate data
fl_interpolate = skdiscovery.data_structure.table.filtersInterpolateFilter('InterpolateFilter')

# Create stage container for the Interpolate filter
sc_interpolate = StageContainer(fl_interpolate)
