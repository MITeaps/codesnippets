# Principal Component Analysis with specified time window
# Set start time
ap_pca_start = AutoParam('2007-09-01')
# Set end time
ap_pca_end = AutoParam('2008-11-01')
# Set number of components
ap_pca_type = AutoParam('PCA')
# Set column names to use
pca_column_names = ('dN','dE')

# Create PCA analysis item
ana_gca = skdiscovery.data_structure.table.analysis.General_Component_Analysis('PCA', [ap_pca_type, ap_pca_start, ap_pca_end],
                                                            n_components=3, column_names=pca_column_names)
# Create stagecontainer for PCA analysis                                                       
sc_gca = StageContainer(ana_gca)
