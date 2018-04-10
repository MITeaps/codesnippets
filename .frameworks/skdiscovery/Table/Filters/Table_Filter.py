# Table filter to remove site with errors
# List of labels
ap_label_list = AutoList(['AV13'])

# Create table filter
fl_table = skdiscovery.data_structure.table.filters.TableFilter('TableFilter', [ap_label_list])

# Create Stage Container
sc_table = StageContainer(fl_table)
