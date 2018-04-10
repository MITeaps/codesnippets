# Set window size
median_window = AutoParam(30)

# Create median filter
fl_median = skdiscovery.data_structure.table.filters.MedianFilter('Median Filter', [median_window], interpolate=True, subtract=False)

# Create stage container for the median filter
sc_median = StageContainer(fl_median)
