# Create a pipeline with a data fetcher and several stages
# Set analysis pipeline with stage containers
pipeline_items = [sc_stage1,
                  sc_stage2,
                  sc_stage3,]

# Create pipeline
pipeline = DiscoveryPipeline(data_fetcher, pipeline_items)
