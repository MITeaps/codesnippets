# Remove Linear, annual, and semiannual trends
# Note: The keyword annual also removes semiannual trends
# To only remove semiannual but not annual trends,
# replace 'annual' with 'semiannual'
ap_tf_type = AutoList(['linear','annual'])

# Create Trend Filter to remove linear, annual, and semi-annual trend
fl_tf = skdiscovery.data_structure.series.filters.TrendFilter('TrendFilter', [ap_tf_type])

# Create stage container for the trend filter
sc_tf = StageContainer(fl_tf)
