# Set number of filter taps
ap_lp_ntaps = AutoParam(101)
# Set frequency passband ratio/percentage
ap_lp_fpassf_per = AutoParam(0.2)
# Set frequency stopband ratio/percentage
ap_lp_fstopf_per = AutoParam(0.3)
# Set band importance weights
al_lp_wghts = AutoList([1,1])
# Set maximum number of iterations for generating the filter
ap_lp_miter = AutoParam(100)

# Create Remez low pass filter
fl_lowpass = skdiscovery.data_structure.table.filters.LowPassFilter('LowPassFilter',
                                                 [ap_lp_ntaps,
                                                  ap_lp_fpassf_per,
                                                  ap_lp_fstopf_per,
                                                  al_lp_wghts, 
                                                  ap_lp_miter])

# Create stage container for the low pass filter
sc_lowpass = StageContainer(fl_lowpass)
