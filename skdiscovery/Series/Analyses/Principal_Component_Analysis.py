# Principal Component Analysis with specified time window
# Number of components

# Start time
ap_pca_start = AutoParam('2007-09-01')
# End time
ap_pca_end = AutoParam('2008-11-01')
# Number of components
ap_pca_ncomponents = AutoParam(3)
# Set componenta analysis type
ap_pca_type = AutoParam('PCA')
# Set column names to use
pca_column_names = ('dN','dE')

pca_param_list = [ap_pca_ncomponents, ap_pca_type, 
                  ap_pca_start, ap_pca_end]

# Create PCA analysis item
ana_gca = skdiscovery.data_structure.series.analysis.General_Component_Analysis('PCA', pca_param_list)
                                                           
# Create stagecontainer for PCA analysis                                                       
sc_gca = StageContainer(ana_gca)
