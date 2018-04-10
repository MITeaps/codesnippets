# Set tau
ap_kf_tau = AutoParam(120)
# Set Sigma Squared
ap_kf_sigmasq = AutoParam(4)
# Set R
ap_kf_R = AutoParam(1)

# Create Kalman Smoother
fl_kf = skdiscovery.data_structure.table.filters.KalmanFilter('Kalman Smoother', [ap_kf_tau, ap_kf_sigmasq, ap_kf_R])

# Create stage container for low pass filter
sc_kf = StageContainer(fl_kf)
