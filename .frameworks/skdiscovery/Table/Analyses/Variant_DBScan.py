# Variant DBScan analysis item
# Set variants
vdbscan_variants = pd.DataFrame({'eps': [2,2,3,3], 'mp' : [4,4,5,5]})
# Set column names
vdbscan_column_names = ('ra', 'dec')

# Create Variant DBScan analysis item
ana_vdbscan = skdiscovery.data_structure.table.analysis.VDBScan('VDBScan',vdbscan_variants, vdbscan_column_names)

# Create stage container for Variant DBScan analysis
sc_vdbscan = StageContainer(ana_vdbscan)
