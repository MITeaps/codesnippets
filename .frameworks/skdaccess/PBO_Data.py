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
