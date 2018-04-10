# Mogi model estimation
# Set model type
ap_mogi_model = AutoParam('mogi')
# Set name (location) of PCA results
ap_mogi_pca_results = AutoParam('PCA')

# Create mogi analysis item
ana_mogi = skdiscovery.data_structure.series.analysis.Mogi_Inversion('Mogi', [ap_mogi_pca_results,ap_mogi_model])

# Create stagecontainer for mogi model
sc_mogi = StageContainer(ana_mogi)
