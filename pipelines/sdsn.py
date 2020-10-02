import importlib

# Identify the correct pipeline to run
def run_pipeline(indicator):
    if indicator == "sdsn_transmission_classification":
        pipeline = "sdsn_transmission_classification"
    else:
        pipeline = "sdsn_smoothed"
    print(">", "using sub-pipeline", pipeline, "...")

    # Load the pipeline
    module = importlib.import_module(".sdsn_pipelines." + pipeline, package=__package__)
    run_module_pipeline = getattr(module, "run_pipeline")

    # Run the pipeline
    run_module_pipeline(indicator)
