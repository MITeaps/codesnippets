# Start and end date
gw_start_date = '2010-01-01'
gw_end_date   = '2014-01-01'

# Bounds
gw_lower_lat = AutoParam(36)
gw_upper_lat = AutoParam(37)
gw_left_lon  = AutoParam(-121)
gw_right_lon = AutoParam(-117)

# Metadata
gw_metadata = WDF.getStationMetadata()

# Create data fetcher
wdf = WDF([gw_lower_lat, gw_upper_lat, gw_left_lon, gw_right_lon], gw_start_date, gw_end_date)
