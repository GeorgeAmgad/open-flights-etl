import numpy as np

from pipelines.transformation_pipeline import TransformationPipeline
from transformers.transformation_steps import ReplaceInvalidValuesWithNullStep, NormalizeTextStep, ReplaceValuesStep


class RoutesPipeline:
    def __init__(self):
        self.pipeline = TransformationPipeline()
        self._setup_pipeline()

    def _setup_pipeline(self):
        self.pipeline.add_step(ReplaceValuesStep(column='codeshare', replacements={"Y": True, np.nan: False}))
        self.pipeline.add_step(ReplaceInvalidValuesWithNullStep())
        self.pipeline.add_step(
            NormalizeTextStep(columns=['source', 'destination', 'airline', 'codeshare', 'equipment']))

    def apply(self, data):
        return self.pipeline.apply(data)
