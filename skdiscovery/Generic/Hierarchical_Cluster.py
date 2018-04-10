# Name of distance matrix:
ap_hcluster_name = 'Distance'

# Create HCluster 
acc_hclust = skdiscovery.data_structure.generic.accumulators.HCluster('HCluster',['Distance'])

# Create Stage Container for HCluster
sc_hclust = StageContainer(acc_hclust)
