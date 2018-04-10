# Start and end date
gldas_start_date = '2010-01-01'
gldas_end_date   = '2014-01-01'

# Location (Latitude and Longitude)
gldas_geo_point = AutoParam([(38, -117), (38, -118)])

# Create data fetcher
gldasdf = GLDASDF([gldas_geo_point],start_date=gldas_start_date,
                  end_date=gldas_end_date, resample=False)
