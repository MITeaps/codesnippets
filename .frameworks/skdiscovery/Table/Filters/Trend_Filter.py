# Create Trend Filter to remove linear, annual, and semi-annual trend
fl_tf = skdiscovery.data_structure.table.filters.TrendFilter('TrendFilter', [])

# Create stage container for the trend filter
sc_tf = StageContainer(fl_tf)
